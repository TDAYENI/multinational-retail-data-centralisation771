-- The operations team would like to know the overall staff numbers in each location around the world. Perform a query to determine the staff numbers in each of the countries the company sells in.
-- Main query to calculate the total staff numbers, grouped by country code, and ordered by total staff numbers
SELECT 
    SUM(dsd.staff_numbers) AS total_staff_numbers,  -- Calculate the total staff numbers for each country
    dsd.country_code
FROM 
    dim_store_details dsd
GROUP BY 
    dsd.country_code  -- Group by country code
ORDER BY 
    total_staff_numbers DESC  -- Order the results by total staff numbers in descending order
LIMIT 6;  -- Limit the results to the top 6


