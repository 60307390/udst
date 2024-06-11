use db60307390;

create table author(
	author_id int(11) primary key not null auto_increment,
    name varchar(100) not null,
    url varchar(250) null
);

create table publisher(
	publisher_id int(11) primary key not null auto_increment,
    name varchar(100) not null,
    address varchar(75) null,
    phone varchar(20) null,
    url varchar(100) null
);

create table book(
	book_id int(11) primary key not null auto_increment,
    isbn char(5) null,
    year int(11) not null,
    title varchar(300) not null,
    category varchar(30) not null,
    price decimal(8,2) null,
    author_id int(11) not null,
    publisher_id int(11) null,
    foreign key (author_id) references author(author_id),
    foreign key (publisher_id) references publisher(publisher_id)
);

create table customer(
	customer_id int(11) primary key not null auto_increment,
    first_name varchar(25) not null,
    last_name varchar(30) not null,
    phone varchar(20) not null,
    email varchar(100) not null,
    address varchar(50) not null,
    city varchar(50) not null,
    country varchar(50) not null
);

create table shopping_cart(
	cart_id int(11) primary key not null auto_increment,
    customer_id int(11) not null,
    created datetime not null,
    ordered datetime null,
    foreign key (customer_id) references customer(customer_id)
);

create table cart_item(
	cart_id int(11) not null,
    book_id int(11) not null,
    quantity int(11) not null,
    foreign key (cart_id) references shopping_cart(cart_id),
    foreign key (book_id) references book(book_id)
);

create table warehouse(
	warehouse_id int(11) primary key not null auto_increment,
    phone varchar(20) not null,
    city varchar(50) not null
);

create table availability(
	book_id int(11) not null,
    warehouse_id int(11) not null,
    quantity int(11) not null,
    foreign key (book_id) references book(book_id),
    foreign key (warehouse_id) references warehouse(warehouse_id)
);