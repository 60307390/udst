# Query 1
select sum(size) from gallery;

# Query 2
select artist.name as name, count(*) as pieces_on_display
from artist inner join artwork
on artwork.artist_id=artist.artist_id
group by artist.name;

# Query 3
select artwork.title as title, artist.name as artist from 
artist inner join artwork on artwork.artist_id=artist.artist_id
where artwork.media like "%canvas%" and artwork_id in (
	select artwork_id from installation where exhibition_id in (
		select exhibition_id from exhibition where gallery_id in (
			select gallery_id from gallery where location='Chicago'
        )
    )
);

# Query 4
alter table invoice_line drop column price;
alter table invoice_line add column price decimal(8,2) not null;
update invoice_line set price=4800 where artwork_id=2;
update invoice_line set price=3200.75 where artwork_id=5;
update invoice_line set price=6500 where artwork_id=8;
update invoice_line set price=45200.80 where artwork_id=11;
update invoice_line set price=3900 where artwork_id=14;


# Query 5
select * from artwork;
select * from installation;
insert into exhibition values (6,'2024-05-01','2024-06-28',2);
insert into installation values(6, 1);
insert into installation values(6, 8);
insert into installation values(6, 11);
insert into installation values(6, 20);
insert into installation values(6, 16);
insert into installation values(6, 14);
insert into installation values(6, 3);
insert into installation values(6, 19);
insert into installation values(6, 2);
insert into installation values(6, 5);
insert into installation values(6, 7);
insert into installation values(6, 9);

select artwork.title, artwork.media, artist.name from 
artwork inner join artist
on artwork.artist_id=artist.artist_id
where artwork.artwork_id in (
	select artwork_id from installation where exhibition_id=6
);