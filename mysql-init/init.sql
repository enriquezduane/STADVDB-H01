CREATE DATABASE IF NOT EXISTS salesdb;
CREATE DATABASE IF NOT EXISTS employeesdb;
CREATE DATABASE IF NOT EXISTS datawarehouse;

USE datawarehouse;

CREATE TABLE dim_employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    birth_date DATE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender ENUM('M', 'F'), 
    hire_date DATE
);

CREATE TABLE dim_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sales_code INT, 
    product_number INT,
    date DATE,
    quantity INT
);

CREATE TABLE dim_complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_received DATE,
    product VARCHAR(255),
    sub_product VARCHAR(255),
    issue VARCHAR(255),
    sub_issue VARCHAR(255),
    company VARCHAR(255),
    company_public_response VARCHAR(255)
);

CREATE TABLE fact_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    sales_id INT,
    complaints_id INT,
    FOREIGN KEY (employee_id) REFERENCES dim_employees(employee_id),
    FOREIGN KEY (sales_id) REFERENCES dim_sales(id),
    FOREIGN KEY (complaints_id) REFERENCES dim_complaints(id),
    FOREIGN KEY (id) REFERENCES dim_sales(id)
);


