-- Adding Primary Key
ALTER TABLE dim_users ADD PRIMARY KEY (user_uuid);
ALTER TABLE dim_card_details ADD PRIMARY KEY (card_number);
ALTER TABLE dim_date_times ADD PRIMARY KEY (date_uuid);
ALTER TABLE dim_products ADD PRIMARY KEY (product_code);
ALTER TABLE dim_store_details ADD PRIMARY KEY (store_code);

--FK user_uuid
ALTER TABLE orders_table
ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);
--FK dim card details
ALTER TABLE orders_table
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);
--fk dim_dates
ALTER TABLE orders_table
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);

--fk dim_products 

ALTER TABLE orders_table
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);

--dim_store_details

ALTER TABLE orders_table
ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);
