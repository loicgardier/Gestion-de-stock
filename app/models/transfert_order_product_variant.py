from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey

class TransfertOrderProductVariant(Base):
    __tablename__="transfert_oder_product_variant"

    product_variant_id: Mapped[int] = mapped_column(Integer,ForeignKey('product_variant.product_variant_id'),primary_key=True)
    transfert_order_id : Mapped[int] = mapped_column(Integer,ForeignKey('transfert_order.transfert_order_id'),primary_key=True)
    transfert_oder_product_variant_quantity : Mapped[int] = mapped_column(Integer,nullable=False)

    product_variant : Mapped["ProductVariant"] = relationship("ProductVariant",back_populates="transfert_oder_product_variants",uselist=False) 
    transfert_order : Mapped["TransfertOrder"] = relationship("TransfertOrder",back_populates="transfert_oder_product_variants",uselist=False)

    def __repr__(self):
        return f"<TransfertOrderProductVariant {self.product_variant_id}-{self.transfert_order_id}>"