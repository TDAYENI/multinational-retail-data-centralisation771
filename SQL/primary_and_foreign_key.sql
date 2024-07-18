-- Adding Primary Key
ALTER TABLE dim_users ADD PRIMARY KEY (user_uuid);
ALTER TABLE dim_card_details ADD PRIMARY KEY (card_number);
ALTER TABLE dim_date_times ADD PRIMARY KEY (date_uuid);
ALTER TABLE dim_products ADD PRIMARY KEY (uuid);
ALTER TABLE dim_store_details ADD PRIMARY KEY (store_code);

--foreign keys in the orders_table to reference the primary keys in the other tables
SELECT DISTINCT(ord.card_number)
FROM orders_table ord
WHERE NOT EXISTS 
	(SELECT * FROM dim_card_details prod
	WHERE prod.card_number = ord.card_number);

-- identify dim_users rows with issue 50
SELECT user_uuid
FROM orders_table
WHERE user_uuid NOT IN (SELECT user_uuid FROM dim_users);

-- identify uuid in orders tbael but not dim_users
SELECT DISTINCT(ord.user_uuid)
FROM orders_table ord
WHERE NOT EXISTS 
	(SELECT * FROM dim_users prod
	WHERE prod.user_uuid = ord.user_uuid)


ALTER TABLE orders_table
ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);
 ---dim_card_details
 --identify dim_card_details rows with issue 57 
 SELECT user_uuid
FROM orders_table
WHERE card_number NOT IN (SELECT card_number FROM dim_card_details);

ALTER TABLE orders_table
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);
--RROR:  Key (card_number)=(4266601318666440) is not present in table "dim_card_details".insert or update on table "orders_table" violates foreign key constraint "orders_table_card_number_fkey" 


-- --"card_number"
-- "4416459602615430"    12564	4416459602615430	08/32	VISA 16 digit	2017/05/15
-- "3560053307745130"   12282	3560053307745130	05/27	JCB 16 digit	September 2016 04
-- "349418762090789"   11334	349418762090789	06/24	American Express	October 2000 04
-- "342678097599435"    7221	342678097599435	02/28	American Express	2008 May 11
-- "4534746397893770" 6667	4534746397893770	01/30	VISA 16 digit	December 2000 01
-- "4266601318666440" 1448	4266601318666440	12/30	VISA 16 digit	December 2021 17
-- "213163034758051" 2376	213163034758051	03/23	JCB 15 digit	2005 July 01
-- "4560485762943720000"    14978	4560485762943720000	04/29	VISA 19 digit	May 1998 09

-- works
ALTER TABLE orders_table
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);

--dim_products 
--identify dim_products rows with issue 187 
SELECT user_uuid
FROM orders_table
WHERE product_code NOT IN (SELECT product_code FROM dim_products);

ALTER TABLE orders_table
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);

--dim_store_details
--identify dim_store_details rows with issue 187 
SELECT store_code
FROM orders_table
WHERE store_code NOT IN (SELECT store_code FROM dim_store_details);

ALTER TABLE orders_table
ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);
