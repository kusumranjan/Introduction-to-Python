USE retail_db;
SELECT o.*,c.customer_name,c.email FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id;
SELECT * FROM orders WHERE customer_id IS NULL;
SELECT o.order_id,o.order_date,o.total_amount,c.city AS customer_city
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id;
SELECT c.customer_id,c.customer_name,COUNT(o.order_id) AS total_orders 
FROM customers c LEFT JOIN orders o
ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name;
SELECT c.customer_id,c.customer_name FROM customers c 
LEFT JOIN orders o ON o.customer_id = c.customer_id 
WHERE o.order_id IS NULL;
SELECT o.order_id,COALESCE(c.customer_name , "Guest Checkout") AS customer_name , o.total_amount
FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id;
SELECT o.* FROM orders o 
LEFT JOIN products p ON o.product_id = p.product_id 
WHERE p.product_id IS NULL;
SELECT o.order_id,o.order_date, o.total_amount,c.customer_name,c.city
FROM orders o LEFT JOIN customers c 
ON o.customer_id = c.customer_id WHERE c.city ="Delhi" OR c.customer_id IS NULL;
SELECT COUNT(*) AS total_orders , 
SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS orders_without_customers
FROM orders;
SELECT (SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END)* 100.0)/
COUNT(*) AS missing_customer_percentage FROM orders;
