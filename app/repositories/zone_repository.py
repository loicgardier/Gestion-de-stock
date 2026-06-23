from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.zone import Zone
from app.models.zone_distance import ZoneDistance
from app.models.location import Location

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
        self.__session.query(ZoneDistance)\
            .where(or_( ZoneDistance.zone_id_1==zone.zone_id, ZoneDistance.zone_id_2 == zone.zone_id))\
            .delete()
        locations = self.__session.query(Location).where(Location.zone_id==zone.zone_id)
        for location in locations:
            location.zone_id=1
        self.__session.flush()
        self.__session.delete(zone)
        self.__session.commit()
