from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,Float

class Product(Base):
    __tablename__="product"

    product_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    product_name : Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    product_description : Mapped[str] = mapped_column(String(1000),nullable=True)
    product_base_price: Mapped[float] = mapped_column(Float,nullable=False,server_default='0')

    product_variants : Mapped[list["ProductVariant"]] = relationship("ProductVariant",back_populates="product")

    def __str__(self):
        return f"id: {self.product_id} | name: {self.product_name} | base price: {self.product_base_price} \
| description: {'NULL' if self.product_description is None 
                else self.product_description if len(self.product_description)<20 
                else self.product_description[:18]+'...'} \
| number of variant: {len(self.product_variants)}"
    def __repr__(self):
        return f"<class Product {self.product_id}>"