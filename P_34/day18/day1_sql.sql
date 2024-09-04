-- create database
create database p34;
CREaTE DATaBASE p341;


-- to display all the database
show databases;

-- delete a database
drop database premainboot;
dRop dataBase p341;

-- CRUD Create Read Update Delete


-- create table table_name (
-- 	column_name data_types
-- )

use p34;

create table student (
	sno int,
    name varchar(255),
    age float,
    sex char(5),
    dob date,
    doj time,
    birth datetime,
    time_reached double
);

-- insert into table_name values ()

insert into student values (1,'magesh',15.0000003,'m','25-11-11','22:22:22','25-11-11T22:22:22',32.0000004);
insert into student values (1,'magesh',15.003,'m','25-10-11','22:22:22','25-10-11',32.0000004);
insert into student values (2,'ram',15.0000003,'m','20-11-11','12:12:22','25-11-11T22:22:22',32.12340004);


select * from student;