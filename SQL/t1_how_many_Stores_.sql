-- The Operations team would like to know which countries we currently operate in and which country now has the most stores. Perform a query on the database to get the information, it should return the following information:

--counts the number of stores in each country 
SELECT country_code, COUNT(*) FROM dim_store_details 
GROUP BY country_code
-- returns the top 3 countries highest store
ORDER BY COUNT(*) DESC
LIMIT 3;