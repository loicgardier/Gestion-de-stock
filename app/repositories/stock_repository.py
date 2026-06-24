from sqlalchemy.orm import Session
from app.models.stock import Stock

class StockRepository:

    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,product_id:int,location_id:int)-> Stock :
        return self.__session.get(Stock,{'product_id':product_id,'location_id':location_id})
    def get_all(self):
        return self.__session.query(Stock).all()
    
    def add(self,stock:Stock)->Stock:
        self.__session.add(stock)
        self.__session.commit()
        return stock
    
    def update(self,product_id:int,location_id:int,stock:Stock)->Stock:
        existing =self.get_one(product_id,location_id)
        if existing:
            existing.product_id=stock.product_id
            existing.location_id=stock.location_id
            existing.stock_quantity=stock.stock_quantity
            self.__session.commit()
        return existing

    def delete(self,stock:Stock):
        self.__session.delete(stock)
        self.__session.commit()