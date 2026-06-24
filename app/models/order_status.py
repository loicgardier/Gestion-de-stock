#promotion
from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Integer,String

class OrderStatus(Base):
    __tablename__ = "order_status"

    order_status_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    order_status_name : Mapped[str] = mapped_column(String,nullable=False)

    user_orders : Mapped[list["UserOrder"]] = relationship("UserOrder",back_populates="status")
    transfert_orders : Mapped[list["TransfertOrder"]] = relationship("TransfertOrder",back_populates="status")
    location_orders : Mapped[list["LocationOrder"]] = relationship("LocationOrder",back_populates="status")


    def __repr__(self):
        return f"<OrderStatus {self.order_status_name}>"
    
    def __str__(self):
        return f"id: {self.order_status_id} | status: {self.order_status_name}"