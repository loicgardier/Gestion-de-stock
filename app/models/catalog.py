from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Float,Integer,ForeignKey

class Catalog(Base):
    __tablename__="catalog"

    product_variant_id: Mapped[int] = mapped_column(Integer,ForeignKey('product_variant.product_variant_id'),primary_key=True)
    vendor_id : Mapped[int] = mapped_column(Integer,ForeignKey('vendor.vendor_id'),primary_key=True)
    catalog_selling_price : Mapped[float] = mapped_column(Float,nullable=False)

    product_variant : Mapped["ProductVariant"] = relationship("ProductVariant",back_populates="catalogs",uselist=False) 
    vendor : Mapped["Vendor"] = relationship("Vendor",back_populates="catalogs",uselist=False)