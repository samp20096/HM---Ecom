 -- 1. 
select p.category_id, p.product_id, p.name, n.calories, n.fats, n.sugar
from products p
join nutritions n on p.product_id = n.nutrition_id;


 -- 2. 
select *
from products_orders po
join products p on p.product_id = po.order_id
order by po.order_id;

 -- 3. 
insert into products_orders (order_id, product_id, amount) values (1, 8, 1);
insert into products_orders (order_id, product_id, amount) values (2, 4, 1);
insert into products_orders (order_id, product_id, amount) values (3, 5, 1);
insert into products_orders (order_id, product_id, amount) values (4, 2, 1);
insert into products_orders (order_id, product_id, amount) values (5, 7, 1);


 -- 4. 
update orders
set total_price = (
	select sum(po.amount * p.price)
	from products_orders po
	join products p on po.product_id = p.product_id
	where po.order_id = orders.order_id
)


 -- 5. 
select max(o.total_price) as max_price,
min(o.total_price) as min_price,
round(avg(o.total_price)::numeric, 2) as average_price
from orders o


 -- 6. 
select order_id, sum(amount) as total_products
from products_orders po
group by order_id
order by total_products desc limit 1;


 -- 7. 
select max(total_sold) as most_sold, min(total_sold) as less_sold, round(avg(total_sold), 2) as average_sold 
from (
	select product_id, sum(amount) as total_sold
	from products_orders po 
	group by product_id
) as product_total


 -- 8. 
select (
	select category_id
	from (
		select p.category_id, sum(amount) as total_sold
		from products_orders po
		join products p on po.product_id = p.product_id
		group by p.category_id
	) as product_totals
	order by total_sold desc limit 1) as most_sold_by_category,
	(
		select category_id
		from (
		select p.category_id, sum(amount) as total_sold
		from products_orders po
		join products p on po.product_id = p.product_id
		group by p.category_id
		) as products_totals
	order by total_sold limit 1) as least_sold_by_category,
	max(total_sold) as most_products_sold, 
	min(total_sold) as least_products_sold
from (
		select c.name, sum(amount) as total_sold
		from products_orders po
		join category c on po.product_id = c.category_id
		group by c.category_id
) as product_totals;
