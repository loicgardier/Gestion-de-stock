from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey

class UserOrderProductVariant(Base):
    __tablename__="user_oder_product_variant"

    product_variant_id: Mapped[int] = mapped_column(Integer,ForeignKey('product_variant.product_variant_id'),primary_key=True)
    user_order_id : Mapped[int] = mapped_column(Integer,ForeignKey('user_order.user_order_id'),primary_key=True)
    user_oder_product_variant_quantity : Mapped[int] = mapped_column(Integer,nullable=False)

    product_variant : Mapped["ProductVariant"] = relationship("ProductVariant",back_populates="user_oder_product_variants",uselist=False) 
    user_order : Mapped["UserOrder"] = relationship("UserOrder",back_populates="user_oder_product_variants",uselist=False)

    def __repr__(self):
        return f"<TransfertOrderProductVariant {self.product_variant_id}-{self.user_order_id}>"