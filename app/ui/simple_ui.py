from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

from app.repositories.location_repository import LocationRepository
from app.models.location import Location
from app.repositories.stock_repository import StockRepository
from app.models.stock import Stock
from app.repositories.product_repository import ProductRepository
from app.models.product import Product
from app.repositories.product_variant_repository import ProductVariantRepository
from app.models.product_variant import ProductVariant

from sqlalchemy.exc import IntegrityError

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

#region Product product
    def product_product(self):
        print("Product: product")
        choix=-1
        while True:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher la liste des produits")
            print("\t2 - Ajouter un produit")
            print("\t3 - Modifier un produit")
            print("\t4 - Supprimer un produit")

            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>4:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 4")
                if choix<0 and choix>3:
                    print("Veillez à entrer un chiffre entre 0 et 4")
            match choix:
                case 1:self.show_product()
                case 2:self.add_product()
                case 3:self.update_product()
                case 4:self.delete_product()
                case 0:return
            choix=-1

    def show_product(self):
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            table = product_repository.get_all()
            for elem in table:
                print(elem)

    def add_product(self):
        product=Product()
        product.product_name=input("Entrez le nom du produit:")
        product.product_description=input("Entrez une description:")
        while True:
            try:
                product.product_base_price=float(input("Entrez le prix du produit:"))
                break
            except:
                pass
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            product_repository.add(product)
            print("Produit ajouté")
            print(product)

    def update_product(self):
        self.show_product()
        while True:
            try:
                id=int(input("Entrez l'id du produit à moddifier:"))
                break
            except:
                pass
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            product = product_repository.get_one(id)
        if product is None:
            print("Produit non trouvé")
        else:
            #si le champs est vide pas de modification
            val=input("Entrez le nouveau nom:")
            if val:
                product.product_name=val
            val=input("Entrez la nouvelle description:")
            if val:
                product.product_description=val
            while True:
                try:
                    val=input("Entrez le prix du produit:")
                    if val:
                        product.product_base_price=float(val)
                    break
                except:
                    pass
            with self.session_local() as session:
                product_repository=ProductRepository(session)
                product_repository.update(id,product)
            print("Produit modifié")
            print(product)

    def delete_product(self):
        self.show_product()
        while True:
            try:
                id=int(input("Entrez l'id du produit à supprimer:"))
                break
            except:
                pass
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            product = product_repository.get_one(id)
            if product is None:
                print("Produit non trouvé")
            else:
                product_repository.delete(product)
                print("Produit supprimé")
#endregion

#region Product product_variant
    def product_product_variant(self):
        print("Product: Product variant")
        choix=-1
        while True:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher la liste des produits et les variants")
            print("\t2 - Ajouter un variant à un produit")
            print("\t3 - Modifier le variant d'un produit")
            print("\t4 - Supprimer le variant d'un produit")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>4:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 4")
                if choix<0 and choix>4:
                    print("Veillez à entrer un chiffre entre 0 et 4")
            match choix:
                case 1:self.show_product_variant()
                case 2:self.add_product_variant()
                case 3:self.update_product_variant()
                case 4:self.delete_product_variant()
                case 0:return
            choix=-1

    def show_product_variant(self):
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            table = product_repository.get_all()
            for product in table:
                print(product)
                for variant in product.product_variants:
                    print("\t\t",variant,sep="")

    def add_product_variant(self):
        self.show_product()
        product_variant=ProductVariant()
        product_variant.product_id=input("Entrez l'id du produit:")
        with self.session_local() as session:
            product_repository=ProductRepository(session)
            product_variant.product = product_repository.get_one(product_variant.product_id)
            if not product_variant.product:
                print("Id du produit incorect")
                return
        product_variant.product_variant_color=input("Entrez une couleur:")
        product_variant.product_variant_size=input("Entrez une taille:")
        while True:
            try:
                val=input("Entrez le prix du variant:")
                if val:
                    product_variant.product_variant_price=float(val)
                break
            except:
                pass
        with self.session_local() as session:
            product_variant_repository=ProductVariantRepository(session)
            try:
                product_variant_repository.add(product_variant)
                print("Variant ajouté")
                print(product_variant)
            except IntegrityError as e:
                    print(e.__cause__)

    def update_product_variant(self):
        self.show_product_variant()
        while True:
            try:
                id=int(input("Entrez l'id du produit à moddifier:"))
                break
            except:
                pass
        with self.session_local() as session:
            product_variant_repository=ProductVariantRepository(session)
            product_variant = product_variant_repository.get_one(id)
        if product_variant is None:
            print("Variant non trouvé")
        else:
            #si le champs est vide pas de modification
            val=input("Entrez la nouvelle couleur:")
            if val:
                product_variant.product_variant_color=val
            val=input("Entrez la nouvelle taille:")
            if val:
                product_variant.product_variant_size=val
            while True:
                try:
                    val=input("Entrez le prix du produit:")
                    if val:
                        product_variant.product_variant_price=float(val)
                    break
                except:
                    pass
            with self.session_local() as session:
                product_variant_repository=ProductVariantRepository(session)
                try:
                    product_variant_repository.update(id,product_variant)
                    print("Variant modifié")
                    print(product_variant)
                except IntegrityError as e:
                    print(e.__cause__)


    def delete_product_variant(self):
        self.show_product_variant()
        while True:
            try:
                id=int(input("Entrez l'id du variant à supprimer:"))
                break
            except:
                pass
        with self.session_local() as session:
            product_variant_repository=ProductVariantRepository(session)
            product_variant = product_variant_repository.get_one(id)
            if product_variant is None:
                print("Variant non trouvé")
            else:
                product_variant_repository.delete(product_variant)
                print("Produit supprimé")

#endregion

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
        while True:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher les zones")
            print("\t2 - Ajouter une zone")
            print("\t3 - Modifier une zone")
            print("\t4 - Supprimer une zone")
            print("\t5 - Configurer la distance entre deux zone")
            print("\t6 - Afficher les location")
            print("\t7 - Ajouter une location")
            print("\t8 - Modifier une location")
            print("\t9 - Supprimer une location")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>9:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 9")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 0 et 9")
            match choix:
                case 1:pass
                case 2:pass
                case 3:pass
                case 4:pass
                case 5:pass
                case 6:pass
                case 7:pass
                case 8:pass
                case 9:pass
                case 0:return
            choix=-1

    


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