create table products (
	product_id serial primary key,
	name varchar(100), 
	price real, 
	category_id int, 
	foreign key (category_id) references category(category_id) on delete cascade
); 

create table category (
	category_id serial primary key, 
	name varchar(100)
);

create table nutritions (
	nutrition_id serial primary key, 
	product_id int, 
	foreign key (product_id) references products(product_id) on delete cascade, 
	name varchar(100), 
	calories int, 
	fats real, 
	sugars real
); 

create table orders (
	order_id serial primary key, 
	date_time timestamp, 
	address varchar(100), 
	costumer_name varchar(100), 
	costumer_ph varchar(15), 
	total_price real
); 

create table products_orders (
	order_id int, 
	product_id int, 
	primary key (order_id, product_id), 
	foreign key (order_id) references orders(order_id) on delete cascade,
	foreign key (product_id) references products(product_id) on delete cascade, 
	amount int
);