
-- order_table 
ALTER TABLE  orders_table
ALTER COLUMN date_uuid  TYPE  UUID USING date_uuid::uuid,
	ALTER COLUMN user_uuid  TYPE UUID USING user_uuid::uuid,
	ALTER COLUMN card_number TYPE VARCHAR,
	ALTER COLUMN store_code TYPE VARCHAR,
	ALTER COLUMN product_code    TYPE VARCHAR,
	ALTER COLUMN product_quantity TYPE SMALLINT;

--dim_users

ALTER TABLE  dim_users
ALTER COLUMN first_name  TYPE  VARCHAR(255),
	ALTER COLUMN last_name  TYPE  VARCHAR(255),
	ALTER COLUMN date_of_birth TYPE DATE,
	ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
	ALTER COLUMN country_code    TYPE VARCHAR,
	ALTER COLUMN join_date TYPE DATE;  


--dim_store_details

ALTER TABLE  dim_store_details
ALTER COLUMN longitude TYPE  FLOAT USING longitude::double precision,
	ALTER COLUMN locality  TYPE  VARCHAR(255),
	ALTER COLUMN store_code TYPE VARCHAR,
	ALTER COLUMN staff_numbers TYPE SMALLINT,
	ALTER COLUMN opening_date    TYPE DATE,
	ALTER COLUMN store_type  TYPE VARCHAR(255) ,
	ALTER COLUMN latitude TYPE FLOAT USING latitude::double precision,
	ALTER COLUMN country_code TYPE VARCHAR,
	ALTER COLUMN continent    TYPE VARCHAR;
	
	
--dim_products change product numbers

    ALTER TABLE dim_products ADD COLUMN temp_product_price NUMERIC(10, 2);

UPDATE dim_products
SET temp_product_price = CAST(REPLACE(product_price, '£', '') AS NUMERIC(10, 2));

UPDATE dim_products
SET product_price = temp_product_price;

ALTER TABLE dim_products DROP COLUMN temp_product_price;

-- Step 2: Add the weight_class column
ALTER TABLE dim_products ADD COLUMN weight_class VARCHAR(20);

-- Step 3: Populate the weight_class column
UPDATE dim_products
SET weight_class = CASE
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    WHEN weight >= 140 THEN 'Truck_Required'
END;

dim_products set CAST





--


	ALTER COLUMN weight_class TYPE VARCHAR;

-- removed with EAN


-- ALTER COLUMN still_available TYPE boolean USING
-- 	(CASE 
-- 	WHEN still_available = 'Still_avaliable' THEN true
-- 	WHEN still_available = 'Removed' THEN FALSE
-- 	END) ;

-- change dim products column name
ALTER TABLE dim_products RENAME COLUMN removed TO still_available ;
ALTER TABLE  dim_products
ALTER COLUMN product_price TYPE  FLOAT USING product_price::double precision,
	ALTER COLUMN weight  TYPE  FLOAT,
	ALTER COLUMN product_code TYPE VARCHAR,
	ALTER COLUMN date_added    TYPE DATE,
    ALTER COLUMN "EAN" TYPE VARCHAR,
	ALTER COLUMN uuid TYPE uuid USING uuid::uuid,
    ALTER COLUMN still_available TYPE boolean USING
	(CASE 
	WHEN still_available = 'Still_avaliable' THEN true
	WHEN still_available = 'Removed' THEN FALSE
	) ,
	ALTER COLUMN weight_class TYPE VARCHAR;


    -- dim_dates
    ALTER TABLE  dim_date_times
ALTER COLUMN month TYPE  VARCHAR,
	ALTER COLUMN year  TYPE  VARCHAR,
	ALTER COLUMN day TYPE VARCHAR,
	ALTER COLUMN time_period TYPE VARCHAR,
	ALTER COLUMN date_uuid    TYPE uuid USING date_uuid::uuid;

	--dim_card_details    

        ALTER TABLE  dim_card_details
ALTER COLUMN card_number TYPE VARCHAR,
	ALTER COLUMN expiry_date  TYPE  VARCHAR,
	ALTER COLUMN date_payment_confirmed  TYPE DATE;


ALTER TABLE orders_table
--card details table
ADD CONSTRAINT fk_card_number
FOREIGN KEY (card_number)
REFERENCES dim_card_details (card_number)