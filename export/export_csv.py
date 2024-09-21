import mysql.connector
import pandas as pd

# db connection details
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword",
        database="datawarehouse"
)

cursor = db.cursor()

csv_file_path = "data/TEST_Consumer_Complaints.csv"

# read csv into pandas dataframe
df = pd.read_csv(csv_file_path)

# complaints table columns
complaints_data = df[[
    "Date received",
    "Product", 
    "Sub-product", 
    "Issue", 
    "Sub-issue", 
    "Company", 
    "Company public response"
]].drop_duplicates()

# conversion of 'Date received' to datetime objects and formatting
complaints_data['Date received'] = pd.to_datetime(complaints_data['Date received'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

sql = """
INSERT INTO dim_complaints (date_received, product, sub_product, issue, sub_issue, company, company_public_response) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

def handle_nan(value):
  """replace NaN value with NULL"""
  if pd.isnull(value):
    return None  # Or return "Unknown" if you prefer
  return value

# Iterate through the DataFrame and insert data into the table
for index, row in complaints_data.iterrows():
    values = (
        handle_nan(row["Date received"]),
        handle_nan(row["Product"]),
        handle_nan(row["Sub-product"]),
        handle_nan(row["Issue"]),
        handle_nan(row["Sub-issue"]),
        handle_nan(row["Company"]),
        handle_nan(row["Company public response"])
    )
    cursor.execute(sql, values)

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()

print("CSV exported successfully!")
