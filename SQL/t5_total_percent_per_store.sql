-- The sales team wants to know which of the different store types is generated the most revenue so they know where to focus.
-- Find out the total and percentage of sales coming from each of the different store types.
-- The query should return:

-- Common Table Expression (CTE) to calculate the total sales sum
WITH TotalSales AS (
    SELECT 
        SUM(o.product_quantity * p.product_price) AS total_sum  -- Calculate the total sum of sales
    FROM
        orders_table o
    JOIN 
        dim_products dp 
    ON 
        o.product_code = dp.product_code
)

-- Main query to calculate total sales and percentage of total sales by store type
SELECT 
    dsd.store_type AS store_type, 
    ROUND(SUM(o.product_quantity * dp.product_price)::numeric, 2) AS total_sales,  -- Calculate total sales for each store type
    ROUND((SUM(o.product_quantity * dp.product_price) / ts.total_sum * 100)::numeric, 2) AS "percentage_total (%)"  -- Calculate percentage of total sales
FROM 
    orders_table o
JOIN
    dim_store_details dsd 
ON 
    dsd.store_code = o.store_code
JOIN 
    dim_products dp 
ON 
    o.product_code = dp.product_code
CROSS JOIN 
    TotalSales ts  -- Include the total sales sum in the calculation
GROUP BY 
    dsd.store_type, ts.total_sum  -- Group by store type and total sales sum
ORDER BY 
    total_sales DESC;  -- Order the results by total sales in descending order
