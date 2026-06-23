from .base import Base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey

class Vendor(Base):
    __tablename__ = "vendor"

    vendor_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    vendor_name: Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    zone_id : Mapped[int] = mapped_column(Integer,ForeignKey('zone.zone_id'),nullable=False,server_default='1')

    catalogs : Mapped[list["Catalog"]] = relationship("Catalog",back_populates="vendor")
    zone : Mapped["Zone"] =relationship("Zone",back_populates="vendors",uselist=False)

    def __repr__(self):
        return f"<Vendor {self.vendor_name}>"
    
    def __str__(self):
        return f"id: {self.vendor_id} | name: {self.vendor_name} | zone: {self.zone.zone_name}"