Insert into country(cntr_desc)
select distinct trim(country) from breweries_semi_treated bst ;

insert into state_province (stpr_desc, stpr_cntr_seq)
select distinct trim(bst.state_province), cntr_seq
from breweries_semi_treated bst 
join country c on c.cntr_desc = trim(bst.country);

insert into city (city_desc, city_stpr_seq)
select distinct trim(bst.city), st.stpr_seq
from breweries_semi_treated bst 
join country c on c.cntr_desc = trim(bst.country)
join state_province st on st.stpr_desc = trim(bst.state_province);


insert into brewery_type (brtp_desc)
select distinct trim(bst.brewery_type)
from breweries_semi_treated bst; 


INSERT INTO brewery
( brwr_id, brwr_name, brwr_url, brwr_phone, brwr_brtp_seq, brwr_city_seq)
select distinct bst.id, bst.name,bst.website_url, bst.phone,  bt.brtp_seq, ct.city_seq
from breweries_semi_treated bst 
join brewery_type bt on  bt.brtp_desc = trim(bst.brewery_type)
join country c on c.cntr_desc = trim(bst.country)
join state_province st on st.stpr_desc = trim(bst.state_province) and st.stpr_cntr_seq = c.cntr_seq
join city ct on ct.city_desc = trim(bst.city)  and ct.city_stpr_seq = st.stpr_seq;



