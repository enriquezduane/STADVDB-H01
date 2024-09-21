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

CREATE TABLE dim_supplies_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL UNIQUE,
    sale_date DATETIME,
    store_location VARCHAR(100),
    customer_gender CHAR(1),
    customer_age INT,
    customer_email VARCHAR(255),
    customer_satisfaction INT,
    coupon_used BOOLEAN,
    purchase_method VARCHAR(50)
);

CREATE TABLE dim_supplies_order_items (
    item_key INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(50),
    name VARCHAR(100),
    price DECIMAL(10, 2),
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES dim_supplies_orders(order_id)
);

CREATE TABLE dim_supplies_order_item_tags (
    item_tag_key INT AUTO_INCREMENT PRIMARY KEY,
    item_key INT,
    tagname VARCHAR(50),
    FOREIGN KEY(item_key) REFERENCES dim_supplies_order_items(item_key)
);

CREATE TABLE fact_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    sales_id INT,
    complaints_id INT,
    orders_id INT,
    order_items_id INT,
    tags_id INT,
    FOREIGN KEY (employee_id) REFERENCES dim_employees(employee_id),
    FOREIGN KEY (sales_id) REFERENCES dim_sales(id),
    FOREIGN KEY (complaints_id) REFERENCES dim_complaints(id),
    FOREIGN KEY (orders_id) REFERENCES dim_supplies_orders(id),
    FOREIGN KEY (order_items_id) REFERENCES dim_supplies_order_items(item_key),
    FOREIGN KEY (tags_id) REFERENCES dim_supplies_order_item_tags(item_tag_key)
);
