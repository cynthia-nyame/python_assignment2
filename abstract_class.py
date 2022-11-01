from abc import ABC,abstractmethod
class Product:
    product_name='Samsung'
    product_type='A50'
    product_cost='Ghc1,200.00'
    product_id=22
    product_image=''
    delete_product=''


class Productabstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product_id):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_all_product(self):
        pass

    @abstractmethod
    def upload_product_image(self, product_id, image):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass

class ProductManager(Productabstract):
    def create_product(self, product: Product):
        print(f"{product.product_name}")

    def edit_product(self):
         print("Edit product here")

    def get_product_by_id(self,product_id):
         print(f"{product_id}")

    def get_all_product(self):
         print("List all products")
   
    def upload_product_image(self):
         print("Upload Image here")

    def delete_product(self):
         print("Delete product")

prod=ProductManager()
prod.edit_product()
prod.get_product_by_id(22)
prod.get_all_product()
prod.upload_product_image()
prod.delete_product()
prod.create_product(Product())

