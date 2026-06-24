from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey,DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    user_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    user_firstname: Mapped[str] = mapped_column(String(50),nullable=False)
    user_lastname: Mapped[str] = mapped_column(String(50),nullable=False)
    user_birthday: Mapped[datetime] = mapped_column(DateTime,nullable=False)
    user_mail: Mapped[str] = mapped_column(String(50),nullable=False)
    zone_id : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),nullable=False,server_default='1')

    zone : Mapped["Zone"] =relationship("Zone",back_populates="users",uselist=False)
    user_orders : Mapped[list["UserOrder"]] =relationship("UserOrder",back_populates="user")
    
    def __repr__(self):
        return f"<User {self.user_firstname} {self.user_lastname}>"
    
    def __str__(self):
        return f"{self.user_firstname} {self.user_lastname}"