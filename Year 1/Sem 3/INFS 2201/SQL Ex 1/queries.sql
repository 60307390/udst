create table student(
	st_ID int primary key not null auto_increment,
    st_name varchar(45) not null,
    st_phone varchar(12) not null unique,
    st_address varchar(169) not null,
    st_gpa decimal(3,2) not null
);

insert into student(st_ID, st_name, st_phone, st_address, st_gpa) values (123, 'Ahmad', 435434534, 'thuamama street, thumama', 2.5);
insert into student(st_name, st_phone, st_address, st_gpa) values ('Mustafa', 345344534, 'alQabban street, al-jadeeda', 3.9);
insert into student(st_name, st_phone, st_address, st_gpa) values ('Soha', 435345435, 'society avenue, bidda', 3);
insert into student(st_name, st_phone, st_address, st_gpa) values ('Gamela', 34534534, 'wick street, jonathan district', 3.4);

select * from student;
select * from student where st_gpa >= 3;
select st_name from student where st_gpa < 2;
select st_ID, st_name from student where st_gpa < 3.5 and st_gpa > 3;
update student set st_name = "Ola" where st_ID = 125;
delete from student where st_ID = 124;
desc student;

select max(st_gpa), min(st_gpa) from student;
select sum(st_gpa) from student;
select count(st_gpa > 2) from student;
select st_ID, st_name from student where st_gpa > 2 order by st_gpa;

alter table student add column ST_CITY varchar(45) not null;
alter table student add column ST_DEPT varchar(45) not null;
alter table student drop column ST_DEPT;
alter table student rename column ST_CITY to ST_MAJOR;

# test
select count(st_gpa) from student where st_gpa > 2;