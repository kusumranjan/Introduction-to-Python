##########################################################
Show all orders, even those without customer info.

SELECT
    o.order_id,
    o.total_amount,
    c.customer_name,
    c.city,
    c.email
FROM orders o
LEFT JOIN customers c

########################################################## 
Find all orders where customer_id is NULL.

SELECT
    o.order_id,
    o.total_amount
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

##########################################################   
Display orders with customer city (NULL when customer is missing).
SELECT o.order_date, o.order_id,o.total_amount,c.city
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
##########################################################  
Show all customer names and the number of orders they placed (include zero).

SELECT
    c.customer_name,
    COUNT(o.order_id) AS counttot
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

########################################################## 
Show customers who have not placed ANY order.
SELECT
    c.customer_name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
##########################################################
Show all orders and label missing customers as “Guest Checkout”.

SELECT
    o.order_id,
    o.order_date,
    o.total_amount,
    COALESCE(c.customer_name, 'Guest Checkout') AS customer_name #coalesce replaces the strings
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id;

########################################################## 
Show orders that have missing product details.

SELECT
    o.order_id,
    o.order_date,
    o.total_amount
FROM orders o
LEFT JOIN products p
    ON o.product_id = p.product_id
WHERE p.product_id IS NULL;

##########################################################  
Show orders placed by customers from Delhi or missing customer info.
select o.order_id, c.city,c.customer_name
from orders o
left join customers c
on c.customer_id=o.customer_id
where c.city='Delhi' or c.city='NULL'
  
##########################################################  
Count total orders including ones without customer linkage.

SELECT
    COUNT(o.order_id) AS total_orders
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id;

 ########################################################## 
Show the percentage of orders with missing customers.
  
SELECT
    (COUNT(CASE WHEN c.customer_id IS NULL THEN 1 END) * 100.0 / COUNT(*)) AS missing_customer_percentage
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id;
