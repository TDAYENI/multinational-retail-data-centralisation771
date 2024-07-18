-- Adding Primary Key
ALTER TABLE dim_users ADD PRIMARY KEY (user_uuid);
ALTER TABLE dim_card_details ADD PRIMARY KEY (card_number);
ALTER TABLE dim_date_times ADD PRIMARY KEY (date_uuid);
ALTER TABLE dim_products ADD PRIMARY KEY (uuid);
ALTER TABLE dim_store_details ADD PRIMARY KEY (store_code);



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

--works
ALTER TABLE orders_table
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);




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
