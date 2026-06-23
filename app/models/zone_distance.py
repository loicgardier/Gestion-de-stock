from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Float,Integer,ForeignKey

class ZoneDistance(Base):
    __tablename__ = "zone_distance"

    zone_id_1 : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),primary_key=True)
    zone_id_2 : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),primary_key=True)
    zone_distance: Mapped[float] = mapped_column(Float,nullable=False)

    zone_1 : Mapped["Zone"] = relationship("Zone",foreign_keys=[zone_id_1],back_populates="zone_distances_1",uselist=False)
    zone_2 : Mapped["Zone"] = relationship("Zone",foreign_keys=[zone_id_2],back_populates="zone_distances_2",uselist=False)

    def __repr__(self):
        return f"<ZoneDistance {self.zone_id_1} - {self.zone_id_2} >"
    def __str__(self):
        return f"zone 1: {self.zone_1.zone_name} | zone 2: {self.zone_2.zone_name} | distance: {self.zone_distance}"