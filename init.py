import sqlalchemy
import mysql.connector
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
    
# db connection details
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword"
)

cursor = db.cursor()

csv_file_path = ""

# read csv into pandas dataframe
df = pd.read_csv(csv_file_path)

# complaints table columns
complaints_data = df[[
    "Product", 
    "Sub-product", 
    "Issue", 
    "Sub-issue", 
    "Company", 
    "Company public response"
]].drop_duplicates()

sql = """
INSERT INTO dim_complaints (product, sub_product, issue, sub_issue, company, company_public_response) 
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Iterate through the DataFrame and insert data into the table
for index, row in complaints_data.iterrows():
    values = (
        row["Product"], 
        row["Sub-product"], 
        row["Issue"], 
        row["Sub-issue"], 
        row["Company"], 
        row["Company public response"]
    )
    cursor.execute(sql, values)

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()

print("Data copied successfully!")

