from models import Connection
db = Connection()

class Product:
    """ This class contains methods that allows to do CRUD"""

    def __init__(self, name='', brand='', model='', serial_number=''):
        self.name = name
        self.brand = brand
        self.model = model
        self.serial_number = serial_number

    def get_product_by_id(self, product_id):
        SQL = f"SELECT * FROM product where product_id = '{product_id}' "
        product = db.execute(SQL)

        return product

    def add_product(self):
        SQL = f"""INSERT INTO `flask-api`.`product` (`name`, `brand`, `model`, `serial_number`)
        VALUES ('{self.name}', '{self.brand}', '{self.model}', '{self.serial_number}'); """
        db.execute(SQL)

    @staticmethod
    def display_products():
        SQL = "SELECT * FROM product"
        products = db.execute(SQL)

        return products

    def update_product(self, product_id):
        SQL = f"""
        UPDATE product
        SET name = '{self.name}',
        brand = '{self.brand}',
        model = '{self.model}',
        serial_number = '{self.serial_number}'
        WHERE product_id = '{product_id}'
        """
        db.execute(SQL)

        return True

    def delete_product(self, product_id):
        SQL = f"DELETE FROM product where product_id = '{product_id}' "
        db.execute(SQL)

        return True
