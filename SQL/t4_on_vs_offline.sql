-- <!-- The company is looking to increase its online sales.
-- They want to know how many sales are happening online vs offline.
-- Calculate how many products were sold and the amount of sales made for online and offline purchases. --

























SELECT 
    COUNT(*) AS number_of_sales, 
    SUM(o.product_quantity) AS total_product_quantity, 
    'Web' AS location
FROM 
    orders_table o
    JOIN dim_store_details dsd ON dsd.store_code = o.store_code
WHERE 
    dsd.store_type = 'Web Portal'
GROUP BY 
    dsd.store_type;
