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
from app.models.zone import Zone
from app.repositories.zone_repository import ZoneRepository
from app.models.zone_distance import ZoneDistance
from app.repositories.zone_distance_repository import ZoneDistanceRepository
from app.models.vendor import Vendor
from app.repositories.vendor_repository import VendorRepository
from app.models.catalog import Catalog
from app.repositories.catalog_repository import CatalogRepository

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
            print("\t1 - location")
            print("\t2 - user")
            print("Products")
            print("\t3 - product")
            print("\t4 - product variant")
            print("Configuration")
            print("\t5 - zone")
            print("\t6 - location")
            print("\t7 - vendor")
            print("\n\t0 - Quitter l'application")

            while choix<0 or choix>8:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 8")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 0 et 8")
            match choix:
                case 1: self.operation_location()
                case 2: self.operation_user()
                case 3: self.product_product()
                case 4: self.product_product_variant()
                case 5: self.configuration_zone()
                case 6: self.configuration_location()
                case 7: self.configuration_vendor()
                case 0: return
            choix=-1

    def operation_location(self):
        print("Operation: location")
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


    def operation_user(self):
        print("Operation: user")
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
                print("\t",elem,sep="")

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
            print("\t",product,sep="")

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
            print("\t",product,sep="")

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
                print("\t",product,sep="")
                for variant in product.product_variants:
                    print("\t\t",variant,sep="")

    def add_product_variant(self):
        self.show_product()
        product_variant=ProductVariant()
        while True:
            try:
                product_variant.product_id=int(input("Entrez l'id du produit:"))
                break
            except:
                pass
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

#region Configuration zone

    def configuration_zone(self):
        print("Configuration: zone")
        choix=-1
        while True:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher les zones")
            print("\t2 - Ajouter une zone")
            print("\t3 - Modifier une zone")
            print("\t4 - Supprimer une zone")
            print("\t5 - Configurer la distance entre deux zone")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>5:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 5")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 0 et 5")
            match choix:
                case 1:self.show_zone()
                case 2:self.add_zone()
                case 3:self.update_zone()
                case 4:self.delete_zone()
                case 5:self.configure_zone_distance()
                case 0:return
            choix=-1  

    def show_zone(self):
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            table = zone_repository.get_all()
            for zone in table:
                print("\t",zone,sep="")

    def add_zone(self):
        zone=Zone()
        zone.zone_name=input("Entrez le nom de la zone:")
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone_repository.add(zone)
            print("Zone ajouté")
            print("\t",zone,sep="")

    def update_zone(self):
        self.show_zone()
        while True:
            try:
                id=int(input("Entrez l'id de la zone à moddifier:"))
                break
            except:
                pass
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone = zone_repository.get_one(id)
        if zone is None:
            print("Zone non trouvé")
        else:
            #si le champs est vide pas de modification
            val=input("Entrez le nouveau nom:")
            if val:
                zone.zone_name=val
            with self.session_local() as session:
                zone_repository=ZoneRepository(session)
                zone_repository.update(id,zone)
            print("zone modifié")
            print("\t",zone,sep="")

    def delete_zone(self):
        self.show_zone()
        while True:
            try:
                id=int(input("Entrez l'id de la zone à supprimer:"))
                break
            except:
                pass
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone = zone_repository.get_one(id)
            if zone is None:
                print("Zone non trouvé")
            else:
                zone_repository.delete(zone)
                print("Zone supprimé")

    def configure_zone_distance(self):
        self.show_zone()
        while True:
            try:
                id_1=int(input("Entrez l'id de la zone à configurer:"))
                break
            except:
                pass
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone = zone_repository.get_one(id_1)
            if zone is None:
                print("Zone non trouvé")
                return
            zone_distance_repository=ZoneDistanceRepository(session)
            existing =zone_distance_repository.get_by_zone(id_1)
            print(f"Distance configurée: {len(existing)//2}")
            for zone_distance in existing:
                print("\t",zone_distance,sep="")
        while True:
            try:
                id_2=int(input("Entrez l'id de la zone avec laquelle la distance va être ajouté:"))
                break
            except:
                pass
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone = zone_repository.get_one(id_2)
            if zone is None:
                print("Zone non trouvé")
                return
            if id_1==id_2:
                print("la distance doit être calculer entre 2 location différente")
                return
            
            zone_distance_repository=ZoneDistanceRepository(session)

            existing=zone_distance_repository.get_one((id_1,id_2))
            existing2=zone_distance_repository.get_one((id_2,id_1))
            if existing:
                while True:
                    try:
                        val=input("Entrez la distance de la zone 1 vers la zone 2:")
                        if val:
                            distance_aller=float(val)
                        else:
                            distance_aller=existing.zone_distance
                        break
                    except:
                        pass
                while True:
                    try:
                        val=input("Entrez la distance de la zone 2 vers la zone 1:")
                        if val:
                            distance_retour=float(val)
                        else:
                            distance_retour=existing2.zone_distance
                        break
                    except:
                        pass

                zone_distance_1 = ZoneDistance()
                zone_distance_1.zone_id_1=id_1
                zone_distance_1.zone_id_2=id_2
                zone_distance_1.zone_distance=distance_aller
                zone_distance_2 = ZoneDistance()
                zone_distance_2.zone_id_1=id_2
                zone_distance_2.zone_id_2=id_1
                zone_distance_2.zone_distance=distance_retour
                
                zone_distance_repository=ZoneDistanceRepository(session)
                zone_distance_1=zone_distance_repository.update((id_1,id_2),zone_distance_1)
                zone_distance_2=zone_distance_repository.update((id_2,id_1),zone_distance_2)

                print("Distance modifiée")

            else:
                while True:
                    try:
                        distance_aller=float(input("Entrez la distance de la zone 1 vers la zone 2:"))
                        break
                    except:
                        pass
                while True:
                    try:
                        val=input("Entrez la distance de la zone 2 vers la zone 1:")
                        if val:
                            distance_retour=float(val)
                        else:
                            distance_retour=distance_aller
                        break
                    except:
                        pass
                zone_distance_1 = ZoneDistance()
                zone_distance_1.zone_id_1=id_1
                zone_distance_1.zone_id_2=id_2
                zone_distance_1.zone_distance=distance_aller
                zone_distance_2 = ZoneDistance()
                zone_distance_2.zone_id_1=id_2
                zone_distance_2.zone_id_2=id_1
                zone_distance_2.zone_distance=distance_retour
                
                zone_distance_repository=ZoneDistanceRepository(session)
                zone_distance_1=zone_distance_repository.add(zone_distance_1)
                zone_distance_2=zone_distance_repository.add(zone_distance_2)
                print("Distance ajoutée")
            
            print("\t",zone_distance_1,sep="")
            print("\t",zone_distance_2,sep="")

#endregion

#region Configuration location

    def configuration_location(self):
        print("Configuration: location")
        choix=-1
        while True:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher les location")
            print("\t2 - Ajouter une location")
            print("\t3 - Modifier une location")
            print("\t4 - Supprimer une location")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>9:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 4")
                if choix<1 and choix>8:
                    print("Veillez à entrer un chiffre entre 0 et 4")
            match choix:
                case 1:self.show_location()
                case 2:self.add_location()
                case 3:self.update_location()
                case 4:self.delete_location()
                case 0:return
            choix=-1  


    def show_location(self):
            with self.session_local() as session:
                location_repository=LocationRepository(session)
                table = location_repository.get_all()
                for location in table:
                    print("\t",location,sep="")

    def add_location(self):
        location=Location()
        location.location_name=input("Entrez le nom de la location:")
        self.show_zone()
        while True:
            try:
                id=int(input("Entrez l'id de la zone dans laquel se trouve la location:"))
                break
            except:
                pass
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone = zone_repository.get_one(id)
            if zone is None:
                print("Zone non trouvé")
                return
            location.zone_id=id
            location_repository=LocationRepository(session)
            location=location_repository.add(location)
            print("Location ajouté")
            print("\t",location,sep="")


    def update_location(self):
        self.show_location()
        while True:
            try:
                id=int(input("Entrez l'id de la location à moddifier:"))
                break
            except:
                pass
        with self.session_local() as session:
            location_repository=LocationRepository(session)
            location = location_repository.get_one(id)
        if location is None:
            print("Location non trouvé")
        else:
            #si le champs est vide pas de modification
            val=input("Entrez le nouveau nom:")
            if val:
                location.location_name=val
            self.show_zone()

            while True:
                try:
                    val = input("Entrez l'id de la zone dans laquel se trouve la location:")
                    if val:
                        id_zone=int(val)
                    else:
                        id_zone=None
                    break
                except:
                    pass
            with self.session_local() as session:
                zone_repository=ZoneRepository(session)
                zone = zone_repository.get_one(id_zone)
                if zone is None:
                    pass
                else:
                    location.zone_id=id_zone

            with self.session_local() as session:
                location_repository=LocationRepository(session)
                location=location_repository.update(id,location)
                print("Location modifié")
                print("\t",location,sep="")

    def delete_location(self):
        self.show_location()
        while True:
            try:
                id=int(input("Entrez l'id de la location à supprimer:"))
                break
            except:
                pass
        with self.session_local() as session:
            location_repository=LocationRepository(session)
            location = location_repository.get_one(id)
            if location is None:
                print("Location non trouvé")
            else:
                location_repository.delete(location)
                print("Location supprimé")

#endregion

#region Configuration vendor

    def configuration_vendor(self):
        print("Configuration: vendor")
        choix=-1
        while True:
            print("Entrez le chiffre corespondant a votre choix:")
            print("\t1 - Afficher les vendeurs")
            print("\t2 - Ajouter un vendeurs")
            print("\t3 - Modifier un vendeur")
            print("\t4 - Supprimer un vendeur")
            print("\t5 - Afficher le catalogue d'un vendeur")
            print("\t6 - Modifier le catalogue d'un vendeur")
            print("\n\t0 - Revenir au menu principal")

            while choix<0 or choix>6:
                try:
                    choix=int(input("Votre choix:"))
                except:
                    print("Veillez à entrer un chiffre entre 0 et 6")
                if choix<0 and choix>6:
                    print("Veillez à entrer un chiffre entre 0 et 6")
            match choix:
                case 1:self.show_vendor()
                case 2:self.add_vendor()
                case 3:self.update_vendor()
                case 4:self.delete_vendor()
                case 5:self.show_vendor_catalog()
                case 6:self.update_catalog()
                case 0:return
            choix=-1  


    def show_vendor(self):
            with self.session_local() as session:
                vendor_repository=VendorRepository(session)
                table = vendor_repository.get_all()
                for vendor in table:
                    print("\t",vendor,sep="")

    def add_vendor(self):
        vendor=Vendor()
        vendor.vendor_name=input("Entrez le nom du vendeur:")
        self.show_zone()
        while True:
            try:
                id=int(input("Entrez l'id de la zone dans laquel se trouve le vendeur:"))
                break
            except:
                pass
        with self.session_local() as session:
            zone_repository=ZoneRepository(session)
            zone = zone_repository.get_one(id)
            if zone is None:
                print("Zone non trouvé")
                return
            vendor.zone_id=id
            vendor_repository=VendorRepository(session)
            vendor=vendor_repository.add(vendor)
            print("Vendeur ajouté")
            print("\t",vendor,sep="")


    def update_vendor(self):
        self.show_vendor()
        while True:
            try:
                id=int(input("Entrez l'id du vendeur à moddifier:"))
                break
            except:
                pass
        with self.session_local() as session:
            vendor_repository=VendorRepository(session)
            vendor = vendor_repository.get_one(id)
        if vendor is None:
            print("Vendeur non trouvé")
        else:
            #si le champs est vide pas de modification
            val=input("Entrez le nouveau nom:")
            if val:
                vendor.vendor_name=val
            self.show_zone()

            while True:
                try:
                    val = input("Entrez l'id de la zone dans laquel se trouve la location:")
                    if val:
                        id_zone=int(val)
                    else:
                        id_zone=None
                    break
                except:
                    pass
            with self.session_local() as session:
                zone_repository=ZoneRepository(session)
                #carefull with NONE
                zone = zone_repository.get_one(id_zone)
                if zone is None:
                    pass
                else:
                    vendor.zone_id=id_zone

            with self.session_local() as session:
                vendor_repository=VendorRepository(session)
                vendor=vendor_repository.update(id,vendor)
                print("Vendeur modifié")
                print("\t",vendor,sep="")

    def delete_vendor(self):
        self.show_vendor()
        while True:
            try:
                id=int(input("Entrez l'id du vendeur à supprimer:"))
                break
            except:
                pass
        with self.session_local() as session:
            vendor_repository=VendorRepository(session)
            vendor = vendor_repository.get_one(id)
            if vendor is None:
                print("Vendeur non trouvé")
            else:
                vendor_repository.delete(vendor)
                print("Vendeur supprimé")

    def show_vendor_catalog(self,id_vendor=None):
        if id_vendor is None:
            self.show_vendor()
            while True:
                try:
                    id_vendor=int(input("Entrez l'id du vendeur:"))
                    break
                except:
                    pass
            with self.session_local() as session:
                vendor_repository=VendorRepository(session)
                vendor = vendor_repository.get_one(id_vendor)
                if vendor is None:
                    print("Vendeur non trouvé")
                    return
        with self.session_local() as session:
            catalog_repository = CatalogRepository(session)
            rows = catalog_repository.get_by_vendor(id_vendor)
            product=None
            for row in rows:
                if product is None or product!= row.product_variant.product_id:
                    product=row.product_variant.product_id
                    print(f"\tid: {row.product_variant.product_id} | name: {row.product_variant.product.product_name}")
                print(f"\t\tid: {row.product_variant.product_variant_id} | size: {row.product_variant.product_variant_size} | color: {row.product_variant.product_variant_color}")

    def update_catalog(self):
        self.show_vendor()
        while True:
            try:
                id_vendor=int(input("Entrez l'id du vendeur:"))
                break
            except:
                pass
        with self.session_local() as session:
            vendor_repository=VendorRepository(session)
            vendor = vendor_repository.get_one(id_vendor)
            if vendor is None:
                print("Vendeur non trouvé")
                return
        while True:
            print("Catalogue du vendeur")
            self.show_vendor_catalog(id_vendor)
            print("Liste des produits")
            self.show_product_variant()
            while True:
                try:
                    id_product=int(input("Entrez l'id du produit a ajouter au catalogue du vendeur:"))
                    break
                except:
                    pass

            with self.session_local() as session:
                product_repository=ProductRepository(session)
                product=product_repository.get_one(id_product)
                if product is None:
                    print("Produit non trouvé")
                    return
                price=None
                for variant in product.product_variants:
                    print("\t",variant,sep="")
                    while True:
                        try:
                            val=input("Entrez le prix de achat du variant:")
                            if not val and price is not None:
                                pass
                            else:
                                price = float(val)
                            break
                        except:
                            pass
                    catalog=Catalog()
                    catalog.vendor_id=id_vendor
                    catalog.product_variant_id=variant.product_variant_id
                    catalog.catalog_selling_price=price
                    with self.session_local() as session:
                        catalog_repository=CatalogRepository(session)
                        existing= catalog_repository.get_one((catalog.product_variant_id,catalog.vendor_id))
                        if existing:
                            catalog_repository.update((catalog.product_variant_id,catalog.vendor_id),catalog)
                        else:
                            catalog_repository.add(catalog)
            choix=-1
            while True:
                print("Continuer à encoder des produits?:")
                print("\t1 - Oui")
                print("\t0 - Non")
                while choix<0 or choix>2:
                    try:
                        choix=int(input("Votre choix:"))
                    except:
                        print("Veillez à entrer un chiffre entre 0 et 1")
                    if choix<0 and choix>6:
                        print("Veillez à entrer un chiffre entre 0 et 1")
                match choix:
                    case 0:return
                    case 1:break       


#endregion