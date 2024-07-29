-- Query the database to find out which months have produced the most sales.
--verify join

-- Product quant,prive and month from orders as well as dim dates and products
SELECT ord.product_quantity, prod.product_price, ddt.month
FROM orders_table ord
JOIN dim_products prod ON ord.product_code = prod.product_code --join with orders table on product
JOIN dim_date_times ddt ON ord.date_uuid = ddt.date_uuid -- JOIN THe table on order uuid
LIMIT 10;
