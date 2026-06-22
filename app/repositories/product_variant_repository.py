from sqlalchemy.orm import Session
from app.models.product_variant import ProductVariant

class ProductVariantRepository:

    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:int)-> ProductVariant :
        return self.__session.get(ProductVariant,id)
    def get_all(self)->list[ProductVariant]:
        return self.__session.query(ProductVariant).order_by(ProductVariant.product_variant_id).all()
    def get_by_product(self,id:int)->list[ProductVariant]:
        return self.__session.query(ProductVariant).where(ProductVariant.product_id==id).all()

    
    def add(self,product_variant:ProductVariant)->ProductVariant:
        if product_variant.product_variant_price is None:
            product_variant.product_variant_price=product_variant.product.product_base_price
        self.__session.add(product_variant)
        self.__session.commit()
        return product_variant
    
    def update(self,id:int,product_variant:ProductVariant)->ProductVariant:
        existing =self.get_one(id)
        if existing:
            existing.product_variant_id=product_variant.product_variant_id
            existing.product_id=product_variant.product_id
            existing.product_variant_size=product_variant.product_variant_size
            existing.product_variant_color=product_variant.product_variant_color
            if product_variant.product_variant_price:
                existing.product_variant_price=product_variant.product_variant_price
            else:
                existing.product_variant_price=existing.product.product_base_price
            self.__session.commit()
        return existing

    def delete(self,product_variant:ProductVariant):
        self.__session.delete(product_variant)
        self.__session.commit()