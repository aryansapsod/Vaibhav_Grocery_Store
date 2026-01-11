from multiprocessing import connection
from urllib import response
from flask import Flask, app, request, jsonify
from products_dao import get_all_products
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['POST', 'GET'])
def get_products():
    # connection = get_sql_connection()
    products = get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProducts', methods=['POST', 'GET'])
def delete_products():
    return_id = delete_products(connection, request.form('product_id'))
    # connection = get_sql_connection()
    products = get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

    

if __name__ == '__main__':
    print("Starting Python Flask Server For Grocery Store")
    app.run(port=5000)

