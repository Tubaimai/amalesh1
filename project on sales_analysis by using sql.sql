use company
create table customers(customer_id int primary key, customer_name varchar(50),customer_email varchar(50))
create table orders(order_id int primary key,customer_id int,order_date date,order_total decimal(10,2), foreign key(customer_id) references customers(customer_id))
create table order_items(order_item_id int primary key,order_id int,product_id int,quality int,price decimal(10,2),foreign key(order_id) references orders(order_id))
create table products(product_id int primary key,product_name varchar(50),product_catagory varchar(50))

insert into customers(customer_id,customer_name,customer_email)
values(1,'amalesh','maityamalesh3@gmail.com')
insert into customers(customer_id,customer_name,customer_email)
values(2,'animesh_dinda','dindaanimesh263@gmail.com')
insert into customers(customer_id,customer_name,customer_email)
values(3,'debkumar_samanta','samantadebkumar56@gmail.com')

insert into products(product_id,product_name,product_catagory)
values(1,'oppo','catagory1')
insert into products(product_id,product_name,product_catagory)
values(2,'honor','catagory2')
insert into products(product_id,product_name,product_catagory)
values(3,'redmi','catagory3')

insert into orders(order_id,customer_id,order_date,order_total)
values(1,1,'2022-01-01',100.00)
insert into orders(order_id,customer_id,order_date,order_total)
values(2,2,'2022-01-02',200.00)
insert into orders(order_id,customer_id,order_date,order_total)
values(3,3,'2022-01-03',300.00)

insert into order_items(order_item_id,order_id,product_id,quality,price)
values(1,1,1,2,100.00)
insert into order_items(order_item_id,order_id,product_id,quality,price)
values(2,1,2,1,200.00)
insert into order_items(order_item_id,order_id,product_id,quality,price)
values(3,2,3,3,300.00)
insert into order_items(order_item_id,order_id,product_id,quality,price)
values(4,3,1,1,70.00)

select*from customers

select*from orders

select*from order_items

select*from products

SELECT
products.product_catagory, 
SUM(order_items.price * order_items.quality) AS total_revenue
FROM orders
INNER JOIN order_items ON orders.order_id = order_items.order_id
INNER JOIN products ON order_items.product_id = products.product_id
GROUP BY products.product_catagory

