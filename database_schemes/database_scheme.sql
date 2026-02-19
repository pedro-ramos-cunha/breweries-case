
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

CREATE TABLE country (
	cntr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	cntr_desc TEXT(200) NULL
);
CREATE UNIQUE INDEX country_cntr_desc_IDX ON country (cntr_desc);
commit;

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

CREATE TABLE address (
	addr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	addr_line1 TEXT(200) NULL,
    addr_line2 TEXT(200) NULL,
    addr_line3 TEXT(200) NULL,
    addr_city_seq INTEGER NOT NULL,
    CONSTRAINT addr_city_seq_fk 
        FOREIGN KEY (addr_city_seq) 
        REFERENCES city (city_seq)
);
CREATE UNIQUE INDEX addr_desc_IDX ON addr (addr_city_seq,addr_line1,addr_line2,addr_line3);
commit;    

CREATE TABLE brewery (
	brwr_seq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	brwr_id TEXT(50) NOT NULL,
	brwr_name TEXT(500) NOT NULL,
    brwr_brtp_seq INTEGER NOT NULL,
    brwr_addr_seq INTEGER NULL,
    CONSTRAINT brewery_brtp_seq_fk 
        FOREIGN KEY (brwr_brtp_seq) 
        REFERENCES brewery_type (brtp_seq),
    CONSTRAINT brewery_addr_seq_fk 
        FOREIGN KEY (brwr_addr_seq) 
        REFERENCES address (addr_seq)
);
CREATE UNIQUE INDEX brewery_brwr_id_IDX ON brewery (brwr_id);
commit;