-- The sales team is looking to expand their territory in Germany. Determine which type of store is generating the most sales in Germany.

SELECT 
    ROUND(SUM(ord.product_quantity * prod.product_price)::numeric, 2) AS total_sales,
    store.store_type AS store_type,
    store.country_code AS country_code
FROM orders_table ord
JOIN dim_store_details store ON store.store_code = ord.store_code
JOIN dim_products prod ON ord.product_code = prod.product_code
WHERE store.country_code = 'DE'
GROUP BY store.store_type, store.country_code
ORDER BY total_sales;
