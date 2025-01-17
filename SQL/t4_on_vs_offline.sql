-- <!-- The company is looking to increase its online sales.
-- They want to know how many sales are happening online vs offline.
-- Calculate how many products were sold and the amount of sales made for online and offline purchases. --


--CTE,COUNT no/sum,online sales, join orders group by storetype
WITH OnlineData AS (
    SELECT 
        COUNT(*) AS number_of_sales, --total orders online
        SUM(o.product_quantity) AS total_product_quantity, 
        'Web' AS location
    FROM  orders_table o
        JOIN dim_store_details dsd ON dsd.store_code = o.store_code -- joins to get store detail
    WHERE 
        dsd.store_type = 'Web Portal'
    GROUP BY dsd.store_type
), 
--offline CTE, count num off line sale /sum prod quant
OfflineData AS (
    SELECT COUNT(*) AS number_of_sales, SUM(o.product_quantity) AS total_product_quantity, 
        'Offline' AS location --
    FROM 
        orders_table o -- join store details
        JOIN dim_store_details dsd ON dsd.store_code = o.store_code
    WHERE 
        dsd.store_type != 'Web Portal'
    GROUP BY 
        dsd.store_type
) -- Main qeury
SELECT SUM(number_of_sales) AS total_sales,  
    SUM(total_product_quantity) AS total_product_quantity, 
    location
FROM  OnlineData
GROUP BY 
    location

UNION
-- agg of offline results
SELECT SUM(number_of_sales) AS total_sales,
    SUM(total_product_quantity) AS total_product_quantity, 
    location
FROM  OfflineData
GROUP BY 
    location;
