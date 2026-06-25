#promotion
from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey

class LocationOrder(Base):
    __tablename__ = "location_order"

    location_order_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    location_id : Mapped[int] = mapped_column(Integer,ForeignKey('location.location_id'),nullable=False)
    vendor_id : Mapped[int] = mapped_column(Integer,ForeignKey('vendor.vendor_id'),nullable=False)
    order_status_id: Mapped[int] = mapped_column(Integer,ForeignKey('order_status.order_status_id'),nullable=False)

    status : Mapped["OrderStatus"] =relationship("OrderStatus",back_populates="location_orders",uselist=False)
    location_oder_product_variants : Mapped[list["LocationOrderProductVariant"]] = relationship("LocationOrderProductVariant",back_populates="location_order")

    vendor : Mapped["Vendor"] =relationship("Vendor",back_populates="location_orders",uselist=False)
    location : Mapped["Location"] =relationship("Location",back_populates="location_orders",uselist=False)

    def __repr__(self):
        return f"<LocationOrder {self.user_order_id}>"
    
    def __str__(self):
        return f"id: {self.location_order_id} | status: {self.status.order_status_name}"