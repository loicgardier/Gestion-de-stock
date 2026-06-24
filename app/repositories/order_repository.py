from app.models.product_variant import ProductVariant
from app.models.location_order import LocationOrder
from app.models.location_order_product_variant import LocationOrderProductVariant
from app.models.transfert_order import TransfertOrder
from app.models.transfert_order_product_variant import TransfertOrderProductVariant
from app.models.order_status import OrderStatus
from app.models.user_oder_product_variant import UserOrderProductVariant
from app.models.user_order import UserOrder
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.stock import Stock


class OrderRepository:
    def __init__(self,session:Session):
        self.__session=session

    def get_order_status(self,order_status_name:str)->int:
        return self.__session.query(OrderStatus.order_status_id).where(OrderStatus.order_status_name==order_status_name).scalar()

    def replenishment_order(self,vendor_id:int,location_id:int,variant_list:list[tuple[int]]):
        location_order = LocationOrder()
        location_order.vendor_id=vendor_id
        location_order.location_id=location_id
        location_order.order_status_id = self.get_order_status("PENDING")
        self.__session.add(location_order)
        self.__session.flush()
        for variant in variant_list:
            location_order_product_variant =LocationOrderProductVariant()
            location_order_product_variant.location_order_id=location_order.location_order_id
            location_order_product_variant.product_variant_id=variant[0]
            location_order_product_variant.location_order_product_variant_quantity=variant[1]
            self.__session.add(location_order_product_variant)
        self.__session.commit()

    def replenishment_shipping(self,id:int):
        location_order = self.__session.get(LocationOrder,id)
        if location_order is None:
            raise ValueError(f"No order {id} found")
        location_order.order_status_id=self.get_order_status("SHIPPED")
        self.__session.commit()

    def replenishment_delivered(self,id:int):
        location_order = self.__session.get(LocationOrder,id)
        if location_order is None:
            raise ValueError(f"No order {id} found")
        location_order.order_status_id=self.get_order_status("DELIVERED")
        for location_order_product_variant in location_order.location_oder_product_variants:
            stock = self.__session.query(Stock).\
                where(and_(Stock.location_id==location_order.location_id,
                           Stock.product_variant_id == location_order_product_variant.product_variant_id)).scalar()
            if stock is None:
                stock=Stock()
                stock.location_id=location_order.location_id
                stock.product_variant_id=location_order_product_variant.product_variant_id
                stock.stock_quantity=location_order_product_variant.location_order_product_variant_quantity
                self.__session.add(stock)
            else:
                stock.stock_quantity+=location_order_product_variant.location_order_product_variant_quantity
        self.__session.commit()

    def replenishment_aborted(self,id:int):
        location_order = self.__session.get(LocationOrder,id)
        if location_order is None:
            raise ValueError(f"No order {id} found")
        location_order.order_status_id=self.get_order_status("ABORTED")
        self.__session.commit()  
        
    def transfert_order(self,from_location_id:int,to_location_id:int,variant_list:list[tuple[int]]):
        transfert_order = TransfertOrder()
        transfert_order.from_location_id=from_location_id
        transfert_order.to_location_id=to_location_id
        transfert_order.order_status_id = self.get_order_status("PENDING")
        self.__session.add(transfert_order)
        self.__session.flush()
        for variant in variant_list:
            transfert_order_product_variant =TransfertOrderProductVariant()
            transfert_order_product_variant.transfert_order_id=transfert_order.transfert_order_id
            transfert_order_product_variant.product_variant_id=variant[0]
            transfert_order_product_variant.transfert_oder_product_variant_quantity=variant[1]
            self.__session.add(transfert_order_product_variant)
        self.__session.commit()

    def transfert_shipping(self,id:int):
        transfert_order = self.__session.get(TransfertOrder,id)
        if transfert_order is None:
            raise ValueError(f"No order {id} found")
        transfert_order.order_status_id=self.get_order_status("SHIPPED")
        for transfert_order_product_variant in transfert_order.transfert_oder_product_variants:
            stock = self.__session.query(Stock).\
                where(and_(Stock.location_id==transfert_order.from_location_id,
                           Stock.product_variant_id == transfert_order_product_variant.product_variant_id)).scalar()
            if stock is None:
                self.__session.rollback()
                raise ValueError(f"Missing product in stock")
            else:
                stock.stock_quantity-=transfert_order_product_variant.transfert_oder_product_variant_quantity
                if stock.stock_quantity<0:
                    self.__session.rollback()
                    raise ValueError(f"Too few product in stock")
        self.__session.commit()

    def transfert_delivered(self,id:int):
        transfert_order = self.__session.get(TransfertOrder,id)
        if transfert_order is None:
            raise ValueError(f"No order {id} found")
        for transfert_order_product_variant in transfert_order.transfert_oder_product_variants:
            stock = self.__session.query(Stock).\
                where(and_(Stock.location_id==transfert_order.to_location_id,
                        Stock.product_variant_id == transfert_order_product_variant.product_variant_id)).scalar()
            if stock is None:
                stock = Stock()
                stock.location_id=transfert_order.to_location_id
                stock.product_variant_id = transfert_order_product_variant.product_variant_id
                self.__session.add(stock)
            else:
                stock.stock_quantity+=transfert_order_product_variant.transfert_oder_product_variant_quantity
        transfert_order.order_status_id=self.get_order_status("ABORTED")
        self.__session.commit()  

    def transfert_aborted(self,id:int):
        transfert_order = self.__session.get(TransfertOrder,id)
        if transfert_order is None:
            raise ValueError(f"No order {id} found")
        if transfert_order.order_status_id == self.get_order_status("SHIPPED"):
            for transfert_order_product_variant in transfert_order.transfert_oder_product_variants:
                stock = self.__session.query(Stock).\
                    where(and_(Stock.location_id==transfert_order.from_location_id,
                            Stock.product_variant_id == transfert_order_product_variant.product_variant_id)).scalar()
                if stock is None:
                    self.__session.rollback()
                    raise ValueError(f"Missing product in stock")
                else:
                    stock.stock_quantity+=transfert_order_product_variant.transfert_oder_product_variant_quantity
        transfert_order.order_status_id=self.get_order_status("ABORTED")
        self.__session.commit()  

    def user_order(self,user_id,variant_list:list[tuple[int]],user_order_promotion=0):
        user_order = UserOrder()
        user_order.user_id=user_id
        user_order.user_order_promotion=user_order_promotion
        user_order.order_status_id = self.get_order_status("PENDING")
        self.__session.add(user_order)
        self.__session.flush()
        for variant in variant_list:
            user_order_product_variant =UserOrderProductVariant()
            user_order_product_variant.user_order_id=user_order.user_id
            user_order_product_variant.product_variant_id=variant[0]
            user_order_product_variant.user_oder_product_variant_quantity=variant[1]
            self.__session.add(user_order_product_variant)
        self.__session.commit()
