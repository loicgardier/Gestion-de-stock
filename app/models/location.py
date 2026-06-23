from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey

class Location(Base):
    __tablename__ = "location"

    location_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    location_name: Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    zone_id : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),nullable=False)

    stocks : Mapped[list["Stock"]] = relationship("Stock",back_populates="location")
    zone : Mapped["Zone"] =relationship("Zone",back_populates="locations",uselist=False)