from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.zone_distance import ZoneDistance

class ZoneDistanceRepository:
    
    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:tuple[int])-> ZoneDistance :
        return self.__session.get(ZoneDistance,id)
    
    def get_by_zone(self,id:int)->list[ZoneDistance]:
        return self.__session.query(ZoneDistance).where( or_(ZoneDistance.zone_id_1==id, ZoneDistance.zone_id_2==id)).all()
    
    def get_all(self)->list[ZoneDistance]:
        return self.__session.query(ZoneDistance).all()
    
    def add(self,zone_distance:ZoneDistance)->ZoneDistance:
        self.__session.add(zone_distance)
        self.__session.commit()
        return zone_distance
    
    def update(self,id:tuple[int],zone_distance:ZoneDistance)->ZoneDistance:
        existing =self.get_one(id)
        if existing:
            existing.zone_id_1=zone_distance.zone_id_1
            existing.zone_id_2=zone_distance.zone_id_2
            existing.zone_distance=zone_distance.zone_distance
            self.__session.commit()
        return existing

    def delete(self,zone_distance:ZoneDistance):
        self.__session.delete(zone_distance)
        self.__session.commit()
