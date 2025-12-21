###################################
List all orders with customer names and email.
select c.customer_name, c.email,o.order_id
FROM customers c
inner join orders o
on c.customer_id =o.customer_id;
 ###################################  
Show product name, category, price for every ordered product.
select p.product_name,p.category,p.price,o.order_id
from products p
inner join orders o
on p.product_id = o.product_id
###################################   
List all orders with customer name and product name.
SELECT
    o.order_id,
    c.customer_name,
    p.product_name
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id
INNER JOIN products p
    ON o.product_id = p.product_id
###################################   
Show customer name and total_amount for all valid customer orders.
SELECT
    o.order_id,
    o.total_amount,
    c.customer_name
FROM orders o
INNER JOIN customers 
    ON o.customer_id = c.customer_id
###################################   
 . List all Electronics products that have been ordered.
SELECT
    p.product_name,
    o.order_id,
    o.order_date
FROM orders o
INNER JOIN products p
    ON o.product_id = p.product_id
 ###################################  
Find customers who ordered Fashion products.

SELECT
    c.customer_name,
    p.product_name
FROM customers c
INNER JOIN orders o
    ON o.customer_id = c.customer_id
INNER JOIN products p
    ON o.product_id = p.product_id


###################################   
Show all orders above 1000 with customer and product details.
select c.customer_name,
c.city,
c.email,
c.customer_id,
p.product_id,
p.product_name,
p.category,
p.price

from customers c
inner join orders o
on o.customer_id=c.customer_id
inner join products p
on p.product_id=o.product_id
where p.price >= 1000
################################
Show customers from Mumbai who placed at least one order.
select c.customer_name,
c.city,
o.order_id
from customers c
inner join orders o
on o.customer_id = c.customer_id
where c.city='Mumbai'
 ###################################333  
Show number of orders per customer (using INNER JOIN + GROUP BY).
select c.customer_name,
count(o.order_id)as tot
from customers c
inner join orders o
on o.customer_id =c.customer_id
group by c.customer_name
   
List all customers and the total amount they have spent
SELECT
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
INNER JOIN orders o
    ON o.customer_id = c.customer_id
GROUP BY c.customer_name;
