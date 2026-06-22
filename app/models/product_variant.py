from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,Float,ForeignKey,CheckConstraint

class ProductVariant(Base):
    __tablename__="product_variant"

    product_variant_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer,ForeignKey('product.product_id'),nullable=False)
    product_variant_size: Mapped[str] = mapped_column(String,
                                CheckConstraint("product_variant_size in ('XXS','XS','S','M','L','XL','XXL','XXXL')",
                                                name="ck_product_variant_size"),nullable=False)
    product_variant_color: Mapped[str] = mapped_column(String,nullable=False,server_default="Blanc")
    product_variant_price: Mapped[float] = mapped_column(Float,nullable=False,server_default='0')

    stocks : Mapped[list["Stock"]] = relationship("Stock",back_populates="product_variant")
    product : Mapped["Product"] = relationship("Product",back_populates="product_variants",uselist=False)

    def __repr__(self):
        return f"<class ProductVariant {self.product_variant_id}>"