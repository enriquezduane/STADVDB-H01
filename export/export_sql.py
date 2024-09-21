import sqlalchemy
import pandas as pd
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import OperationalError

employee_local_engine = sqlalchemy.create_engine(
    URL.create(
        "mysql+mysqlconnector",
        username="root",
        password="rootpassword",
        host="localhost",
        port=3306,
        database="employeesdb",
        query={"connect_timeout": "10"}
    )
)

sales_local_engine = sqlalchemy.create_engine(
    URL.create(
        "mysql+mysqlconnector",
        username="root",
        password="rootpassword",
        host="localhost",
        port=3306,
        database="salesdb",
        query={"connect_timeout": "10"}
    )
)

employee_cloud_engine = sqlalchemy.create_engine(
    URL.create(
        "mysql+mysqlconnector",
        username="guest",
        password="relational",
        host="db.relational-data.org",
        port=3306,
        database="employee",
        query={"connect_timeout": "10"}
    )
)

sales_cloud_engine = sqlalchemy.create_engine(
    URL.create(
        "mysql+mysqlconnector",
        username="guest",
        password="relational",
        host="db.relational-data.org",
        port=3306,
        database="GOSales",
        query={"connect_timeout": "10"}
    )
)

def test_connection(engine, name):
    try:
        with engine.connect() as conn:
            print(f"Successfully connected to {name} database")
    except Exception as e:
        print(f"Failed to connect to {name} database: {str(e)}")

print("Testing database connections...")
test_connection(employee_cloud_engine, "cloud employee")
test_connection(employee_local_engine, "local employee")
test_connection(sales_local_engine, "local sales")

print("Testing cloud employee database connection...")
try:
    with employee_cloud_engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT COUNT(*) FROM employees")).fetchone()
        print(f"Connected successfully. Employee count: {result[0]}")
except Exception as e:
    print(f"Failed to connect to cloud employee database: {str(e)}")


print("Starting employee data transfer...")
try:
    df = pd.read_sql_query("SELECT * FROM employees", employee_cloud_engine)
    print(f"Fetched {len(df)} rows")
    df.to_sql("employees", employee_local_engine, if_exists="append", index=False)
    print("Employee data transfer complete")
except OperationalError as e:
    print(f"Query timed out or failed: {str(e)}")
except Exception as e:
    print(f"Error during employee data transfer: {str(e)}")

print("Starting sales data transfer...")
try:
    df = pd.read_sql_query("SELECT * FROM go_1k", sales_cloud_engine)
    print(f"Fetched {len(df)} rows")
    df.to_sql("sales", sales_local_engine, if_exists="append", index=False)
    print("Sales data transfer complete")
except OperationalError as e:
    print(f"Query timed out or failed: {str(e)}")
except Exception as e:
    print(f"Error during employee data transfer: {str(e)}")

print("Data Transferred Successfully")
