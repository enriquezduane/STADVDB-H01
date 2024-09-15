import mysql.connector

try:
    # establish conn
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword"
    )

    # cursor
    cursor = db.cursor()

    # select all from the 'datawarehouse' database and 'Customers' table
    cursor.execute("SELECT * FROM datawarehouse.Customers")

    result = cursor.fetchall()

    # print contents
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if db.is_connected():
        cursor.close()
        db.close()
