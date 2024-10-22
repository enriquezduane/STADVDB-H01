import mysql.connector

# db connection details
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword",
        database="datawarehouse"
)

cursor = db.cursor()

try:
    # SQL statements to be executed sequentially
    sql_statements = [
        """
        INSERT INTO datawarehouse.dim_employees (employee_id, birth_date, first_name, last_name, gender, hire_date)
        SELECT emp_no, birth_date, first_name, last_name, gender, hire_date
        FROM employeesdb.employees;
        """,
        """
        INSERT INTO datawarehouse.dim_sales (sales_code, product_number, date, quantity)
        SELECT `Retailer code`, `Product number`, Date, Quantity
        FROM salesdb.sales;
        """,
        """
        INSERT INTO datawarehouse.fact_table (employee_id, sales_id)
        SELECT e.employee_id, s.id
        FROM datawarehouse.dim_employees e LEFT JOIN datawarehouse.dim_sales s 
        ON e.employee_id = s.id + 10000;
        """,
        """
        UPDATE datawarehouse.fact_table f
        JOIN datawarehouse.dim_complaints c
        SET f.complaints_id = c.id
        WHERE f.id = c.id;
        """,
        """
        UPDATE datawarehouse.fact_table f
        JOIN datawarehouse.dim_supplies_order_item_tags t
        SET f.tags_id = t.item_tag_key
        WHERE f.id = t.item_tag_key;
        """,
        """
        UPDATE datawarehouse.fact_table f
        JOIN datawarehouse.dim_supplies_order_items i
        SET f.order_items_id = i.item_key
        WHERE f.id = i.item_key;
        """,
        """
        UPDATE datawarehouse.fact_table f
        JOIN datawarehouse.dim_supplies_orders o
        SET f.orders_id = o.id
        WHERE f.id = o.id;
        """
    ]

    # Execute each SQL statement one by one
    for statement in sql_statements:
        cursor.execute(statement)
        db.commit() 

    print("SQL statements executed successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    db.rollback() # Rollback changes if an error occurs

finally:
    # Close the cursor and database connection
    cursor.close()
    db.close() 
