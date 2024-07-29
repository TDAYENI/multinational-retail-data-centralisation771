-- The company stakeholders want assurances that the company has been doing well recently.
-- Find which months in which years have had the most sales historically.
-- Main query to calculate total sales, grouped by year and month, and ordered by total sales

SELECT 
    ROUND(SUM(ord.product_quantity * prod.product_price)::numeric, 2) AS total_sales,  -- Calculate total sales for each year and month
    date_dim.year, 
    date_dim.month
FROM 
    orders_table ord
JOIN 
    dim_products prod 
ON ord.product_code = prod.product_code
JOIN 
    dim_date_times date_dim 
ON  ord.date_uuid = date_dim.date_uuid
GROUP BY 
    date_dim.year, date_dim.month  -- Group by year and month
ORDER BY  total_sales DESC  
LIMIT 10; 
