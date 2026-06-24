#promotion
from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey
from .order import Order

class UserOrder(Base,Order):
    __tablename__ = "user_order"

    user_order_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer,ForeignKey('user.user_id'),nullable=False)
    order_status_id: Mapped[int] = mapped_column(Integer,ForeignKey('order_status.order_status_id'),nullable=False)
    user_order_promotion: Mapped[int] = mapped_column(Integer,nullable=False,default='0',server_default='0')

    status : Mapped["OrderStatus"] =relationship("OrderStatus",back_populates="user_orders",uselist=False)
    user_oder_product_variants : Mapped[list["UserOrderProductVariant"]] =relationship("UserOrderProductVariant",back_populates="user_order")
    user : Mapped["User"] =relationship("User",back_populates="user_orders",uselist=False)



    def __repr__(self):
        return f"<UserOrder {self.user_order_id}>"
    
    def __str__(self):
        return f"id: {self.user_order_id} | status: {self.status.order_status_name}"