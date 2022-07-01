alter table products
Add constraint fk_category_products Foreign KEY (categoryid)
REFERENCES category(id)

