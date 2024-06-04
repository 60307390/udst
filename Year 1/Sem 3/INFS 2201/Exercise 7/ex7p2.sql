# Question 1
select * from agent where country = '94';

# Question 2
select customer_id, naem, phone_no from customer where area is null;

# Question 3
insert into purchase_order (cust_id, agent_id, ord_amount, ord_date)
values ('AB221', 'CC112', 252.25, '20240406');

# Question 4
update agent set phone='2000-2000' where phone='1123-9000';