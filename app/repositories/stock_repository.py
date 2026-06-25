from sqlalchemy.orm import Session,aliased
from sqlalchemy import and_
from app.models.stock import Stock
from app.models.location_order_product_variant import LocationOrderProductVariant
from app.models.user_order_product_variant import UserOrderProductVariant
from app.models.transfert_order_product_variant import TransfertOrderProductVariant
from app.models.location_order import LocationOrder
from app.models.user_order import UserOrder
from app.models.transfert_order import TransfertOrder
from app.models.user import User
from app.models.location import Location
from app.models.order_status import OrderStatus


class StockRepository:

    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:tuple[int])-> Stock :
        return self.__session.get(Stock,id)
    
    def get_by_location(self,id:int):
        return self.__session.query(Stock).where(Stock.location_id==id).all()
    
    def get_all(self):
        return self.__session.query(Stock).order_by(Stock.location_id).all()
    
    def get_prevision(self):

        '''
SELECT sub4.location_name,sub4.product_name,sub4.product_variant_color,sub4.product_variant_size,
sub4.stock_quantity+COALESCE(sub4."lopv sum",0)-COALESCE(sub4."ftopv sum",0)+COALESCE(sub4."ttopv sum",0)-COALESCE(sub4."uopv sum",0)
FROM(
	SELECT sub3.location_id,sub3.product_variant_id, sub3.location_name,sub3.product_name,sub3.product_variant_color,sub3.product_variant_size,sub3.stock_quantity,sub3.zone_id,
	sub3."lopv sum",sub3."ftopv sum",sub3."ttopv sum",
	SUM(uopv.user_order_product_variant_quantity) as "uopv sum"
	FROM
		(SELECT sub2.location_id,sub2.product_variant_id, sub2.location_name,sub2.product_name,sub2.product_variant_color,sub2.product_variant_size,sub2.stock_quantity,sub2.zone_id,
		sub2."lopv sum",sub2."ftopv sum",
		SUM(ttopv.transfert_order_product_variant_quantity) as "ttopv sum"
		FROM (SELECT sub1.location_id,sub1.product_variant_id, sub1.location_name,sub1.product_name,sub1.product_variant_color,sub1.product_variant_size,sub1.stock_quantity,sub1.zone_id,
				sub1."lopv sum",
				SUM(ftopv.transfert_order_product_variant_quantity) as "ftopv sum"
			FROM (SELECT s.location_id,s.product_variant_id,l.location_name,p.product_name,pv.product_variant_color,pv.product_variant_size,s.stock_quantity,l.zone_id,
				SUM(lopv.location_order_product_variant_quantity) as "lopv sum"
				FROM STOCK s
				JOIN Location l on (s.location_id=l.location_id)
				JOIN PRODUCT_VARIANT pv on (pv.product_variant_id = s.product_variant_id)
				JOIN PRODUCT p on (p.product_id = pv.product_id)
				LEFT JOIN LOCATION_ORDER lo on (lo.location_id = s.location_id)
				LEFT JOIN LOCATION_ORDER_PRODUCT_VARIANT lopv ON (lo.location_order_id=lopv.location_order_id 
																AND s.product_variant_id = lopv.product_variant_id)
				LEFT JOIN ORDER_STATUS loos on (lo.order_status_id = loos.order_status_id)
				WHERE loos.order_status_name in ('PENDING','SHIPPED') or loos.order_status_name is NULL
				GROUP BY s.location_id,s.product_variant_id,l.location_name,p.product_name,pv.product_variant_color,pv.product_variant_size,s.stock_quantity,l.zone_id) sub1
			LEFT JOIN TRANSFERT_ORDER fto on (fto.from_location_id = sub1.location_id)
			LEFT JOIN TRANSFERT_ORDER_PRODUCT_VARIANT ftopv on (ftopv.transfert_order_id=fto.transfert_order_id 
															AND ftopv.product_variant_id=sub1.product_variant_id)
			LEFT JOIN ORDER_STATUS ftoos on (fto.order_status_id = ftoos.order_status_id)
			WHERE ftoos.order_status_name in ('PENDING') or ftoos.order_status_name is NULL
			GROUP BY sub1.location_id,sub1.product_variant_id, sub1.location_name,sub1.product_name,sub1.product_variant_color,sub1.product_variant_size,sub1.stock_quantity,
				sub1.zone_id,sub1."lopv sum") sub2
		LEFT JOIN TRANSFERT_ORDER tto on (tto.to_location_id = sub2.location_id)
		LEFT JOIN TRANSFERT_ORDER_PRODUCT_VARIANT ttopv on (ttopv.transfert_order_id=tto.transfert_order_id 
														AND ttopv.product_variant_id=sub2.product_variant_id)
		LEFT JOIN ORDER_STATUS ttoos on (tto.order_status_id = ttoos.order_status_id)
		WHERE ttoos.order_status_name in ('PENDING','SHIPPED') or ttoos.order_status_name is NULL
		GROUP BY sub2.location_id,sub2.product_variant_id, sub2.location_name,sub2.product_name,sub2.product_variant_color,sub2.product_variant_size,sub2.stock_quantity,sub2.zone_id,
		sub2."lopv sum",sub2."ftopv sum") sub3
	LEFT JOIN "user" u on (u.zone_id = sub3.zone_id)
	LEFT JOIN USER_ORDER uo on (uo.user_id=u.user_id)
	LEFT JOIN USER_ORDER_PRODUCT_VARIANT uopv on (uopv.user_order_id=uo.user_order_id 
												AND uopv.product_variant_id=sub3.product_variant_id)
	LEFT JOIN ORDER_STATUS uoos on (uo.order_status_id = uoos.order_status_id)
	WHERE uoos.order_status_name in ('PENDING') or uoos.order_status_name is NULL
	GROUP BY sub3.location_id,sub3.product_variant_id, sub3.location_name,sub3.product_name,sub3.product_variant_color,sub3.product_variant_size,sub3.stock_quantity,
		sub3.zone_id,sub3."lopv sum",sub3."ftopv sum",sub3."ttopv sum"
	)sub4
ORDER BY sub4.location_name,sub4.product_name,sub4.product_variant_color,sub4.product_variant_size;


'''
        from_transfer =aliased(TransfertOrder)
        to_transfer = aliased(TransfertOrder)
        user_order_status = aliased(OrderStatus)
        from_transfert_status = aliased(OrderStatus)
        to_transfert_status = aliased(OrderStatus)
        location_order_status = aliased(OrderStatus)
        prediction = self.__session.query(Stock,
            LocationOrderProductVariant.location_order_product_variant_quantity,
            UserOrderProductVariant.user_oder_product_variant_quantity,
            TransfertOrderProductVariant.transfert_oder_product_variant_quantity).\
            outerjoin(LocationOrderProductVariant,LocationOrderProductVariant.product_variant_id==Stock.product_variant_id).\
            join(LocationOrder,and_(LocationOrder.location_order_id==LocationOrderProductVariant.location_order_id,
                                    LocationOrder.location_id==Stock.location_id)).\
            outerjoin(TransfertOrderProductVariant,TransfertOrderProductVariant.product_variant_id==Stock.product_variant_id).\
            join(from_transfer,and_(from_transfer.transfert_order_id==TransfertOrderProductVariant.transfert_order_id,
                                     from_transfer.from_location_id==Stock.location_id)).\
            join(to_transfer,and_(to_transfer.transfert_order_id==TransfertOrderProductVariant.transfert_order_id,
                                     to_transfer.to_location_id==Stock.location_id)).\
            outerjoin(UserOrderProductVariant,UserOrderProductVariant.product_variant_id==Stock.product_variant_id).\
            join(UserOrder,UserOrder.user_order_id==UserOrderProductVariant.user_order_id).\
            join(Location,Location.location_id==Stock.location_id).\
            join(User,and_(User.user_id==UserOrder.user_id,User.zone_id==Location.zone_id)).\
            join(user_order_status,user_order_status.order_status_id==UserOrder.order_status_id).\
            join(from_transfert_status,from_transfert_status.order_status_id==from_transfer.order_status_id).\
            join(to_transfert_status,to_transfert_status.order_status_id==to_transfer.order_status_id).\
            join(location_order_status,location_order_status.order_status_id==LocationOrder.order_status_id)
        
        return prediction.all()
        
    
    def add(self,stock:Stock)->Stock:
        self.__session.add(stock)
        self.__session.commit()
        return stock
    def update(self,id:tuple[int],stock:Stock)->Stock:
        existing =self.get_one(id)
        if existing:
            existing.product_id=stock.product_id
            existing.location_id=stock.location_id
            existing.stock_quantity=stock.stock_quantity
            self.__session.commit()
        return existing
    
    def delete(self,stock:Stock):
        self.__session.delete(stock)
        self.__session.commit()

