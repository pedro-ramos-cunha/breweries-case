
drop table if exists brewery;
drop table if exists brewery_type;
drop table if exists country;
drop table if exists state_province;
drop table if exists city;

CREATE TABLE brewery_type (
	brtp_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	brtp_desc TEXT(30) NOT NULL
);
CREATE UNIQUE INDEX brewery_type_brtp_desc_IDX ON brewery_type (brtp_desc);
commit;

-- Country Table
-- Cant be null, must be unique, and is the primary key.  Will be used as a foreign key in the state_province table.
CREATE TABLE country (
	cntr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	cntr_desc TEXT(200) NOT NULL
);
CREATE UNIQUE INDEX country_cntr_desc_IDX ON country (cntr_desc);
commit;

-- State/Province Table
-- Can be null (in case the brewery is in a country that doesn't have states/provinces), 
-- but if not null, must be unique within the country.  
-- Will be used as a foreign key in the city table.
CREATE TABLE state_province (
	stpr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	stpr_desc TEXT(200) NULL,
    stpr_cntr_seq INTEGER NOT NULL,
    CONSTRAINT state_province_cntr_seq_fk 
        FOREIGN KEY (stpr_cntr_seq) 
        REFERENCES country (cntr_seq)
);
CREATE UNIQUE INDEX state_province_stpr_desc_IDX ON state_province (stpr_cntr_seq,stpr_desc);
commit;

-- City Table
-- Can be null (in case the brewery is in a country that doesn't have city or 
-- location not considered part of a city), but if not null, 
-- must be unique within the state/province with previously checked country.
CREATE TABLE city (
	city_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	city_desc TEXT(200) NULL,
    city_stpr_seq INTEGER NOT NULL,
    CONSTRAINT city_stpr_seq_fk 
        FOREIGN KEY (city_stpr_seq) 
        REFERENCES state_province (stpr_seq)
);
CREATE UNIQUE INDEX city_city_desc_IDX ON city (city_stpr_seq,city_desc);
commit;

-- Address Table
-- Due the lack of standardization in addresses,
-- there is no requirement for the address to be unique.  
-- The address is made up of three lines, but only the first line 
-- is required. The brewery table will have a foreign key to the 
-- address table, but it can be null in case the brewery doesn't 
-- have an address or the address is not known. Also, the integrity 
-- of address related to the city and state/province will be checked
-- in the brewery table, so there is no need to have foreign keys in 
-- the address table to the city and state/province tables.
CREATE TABLE address (
	addr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	addr_line1 TEXT(200) NULL,
    addr_line2 TEXT(200) NULL,
    addr_line3 TEXT(200) NULL,

);
commit;    

CREATE TABLE brewery (
	brwr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	brwr_id TEXT(50) NOT NULL,
	brwr_name TEXT(500) NOT NULL,
    brwr_url TEXT(500) NULL,
    brwr_phone TEXT(50) NULL,
    brwr_brtp_seq INTEGER NOT NULL,
    brwr_addr_seq INTEGER NULL,
    brwr_city_seq INTEGER NULL,
    CONSTRAINT brewery_brtp_seq_fk 
        FOREIGN KEY (brwr_brtp_seq) 
        REFERENCES brewery_type (brtp_seq),
    CONSTRAINT brewery_addr_seq_fk 
        FOREIGN KEY (brwr_addr_seq) 
        REFERENCES address (addr_seq),
    CONSTRAINT brewery_city_seq_fk 
        FOREIGN KEY (brwr_city_seq) 
        REFERENCES city (city_seq)
);
CREATE UNIQUE INDEX brewery_brwr_id_IDX ON brewery (brwr_id);
commit;