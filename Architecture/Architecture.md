# Architecture 

On these part I will describe the architecture I would use for these case. 

Considering the documentation available about the open breweries org :

| Field          | Type           | Description                                       |
|----------------|----------------|---------------------------------------------------|
| id             | string         | Unique identifier for the brewery                 |
| name           | string         | Brewery name                                      |
| brewery_type   | string         | Type of brewery (see by_type for possible values) |
| address_1      | string or null | Primary street address                            |
| address_2      | string or null | Secondary address line                            |
| address_3      | string or null | Third address line                                |
| city           | string         | City name                                         |
| state_province | string         | State or province                                 |
| postal_code    | string         | Postal or ZIP code                                |
| country        | string         | Country name                                      |
| longitude      | number or null | Longitude coordinate                              |
| latitude       | number or null | Latitude coordinate                               |
| phone          | string or null | Contact phone number                              |
| website_url    | string or null | Brewery website URL                               |
| state          | string         | State abbreviation or name (deprecated)           |
| street         | string or null | Street address (deprecated)                       |