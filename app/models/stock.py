from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey

class Stock(Base):
    __tablename__="stock"

    product_variant_id: Mapped[int] = mapped_column(Integer,ForeignKey('product_variant.product_variant_id'),primary_key=True)
    location_id : Mapped[int] = mapped_column(Integer,ForeignKey('location.location_id'),primary_key=True)
    stock_quantity : Mapped[int] = mapped_column(Integer,nullable=False)

    product_variant : Mapped["ProductVariant"] = relationship("ProductVariant",back_populates="stocks",uselist=False) 
    location : Mapped["Location"] = relationship("Location",back_populates="stocks",uselist=False)

    def __repr__(self):
        return f"<Stock {self.product_variant_id}-{self.location_id}>"
    
    def __str__(self):
        return f"id: {self.product_variant_id} | name: {self.product_variant.product.product_name} {self.product_variant.product_variant_color} {self.product_variant.product_variant_size} | quantity: {self.stock_quantity}"