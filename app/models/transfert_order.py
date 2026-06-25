#promotion
from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey

class TransfertOrder(Base):
    __tablename__ = "transfert_order"

    transfert_order_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    from_location_id : Mapped[int] = mapped_column(Integer,ForeignKey('location.location_id'),nullable=False)
    to_location_id : Mapped[int] = mapped_column(Integer,ForeignKey('location.location_id'),nullable=False)
    order_status_id: Mapped[int] = mapped_column(Integer,ForeignKey('order_status.order_status_id'),nullable=False)

    status : Mapped["OrderStatus"] =relationship("OrderStatus",back_populates="transfert_orders",uselist=False)

    transfert_oder_product_variants : Mapped[list["TransfertOrderProductVariant"]] =relationship("TransfertOrderProductVariant",back_populates="transfert_order")

    from_location : Mapped["Location"] = relationship("Location",foreign_keys=[from_location_id],back_populates="from_locations",uselist=False)
    to_location : Mapped["Location"] = relationship("Location",foreign_keys=[to_location_id],back_populates="to_locations",uselist=False)

    def __repr__(self):
        return f"<UserOrder {self.user_order_id}>"
    
    def __str__(self):
        return f"id: {self.user_order_id} | status: {self.status.order_status_name}"