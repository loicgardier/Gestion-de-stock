from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

from app.repositories.location_repository import LocationRepository
from app.repositories.stock_repository import StockRepository
from app.repositories.product_repository import ProductRepository
from app.models.location import Location
from app.models.product import Product
from app.models.stock import Stock

class SimpleUI:
    def __init__(self):
        self.config = dotenv_values(".env")  
        self.engine=create_engine(self.config.get("DATABASE_CONNECTION_STRING"))
        self.session_local = sessionmaker(autoflush=False,bind=self.engine)

    def run(self):
        print("Bienvenu dans l'application gestion de stock")
        self.main_menu()

    def main_menu(self):
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("Operation:")
            print("\t1 - transfert")
            print("\t2 - replenishment")
            print("Products")
            print("\t3 - product")
            print("\t4 - product variant")
            print("Reporting")
            print("\t5 - location")
            print("\t6 - stock")
            print("Configuration")
            print("\t7 - location")
            print("\t8 - vendor")
            print("\n\t0 - Quitter l'application")

            while choix<0 or choix>8:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 0 et 8")
            match choix:
                case 1: self.operation_transfert()
                case 2: self.operation_replenishment()
                case 3: self.product_product()
                case 4: self.product_product_variant()
                case 5: self.reporting_location()
                case 6: self.reporting_stock()
                case 7: self.configuration_location()
                case 8: self.configuration_vendor()
                case 0: return
            choix=-1

    def operation_transfert(self):
        print("Operation: transfert")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass


    def operation_replenishment(self):
        print("Operation: reple,ishment")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass

    def product_product(self):
        print("Product: product")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher la liste des produits")
            print("\t2 - Ajouter un produit")
            print("\t3 - Modifier un produit")

            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>3:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 3")
                if choix<0 and choix>3:
                    print("Veillez à entrer un chiffre entre 0 et 3")
            match choix:
                case 1:self.show_product()
                case 2:pass
                case 3:pass
                case 0:return
            choix=-1

    def show_product(self):
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            table = product_repository.get_all()
            for elem in table:
                print(elem)


    def product_product_variant(self):
        print("Product: Product variant")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass

    def reporting_location(self):
        print("Reporting: location")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass

    def reporting_stock(self):
        print("Reporting: stock")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass

    def configuration_location(self):
        print("Configuration: location")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass

    def configuration_vendor(self):
        print("configuration: vendor")
        choix=-1
        while choix!=0:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>0:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 1 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 1 et 8")
            match choix:
                case 1:pass