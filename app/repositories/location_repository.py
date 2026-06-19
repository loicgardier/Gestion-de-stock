from sqlalchemy.orm import Session
from app.models.location import Location

class LocationRepository:
    
    def __init__(self,session:Session):
        self.__session=session

    def get_one(self,id:int)-> Location :
        return self.__session.get(Location,id)
    def get_all(self):
        return self.__session.query(Location).all()
    
    def add(self,location:Location)->Location:
        self.__session.add(location)
        self.__session.commit()
        return location
    
    def update(self,id:int,location:Location)->Location:
        existing =self.get_one(id)
        if existing:
            existing.location_id=location.location_id
            existing.location_name=location.location_name
            self.__session.commit()
        return existing

    def delete(self,location:Location):
        self.__session.delete(location)
        self.__session.commit()
