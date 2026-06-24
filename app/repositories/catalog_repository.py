from sqlalchemy.orm import Session
from app.models.catalog import Catalog
from app.models.product import Product
from app.models.product_variant import ProductVariant

class CatalogRepository:

    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:tuple[int])-> Catalog :
        return self.__session.get(Catalog,id)
    
    def get_by_vendor(self,id:int):
        return self.__session.query(Catalog)\
            .where(Catalog.vendor_id==id)\
            .join(ProductVariant,Catalog.product_variant_id==ProductVariant.product_variant_id)\
            .join(Product,ProductVariant.product_id==Product.product_id)\
            .order_by(Product.product_id)\
            .all()

    def get_all(self) -> list[Catalog]:
        return self.__session.query(Catalog).all()
    
    def add(self,catalog:Catalog)->Catalog:
        self.__session.add(catalog)
        self.__session.commit()
        return catalog
    
    def update(self,id:tuple[int],catalog:Catalog)->Catalog:
        existing =self.get_one(id)
        if existing:
            existing.product_variant_id=catalog.product_variant_id
            existing.vendor_id=catalog.vendor_id
            existing.catalog_selling_price=catalog.catalog_selling_price
            self.__session.commit()
        return existing

    def delete(self,catalog:Catalog):
        self.__session.delete(catalog)
        self.__session.commit()