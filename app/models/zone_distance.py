from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Float,Integer,ForeignKey

class ZoneDistance(Base):
    __tablename__ = "zone_distance"

    zone_id_1 : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),primary_key=True)
    zone_id_2 : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),primary_key=True)
    zone_distance: Mapped[float] = mapped_column(Float,nullable=False)

    zones_1 : Mapped[list["Zone"]] = relationship("Zone",foreign_keys=[zone_id_1],back_populates="zone_distances_1")
    zones_2 : Mapped[list["Zone"]] = relationship("Zone",foreign_keys=[zone_id_2],back_populates="zone_distances_2")