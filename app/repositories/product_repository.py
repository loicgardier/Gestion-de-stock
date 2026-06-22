from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:

    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:int)-> Product :
        return self.__session.get(Product,id)
    def get_all(self):
        return self.__session.query(Product).order_by(Product.product_id).all()
    
    def add(self,product:Product)->Product:
        self.__session.add(product)
        self.__session.commit()
        return product
    
    def update(self,id:int,product:Product)->Product:
        existing =self.get_one(id)
        if existing:
            existing.product_id=product.product_id
            existing.product_name=product.product_name
            self.__session.commit()
        return existing

    def delete(self,product:Product):
        self.__session.delete(product)
        self.__session.commit()