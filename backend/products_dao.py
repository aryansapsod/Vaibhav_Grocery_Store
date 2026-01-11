
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
if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_products(connection))


