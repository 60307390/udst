use db60307390;

create table user_account(
	username varchar(20) primary key not null,
    password varchar(200) not null
);

create table customer (
	customer_id int primary key not null,
    name varchar(100) not null,
    phone varchar(20) not null,
    email varchar(150) not null,
    username varchar(20) not null,
    foreign key (username) references user_account(username)
);

create table visit (
	ticket_id int primary key not null,
    date datetime null,
    customer_id int not null,
    foreign key (customer_id) references customer(customer_id)
);

create table categories (
	categories_id int primary key not null,
    description varchar(50) not null
);

create table preferences (
	customer_id int not null,
    categories_id int not null,
    foreign key (customer_id) references customer(customer_id),
    foreign key (categories_id) references categories(categories_id)
);

create table artist (
	artist_id int primary key not null,
    name varchar(100) not null,
    email varchar(150) not null,
    phone varchar(20) not null,
    bio text not null,
    username varchar(20) not null,
    foreign key (username) references user_account(username)
);

create table artwork ( 
	artwork_id int primary key not null,
    title varchar(50) not null,
    media varchar(50) not null,
    date date not null,
    dimensions varchar(100) not null,
    status varchar(20) not null,
    artist_id int not null,
    foreign key (artist_id) references artist(artist_id)
);

create table invoice (
	invoice_id int primary key not null,
    date datetime not null,
    customer_id int not null,
    foreign key (customer_id) references customer(customer_id)
);

create table invoice_line (
	artwork_id int not null,
    invoice_id int not null,
    foreign key (artwork_id) references artwork(artwork_id),
    foreign key (invoice_id) references invoice(invoice_id)
);

create table gallery (
	gallery_id int primary key not null,
    location varchar(45) not null,
    size int not null
);

create table exhibition (
	exhibition_id int primary key not null,
    start date not null,
    end date not null,
    gallery_id int not null,
    foreign key (gallery_id) references gallery(gallery_id)
);

create table installation (
	exhibition_id int not null,
    artwork_id int not null,
    foreign key (exhibition_id) references exhibition(exhibition_id),
    foreign key (artwork_id) references artwork(artwork_id)
);

insert into user_account (username, password) values ('artist_jdoe', 'Passw0rd!');
insert into user_account (username, password) values ('artist_jsmith', 'Secur3P@ss');
insert into user_account (username, password) values ('artist_ejohn', 'EJsaf3pa55');
insert into user_account (username, password) values ('cust_abrown', 'Alice123!');
insert into user_account (username, password) values ('cust_bwhite', 'Bwhite456!');
insert into user_account (username, password) values ('cust_cblack', 'Cblack789!');

insert into artist (artist_id, name, email, phone, bio, username) values (1, 'John Doe', 'john.doe@example.com', '123-456-7890', 'Contemporary artist from New York', 'artist_jdoe');
insert into artist (artist_id, name, email, phone, bio, username) values (2, 'Jane Smith', 'jane.smith@example.com', '234-567-8901', 'Abstract painter known for vibrant colors', 'artist_jsmith');
insert into artist (artist_id, name, email, phone, bio, username) values (3, 'Emily Johnson', 'emily.johnson@example.com', '345-678-9012', 'Modern artist incorporating AI in visual arts', 'artist_ejohn');

insert into customer (customer_id, name, phone, email, username) values (1, 'Alice Brown', '456-789-0123', 'alice.brown@example.com', 'cust_abrown');
insert into customer (customer_id, name, phone, email, username) values (2, 'Bob White', '567-890-1234', 'bob.white@example.com', 'cust_bwhite');
insert into customer (customer_id, name, phone, email, username) values (3, 'Charlie Black', '678-901-2345', 'charlie.black@example.com', 'cust_cblack');

insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (1, 'Sunset Overdrive', 'Oil on Canvas', '2022-05-15', '24x36 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (2, 'Abstract Thoughts', 'Acrylic', '2021-11-10', '30x40 inches', 'Sold', 2);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (3, 'Digital Dreams', 'Digital Print', '2023-02-20', '1920x1080 pixels', 'Available', 3);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (4, 'Nature\'s Embrace', 'Mixed Media', '2022-07-22', '20x30 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (5, 'Vibrant Silence', 'Oil on Canvas', '2021-08-15', '36x48 inches', 'Sold', 2);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (6, 'AI Visions', 'Digital Art', '2023-04-05', '1080x1920 pixels', 'Available', 3);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (7, 'Urban Jungle', 'Spray Paint', '2022-03-30', '40x60 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (8, 'Color Symphony', 'Watercolor', '2021-09-10', '18x24 inches', 'Sold', 2);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (9, 'Future Landscapes', 'Digital Art', '2023-06-01', '1920x1080 pixels', 'Available', 3);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (10, 'Ethereal Beauty', 'Oil on Canvas', '2022-12-12', '24x36 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (11, 'Silent Echoes', 'Acrylic', '2021-10-05', '20x30 inches', 'Sold', 2);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (12, 'AI Perspectives', 'Digital Art', '2023-03-15', '1080x1920 pixels', 'Available', 3);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (13, 'Golden Horizon', 'Oil on Canvas', '2022-08-10', '24x36 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (14, 'Abstract Energy', 'Acrylic', '2021-12-20', '30x40 inches', 'Sold', 2);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (15, 'Digital Reality', 'Digital Print', '2023-01-25', '1920x1080 pixels', 'Available', 3);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (16, 'Mountain Majesty', 'Oil on Canvas', '2022-06-14', '20x30 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (17, 'Color Harmony', 'Watercolor', '2021-09-30', '18x24 inches', 'Sold', 2);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (18, 'Future Visions', 'Digital Art', '2023-07-10', '1920x1080 pixels', 'Available', 3);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (19, 'Serenity', 'Oil on Canvas', '2022-11-11', '24x36 inches', 'Available', 1);
insert into artwork (artwork_id, title, media, date, dimensions, status, artist_id) values (20, 'Abstract Symphony', 'Acrylic', '2021-08-22', '30x40 inches', 'Sold', 2);

insert into visit (ticket_id, date, customer_id) values (1, '2023-01-15 10:30:00', 1);
insert into visit (ticket_id, date, customer_id) values (2, '2023-02-10 14:00:00', 2);
insert into visit (ticket_id, date, customer_id) values (3, '2023-03-05 16:45:00', 3);

insert into categories (categories_id, description) values (1, 'Contemporary Art');
insert into categories (categories_id, description) values (2, 'Abstract Art');
insert into categories (categories_id, description) values (3, 'Digital Art');

insert into preferences (customer_id, categories_id) values (1, 1);
insert into preferences (customer_id, categories_id) values (2, 2);

insert into invoice (invoice_id, date, customer_id) values (1, '2023-04-10 12:00:00', 1);
insert into invoice (invoice_id, date, customer_id) values (2, '2023-05-15 15:30:00', 2);

insert into invoice_line (artwork_id, invoice_id) values (2, 1);
insert into invoice_line (artwork_id, invoice_id) values (5, 1);
insert into invoice_line (artwork_id, invoice_id) values (8, 2);
insert into invoice_line (artwork_id, invoice_id) values (11, 2);
insert into invoice_line (artwork_id, invoice_id) values (14, 2);

insert into gallery (gallery_id, location, size) values (1, 'New York', 2000);
insert into gallery (gallery_id, location, size) values (2, 'Los Angeles', 1800);
insert into gallery (gallery_id, location, size) values (3, 'Chicago', 1600);
insert into gallery (gallery_id, location, size) values (4, 'San Francisco', 1500);

insert into exhibition (exhibition_id, start, end, gallery_id) values (1, '2023-01-01', '2023-01-31', 1);
insert into exhibition (exhibition_id, start, end, gallery_id) values (2, '2023-02-01', '2023-02-28', 2);
insert into exhibition (exhibition_id, start, end, gallery_id) values (3, '2023-03-01', '2023-03-31', 3);
insert into exhibition (exhibition_id, start, end, gallery_id) values (4, '2023-04-01', '2023-04-30', 4);
insert into exhibition (exhibition_id, start, end, gallery_id) values (5, '2023-05-01', '2023-05-31', 1);

insert into installation (exhibition_id, artwork_id) values (1, 1);
insert into installation (exhibition_id, artwork_id) values (1, 2);
insert into installation (exhibition_id, artwork_id) values (2, 3);
insert into installation (exhibition_id, artwork_id) values (2, 4);
insert into installation (exhibition_id, artwork_id) values (3, 5);
insert into installation (exhibition_id, artwork_id) values (3, 6);
insert into installation (exhibition_id, artwork_id) values (4, 7);
insert into installation (exhibition_id, artwork_id) values (4, 8);
insert into installation (exhibition_id, artwork_id) values (5, 9);
insert into installation (exhibition_id, artwork_id) values (5, 10);
