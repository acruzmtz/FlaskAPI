from flask import Flask,jsonify, request
from products import Product
product = Product()

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def getProducts():
    """ show all stored products """

    products = Product.display_products()

    return jsonify({"products": products})


@app.route('/select/<int:product_id>')
def getProductById(product_id):
    """ search for product in the database using product_id """

    productFound = product.get_product_by_id(product_id)
    if not productFound:
        return jsonify({"message": "Product not found"})

    return jsonify({"product": productFound})


@app.route('/product', methods=['POST'])
def addProduct():
    """ get the json object with attributes name, brand, model and series """

    if request.method == "POST":
        name = request.json['name']
        brand = request.json['brand']
        model = request.json['model']
        serial_number = request.json['serial']

        newProduct = Product(name, brand, model, serial_number)
        newProduct.add_product()

        products = Product.display_products()

    return jsonify({"products": products})


@app.route('/update', methods=['PUT'])
def updateProduct():
    pass


@app.route('/delete', methods=['DELETE'])
def deleteProduct():
    pass


if __name__ == '__main__':
    app.run(debug=True)
