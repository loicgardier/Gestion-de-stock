from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,Float

class Product(Base):
    __tablename__="product"

    product_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    product_name : Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    product_description : Mapped[str] = mapped_column(String(1000),nullable=True)
    product_base_price: Mapped[float] = mapped_column(Float,nullable=False,server_default='0')

    stocks : Mapped[list["Stock"]] = relationship("Stock",back_populates="product")