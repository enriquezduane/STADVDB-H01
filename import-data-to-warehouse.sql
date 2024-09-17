INSERT INTO datawarehouse.dim_employees (employee_id, birth_date, first_name, last_name, gender, hire_date)
SELECT emp_no, birth_date, first_name, last_name, gender, hire_date
FROM employeesdb.employees;

INSERT INTO datawarehouse.dim_sales (sales_code, product_number, date, quantity)
SELECT `Retailer code`, `Product number`, Date, Quantity
FROM salesdb.sales;

INSERT INTO datawarehouse.fact_table (employee_id, sales_id)
SELECT e.employee_id, s.id
FROM datawarehouse.dim_employees e LEFT JOIN datawarehouse.dim_sales s 
ON e.employee_id = s.id + 10000;