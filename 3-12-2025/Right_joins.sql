Show all products and the orders associated with them (NULL for unused products).
SELECT 
    p.product_id,
    p.product_name,
    o.order_id,
    o.order_date
FROM 
    products p
LEFT JOIN orders o
on o.product_id=p.product_id
order by p.product_id
###################################################   
List products that have never been ordered.
select p.product_name,o.order_id
from products p
left join orders o
on p.product_id=o.product_id
where o.order_id is null;
###################################################    
Show Electronics products and the number of times they were ordered.
SELECT 
    p.product_name,
    COUNT(o.order_id) AS tot
FROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.product_id
WHERE 
    p.category = 'Electronics'
GROUP BY 
    p.product_name

###################################################   
Show Groceries products and their rst order date.

SELECT 
    p.product_name,
    MIN(o.order_date) AS first_order_date
FROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.product_id
WHEREWHERE 
    p.category = 'Groceries'
GROUP BY 
    p.product_name

###################################################    
List all products with their total sales, including those with zero sales.

SELECT 
    p.product_name,
    COALESCE(SUM(od.quantity * od.unit_price), 0) AS total_sales
FROM 
    products p
LEFT JOIN 
    order_details od ON p.product_id = od.product_id
GROUP BY 
    p.product_name


###################################################    
For each category, show number of ordered products (include zero).

SELECT 
    p.category,
    COUNT(o.order_id) AS ordered_products
FROMFROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.product_id

###################################################   
Show products that were ordered by customers from Bangalore.

SELECT 
    p.product_name,
    c.customer_name,
    c.city
FROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.product_id
LEFT JOIN 
    customers c ON o.customer_id = c.customer_id
WHERE 
    c.city = 'Bangalore'

###################################################  
Show products missing from order table (never sold).

SELECT 
    p.product_name
FROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.produ

 ###################################################   
Show the count of orders grouped by product name (including zero).

SELECT 
    p.product_name,
    COUNT(o.order_id) AS order_count
FROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.product_id

 ###################################################   
Show products that appeared in at least one NULL customer order.
SELECT DISTINCT
    p.product_name
FROM 
    products p
LEFT JOIN 
    orders o ON p.product_id = o.product_id
LEFT JOIN 
    customers c ON o.customer_id = c.customer_id
WHERE 
    c.customer_id IS NULL AND o.order_id IS NOT NULL;
