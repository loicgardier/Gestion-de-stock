from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer

class Zone(Base):
    __tablename__ = "zone"

    zone_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    zone_name: Mapped[str] = mapped_column(String(50),nullable=False,unique=True)

    locations : Mapped[list["Location"]] = relationship("Location",back_populates="zone")
    zone_distances_1 : Mapped[list["ZoneDistance"]] = relationship("ZoneDistance",
                                                                  foreign_keys="ZoneDistance.zone_id_1",
                                                                  back_populates="zone_1")
    zone_distances_2 : Mapped[list["ZoneDistance"]] = relationship("ZoneDistance",
                                                                  foreign_keys="ZoneDistance.zone_id_2",
                                                                  back_populates="zone_2")
    def __repr__(self):
        return f"<Zone {self.zone_name}>"
    
    def __str__(self):
        return f"id: {self.zone_id} | name: {self.zone_name}"