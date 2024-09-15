CREATE DATABASE IF NOT EXISTS salesdb;
CREATE DATABASE IF NOT EXISTS employeesdb;
CREATE DATABASE IF NOT EXISTS datawarehouse;

USE datawarehouse;

CREATE TABLE dim_employees (
    employee_id INT PRIMARY KEY,
    birth_date DATE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender ENUM('M', 'F'), 
    hire_date DATE
);

CREATE TABLE dim_sales (
    sales_id INT PRIMARY KEY,
    product_number INT,
    date DATE,
    quantity INT
);

CREATE TABLE fact_table (
    id INT PRIMARY KEY,
    employee_id INT,
    sales_id INT,
    FOREIGN KEY (employee_id) REFERENCES dim_employees(employee_id),
    FOREIGN KEY (sales_id) REFERENCES dim_sales(sales_id)
);
