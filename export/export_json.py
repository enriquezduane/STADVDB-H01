from pymongo import MongoClient
import pymysql
import json
import datetime

client = MongoClient('mongodb://localhost:27017/')

mongodb_conn = client['main']
collection = mongodb_conn['supplies']

db = pymysql.connect(
        host="localhost",
        user="root",
        password="rootpassword",
        database="datawarehouse"
)

cursor = db.cursor()

data = list(collection.find())

for order in data:
    id = str(order['_id'])
    sale_date = order['saleDate']

    store_location = order['storeLocation']
    customer_gender = order['customer']['gender']
    customer_age = order['customer']['age']
    customer_email = order['customer']['email']
    customer_satisfaction = order['customer']['satisfaction']
    coupon_used = order['couponUsed']
    purchase_method = order['purchaseMethod']

    cursor.execute("""
    INSERT INTO dim_supplies_orders (id, sale_date, store_location, customer_gender, customer_age, customer_email, customer_satisfaction, coupon_used, purchase_method)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (id, sale_date, store_location, customer_gender, customer_age, customer_email, customer_satisfaction, coupon_used, purchase_method))

    for item in order['items']:
        item_name = item['name']
        item_price = item['price']
        item_quantity = item['quantity']

        cursor.execute("""
        INSERT INTO dim_supplies_order_items (order_id, name, price, quantity)
        VALUES (%s, %s, %s, %s)
        """, (id, item_name, item_price, item_quantity))

        item_key = cursor.lastrowid
        for tag in item['tags']:
            tag_name = tag

            cursor.execute("""
            INSERT INTO dim_supplies_order_item_tags (item_key, tagname)
            VALUES (%s, %s)
                           """, (item_key, tag_name))


print("Data load successful.")
db.commit()
cursor.close()
db.close()

