import sqlalchemy
import pandas as pd

employee_local_engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:rootpassword@localhost:3306/employeesdb")
sales_local_engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:rootpassword@localhost:3306/salesdb")

employee_cloud_engine = sqlalchemy.create_engine("mysql+mysqlconnector://guest:relational@db.relational-data.org:3306/employee")
sales_cloud_engine = sqlalchemy.create_engine("mysql+mysqlconnector://guest:relational@db.relational-data.org:3306/GOSales")

chunksize = 10000  # Adjust chunksize as needed

for chunk in pd.read_sql_query("SELECT * FROM employees", employee_cloud_engine, chunksize=chunksize):
    chunk.to_sql("employees", employee_local_engine, if_exists="append", index=False)

for chunk in pd.read_sql_query("SELECT * FROM go_1k", sales_cloud_engine, chunksize=chunksize):
    chunk.to_sql("sales", sales_local_engine, if_exists="append", index=False)

