drop table if exists aggr_brewery_by_country_brewery_type;
drop table if exists aggr_brewery_by_country_state_brewery_type;
CREATE TABLE aggr_brewery_by_country_state_brewery_type (
    country text NOT NULL,
    state_province text NOT NULL,
    brewery_type TEXT NOT NULL,
    n_of_breweries INTEGER DEFAULT (0) NOT NULL
);

CREATE TABLE aggr_brewery_by_country_brewery_type (
    country text NOT NULL,
    brewery_type TEXT NOT NULL,
    n_of_breweries INTEGER DEFAULT (0) NOT NULL
);

delete from aggr_brewery_by_country_state_brewery_type  where 1=1;
INSERT INTO aggr_brewery_by_country_state_brewery_type
(country, state_province, brewery_type, n_of_breweries)
select cntr_desc, stpr_desc, brtp_desc, count(*)
from brewery b 
join city c on c.city_seq =b.brwr_city_seq 
join state_province sp on sp.stpr_seq = c.city_stpr_seq
join country cn on cn.cntr_seq = sp.stpr_cntr_seq 
join brewery_type bt on bt.brtp_seq = b.brwr_brtp_seq 
group by cntr_desc, stpr_desc, brtp_desc;

delete from aggr_brewery_by_country_brewery_type  where 1=1;
INSERT INTO aggr_brewery_by_country_brewery_type
(country, brewery_type, n_of_breweries)
select cntr_desc, brtp_desc, count(*)
from brewery b 
join city c on c.city_seq =b.brwr_city_seq 
join state_province sp on sp.stpr_seq = c.city_stpr_seq
join country cn on cn.cntr_seq = sp.stpr_cntr_seq 
join brewery_type bt on bt.brtp_seq = b.brwr_brtp_seq 
group by cntr_desc, brtp_desc;