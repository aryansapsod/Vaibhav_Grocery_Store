
from sql_connection  import get_sql_connection 
import mysql.connector 

def get_all_products(connection):
   
    cursor = connection.cursor()
    query = "SELECT products.product_id, products.product_name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id = uom.uom_id"
    cursor.execute(query)
    responds = []
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        responds.append({
            "product_id": product_id,
            "product_name": product_name,
            "uom_id": uom_id,
            "price_per_unit": float(price_per_unit),
            "uom_name": uom_name
        })
    
    return responds

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = "INSERT INTO products( product_id, product_name, uom_id, price_per_unit) VALUES (%s, %s, %s, %s)"
    data = (product["product_id"],  product["product_name"], product["uom_id"], product["price_per_unit"])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_products(connection))
    print(insert_new_product(connection, {
        "product_id": 10,
        "product_name": "Onion",
        "uom_id": 2,
        "price_per_unit": 20
    }))
