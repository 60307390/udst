# Q1
select count(*) from book where author_id=501;

# Q2
select publisher_id as publisher, count(*) as quantity 
from book group by publisher_id having publisher_id in (60, 180);

# Q3
# select count(distinct(author_id)) as total from book group by publisher_id having publisher_id=50;
select count(author_id) as total from book group by publisher_id having publisher_id=50;

# select author_id, book.publisher_id from book inner join publisher where book.publisher_id=publisher.publisher_id and book.publisher_id=50;

# Q4
select author_id, count(*) from book group by author_id having count(*) = 6;

# Q5
select customer_id from shopping_cart where ordered is not null group by customer_id having count(*)=2;

# Q6
select title from book where publisher_id in (
	select publisher_id from publisher where url like "%.com"
) order by title;



### Part 2

# Q1
select warehouse_id as warehouse, sum(quantity) as total_books 
from availability group by warehouse_id having total_books > 120000;

# Q2
update availability set quantity=quantity+100 where (warehouse_id=2) and (quantity<50);

# Q3
select count(*) from book where book_id not in (select book_id from cart_item);

# Q4
select count(*), sum(quantity) from cart_item where cart_id in (
	select cart_id from shopping_cart where customer_id in (
		select customer_id from customer where (first_name='Lloyd' and last_name='Rust')
    )
);