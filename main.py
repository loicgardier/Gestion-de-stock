from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from app.repositories.location_repository import LocationRepository
from app.repositories.stock_repository import StockRepository
from app.repositories.product_repository import ProductRepository
from app.models.location import Location
from app.models.product import Product
from app.models.stock import Stock
from app.ui.simple_ui import SimpleUI

SimpleUI().run()





'''
config = dotenv_values(".env")  
engine=create_engine(config.get("DATABASE_CONNECTION_STRING"))
session_local = sessionmaker(autoflush=False,bind=engine)

'''
'''
with session_local() as session:
    location_repository = LocationRepository(session)
    location = Location()
    location.location_name="San antonio"
    location_repository.add(location)
    product = Product()
    product.product_name="chausette"
    product_repository = ProductRepository(session)
    product_repository.add(product)
    stock = Stock()
    stock.location_id=location.location_id
    stock.product_id=product.product_id
    stock.quantity=21
    stock_repository= StockRepository(session)
    stock_repository.add(stock)

    print("OK")
'''
'''
with session_local() as session:
    stock_repository= StockRepository(session)

    stock = stock_repository.get_one(2,5)

    print(stock.product.product_name,stock.location.location_name)
'''
'''
with session_local() as session:
    product = Product()
    product.product_name="bas collant"
    product_repository = ProductRepository(session)
    product_repository.add(product)
    stock = Stock()
    stock.location_id=5
    stock.product_id=product.product_id
    stock.quantity=23
    stock_repository= StockRepository(session)
    stock_repository.add(stock)

'''
'''
with session_local() as session:
    location_repository = LocationRepository(session)
    to_print= location_repository.get_all()
    print(to_print[0].stocks[1].quantity)


with session_local() as session:
    stock_repository= StockRepository(session)
    to_print= stock_repository.get_all()
    print(to_print[0].location)

'''