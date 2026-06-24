from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey

class LocationOrderProductVariant(Base):
    __tablename__="location_oder_product_variant"

    product_variant_id: Mapped[int] = mapped_column(Integer,ForeignKey('product_variant.product_variant_id'),primary_key=True)
    location_order_id : Mapped[int] = mapped_column(Integer,ForeignKey('location_order.location_order_id'),primary_key=True)
    location_order_product_variant_quantity : Mapped[int] = mapped_column(Integer,nullable=False)

    product_variant : Mapped["ProductVariant"] = relationship("ProductVariant",back_populates="location_oder_product_variants",uselist=False) 
    location_order : Mapped["LocationOrder"] = relationship("LocationOrder",back_populates="location_oder_product_variants",uselist=False)

    def __repr__(self):
        return f"<LocationOrderProductVariant {self.product_variant_id}-{self.location_order_id}>"