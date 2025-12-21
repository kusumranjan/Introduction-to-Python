1. CREATE DATABASE
 CREATE DATABASE retail_db; 
USE retail_db; 
2. CREATE TABLES
 A. Customers Table
 (Some customers have no orders → used for RIGHT JOIN and OUTER JOIN.)
 CREATE TABLE customers ( 
    customer_id INT PRIMARY KEY, 
    customer_name VARCHAR(50), 
    email VARCHAR(80), 
    city VARCHAR(50)
 ); 
B. Orders Table
 (Some orders have NULL product_id or NULL customer_id to demonstrate LEFT JOIN.)
 CREATE TABLE orders ( 
    order_id INT PRIMARY KEY, 
    order_date DATE, 
    customer_id INT NULL, 
    total_amount DECIMAL(10,2), 
    product_id INT NULL 
); 
C. Products Table
(Some products have never been ordered → used for RIGHT JOIN.)
 CREATE TABLE products ( 
    product_id INT PRIMARY KEY, 
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2) 
); 
3. INSERT DATA
 Customers
 INSERT INTO customers VALUES 
(1, 'Aisha Khan', 'aisha@xyz.com', 'Mumbai'), 
(2, 'Rahul Sharma', 'rahul@xyz.com', 'Delhi'), 
(3, 'John Daniel', 'john@xyz.com', 'Bangalore'), 
(4, 'Meera Iyer', 'meera@xyz.com', 'Chennai'), 
(5, 'Sanjay Patel', 'sanjay@xyz.com', 'Hyderabad'); 
Customer 5 will have no orders.
 Products
 INSERT INTO products VALUES 
(101, 'Laptop HP 15', 'Electronics', 52000), 
(102, 'Samsung Phone A54', 'Electronics', 28000), 
(103, 'Jeans Blue Fit', 'Fashion', 1500), 
(104, 'T-Shirt Classic', 'Fashion', 700), 
(105, 'Wireless Mouse', 'Accessories', 900), 
(106, 'Rice 5KG Bag', 'Groceries', 320), 
(107, 'Olive Oil 1L', 'Groceries', 540), 
(108, 'Printer Canon G2012', 'Electronics', 12500); 
Products 107 and 108 have zero orders.
Orders
 INSERT INTO orders VALUES 
(1001, '2024-01-05', 1, 52000, 101), 
(1002, '2024-01-06', 2, 28000, 102), 
(1003, '2024-01-07', 3, 1500, 103), 
(1004, '2024-01-07', 1, 700, 104), 
(1005, '2024-01-08', 2, 900, 105), 
(1006, '2024-01-08', NULL, 320, 106),    
(1007, '2024-01-09', 1, 540, NULL),     -- customer unknown -- product unknown 
(1008, '2024-01-10', 3, 12500, 108), 
(1009, '2024-01-10', 4, 320, 106), 
(1010, '2024-01-11', NULL, 700, 104),   -- customer null 
(1011, '2024-01-12', 2, 540, 107);      -- product exists but never orde
