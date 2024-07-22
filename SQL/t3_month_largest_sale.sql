-- Query the database to find out which months have produced the most sales.
--verify join
SELECT ord.product_quantity, prod.product_price, ddt.month
FROM orders_table ord
JOIN dim_products prod ON ord.product_code = prod.product_code
JOIN dim_date_times ddt ON ord.date_uuid = ddt.date_uuid
LIMIT 10;
