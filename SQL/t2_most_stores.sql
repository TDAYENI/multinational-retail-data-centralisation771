-- The business stakeholders would like to know which locations currently have the most stores.
-- They would like to close some stores before opening more in other locations.
--  Find out which locations have the most stores currently

--count no of stores in each locality
SELECT locality, COUNT(*) FROM dim_store_details 
GROUP BY locality
-- return top 7 localites
ORDER BY COUNT(*) DESC
LIMIT 7;