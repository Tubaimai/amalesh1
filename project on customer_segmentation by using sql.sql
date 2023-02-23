use d_tableau
create table customer_segmentation(customer_id int,customer_name varchar(50),customer_email varchar(25),age int, gender char(2),purchase_count int,last_purchase_date date)

insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(1,'amalesh_maity','maityamalesh3@gmail.com',23,'m',5,'2023-02-22')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(2,'animesh_dinda','dindaanimesh63@gmail.com',22,'m',9,'2023-02-12')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(3,'anita_adak','adakanita22@gmail.com',24,'f',15,'2023-01-07')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(4,'koushik_barman','kaushikbarman45@gmail.com',25,'m',9,'2023-02-02')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(5,'krishnendu_mahapatra','kmahapatra63@gmail.com',32,'m',8,'2023-01-28')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(6,'taruna_kotal','kotaltarun21@gmail.com',45,'m',3,'2022-12-12')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(7,'susmita_dinda','susmita3@gmail.com',45,'m',2,'2022-05-21')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(8,'payel_samanta','smantapayel45@gmail.com',15,'f',18,'2023-01-23')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(9,'susmita_adak','susmitadak89@gmail.com',28,'f',12,'2023-01-11')
insert into customer_segmentation(customer_id,customer_name,customer_email,age,gender,purchase_count,last_purchase_date)
values(10,'banita_adak','baniitadak89@gmail.com',50,'f',2,'2020-01-01')

select* from customer_segmentation

SELECT
CASE
WHEN age < 30 THEN '18-29'
WHEN age >= 30 AND age < 40 THEN '30-39'
WHEN age >= 40 AND age < 50 THEN '40-49'
ELSE '50+'
end 
as age_group,
gender,
COUNT(*) AS customer_count
FROM
customer_segmentation
GROUP BY
CASE
WHEN age < 30 THEN '18-29'
WHEN age >= 30 AND age < 40 THEN '30-39'
WHEN age >= 40 AND age < 50 THEN '40-49'
ELSE '50+'
end,
gender



