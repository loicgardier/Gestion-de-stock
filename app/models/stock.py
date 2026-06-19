from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey

class Stock(Base):
    __tablename__="stock"

    product_id: Mapped[int] = mapped_column(Integer,ForeignKey('product.product_id'),primary_key=True)
    location_id : Mapped[int] = mapped_column(Integer,ForeignKey('location.location_id'),primary_key=True)
    quantity : Mapped[int] = mapped_column(Integer,nullable=False)

    product : Mapped["Product"] = relationship("Product",back_populates="stocks",uselist=False) 
    location : Mapped["Location"] = relationship("Location",back_populates="stocks",uselist=False)