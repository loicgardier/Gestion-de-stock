from sqlalchemy.orm import Session
from app.models.catalog import Catalog
from app.models.vendor import Vendor

class VendorRepository:
    
    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:int)-> Vendor :
        return self.__session.get(Vendor,id)
    def get_all(self)->list[Vendor]:
        return self.__session.query(Vendor).order_by(Vendor.vendor_id).all()
    
    def add(self,vendor:Vendor)->Vendor:
        self.__session.add(vendor)
        self.__session.commit()
        return vendor
    
    def update(self,id:int,vendor:Vendor)->Vendor:
        existing =self.get_one(id)
        if existing:
            existing.vendor_id=vendor.vendor_id
            existing.vendor_name=vendor.vendor_name
            existing.zone_id=vendor.zone_id
            self.__session.commit()
        return existing

    def delete(self,vendor:Vendor):
        self.__session.query(Catalog).where(Catalog.vendor_id==vendor.vendor_id).delete()
        self.__session.flush()
        self.__session.delete(vendor)
        self.__session.commit()
