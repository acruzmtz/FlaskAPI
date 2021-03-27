from flask import Flask,jsonify, request
from products import Product
product = Product()

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def getProducts():
    """ show all stored products """

    products = Product.display_products()

    return jsonify({"products": products})


@app.route('/select/<int:product_id>', methods=['GET'])
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

    return jsonify({
        "message": "Product added successfully",
        "products": products
    })


@app.route('/update/<int:product_id>', methods=['PUT'])
def updateProduct(product_id):
    upgradedProduct = product.get_product_by_id(product_id)
    if not upgradedProduct:
        return jsonify({"message": "Product not found"})

    name = request.json['name']
    brand = request.json['brand']
    model = request.json['model']
    serial = request.json['serial']

    update_product = Product(name, brand, model, serial)
    update_product.update_product(product_id)

    return jsonify(
        {"message": "Product updated successfully",
        "product_updated": upgradedProduct
        }
    )


@app.route('/delete/<int:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    select_product = product.get_product_by_id(product_id)
    if not select_product:
        return jsonify({"message": "Product not found"})

    product.delete_product(product_id)

    return jsonify({
        "message": "Product deleted successfully",
        "product": select_product
    })


if __name__ == '__main__':
    app.run(debug=True)
