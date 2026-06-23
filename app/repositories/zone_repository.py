from sqlalchemy.orm import Session
from app.models.zone import Zone

class ZoneRepository:
    
    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:int)-> Zone :
        return self.__session.get(Zone,id)
    def get_all(self):
        return self.__session.query(Zone).all()
    
    def add(self,zone:Zone)->Zone:
        self.__session.add(zone)
        self.__session.commit()
        return zone
    
    def update(self,id:int,zone:Zone)->Zone:
        existing =self.get_one(id)
        if existing:
            existing.zone_id=zone.zone_id
            existing.zone_name=zone.zone_name
            self.__session.commit()
        return existing

    def delete(self,zone:Zone):
        self.__session.delete(zone)
        self.__session.commit()
