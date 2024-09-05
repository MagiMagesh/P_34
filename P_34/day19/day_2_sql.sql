
select * from student;

-- where column_name = logic

select * from student where sex = 'm' and age > 15;

select * from student where birth > '2025-10-01' or age > 100;

-- for sorting | order by by default it will be in ascending
select * from student where sex = 'm' or age > 100 order by age;

select * from student where sex = 'm' or age > 100 order by age desc;

select * from student where sex = 'm' or age > 100 order by birth desc;

-- agg functions
SELECT count(*) FROM crop_recommendation where k > 200;

SELECT * FROM crop_recommendation where k > 200;

select sum(age) from student;

select avg(age) from student;

select max(age) from student;

select min(age) from student;

select * from crop_recommendation;

-- to perform delte & update we have to remove safe mode 
SET SQL_SAFE_UPDATES = 0;


-- delete 
delete from crop_recommendation  where k > 200;

delete from crop_recommendation; -- wel will loose the entire table data

-- update
select * from student;

update student set sex = 'f' where sno = 3;

-- alter
-- add column
-- removig column
-- changing column name
-- changing column data type

-- syntax for alter table
-- alter table table_name add column column_name datatype;

alter table student add column scholoarship bool;

-- drop a column
alter table student drop column scholoarship ;

-- change a column datatype
alter table student modify column doj datetime ;

alter table student modify column name int ; -- not possible because already it has varchar datatype

alter table student change column doj  date_of_joining datetime ;




insert into student2 (name,email,fees) values ('Ram','1231@1231.sadf',10000); 
insert into student2 (name,email,fees,scholoarship) values ('Ram','12311@1231.sadf',10000,'yes'); 



select * from student;

-- where column_name = logic

select * from student where sex = 'm' and age > 15;

select * from student where birth > '2025-10-01' or age > 100;

-- for sorting | order by by default it will be in ascending
select * from student where sex = 'm' or age > 100 order by age;

select * from student where sex = 'm' or age > 100 order by age desc;

select * from student where sex = 'm' or age > 100 order by birth desc;

-- agg functions
SELECT count(*) FROM crop_recommendation where k > 200;

SELECT * FROM crop_recommendation where k > 200;

select sum(age) from student;

select avg(age) from student;

select max(age) from student;

select min(age) from student;

select * from crop_recommendation;

-- to perform delte & update we have to remove safe mode 
SET SQL_SAFE_UPDATES = 0;


-- delete 
delete from crop_recommendation  where k > 200;

delete from crop_recommendation; -- wel will loose the entire table data

-- update
select * from student;

update student set sex = 'f' where sno = 3;

-- alter
-- add column
-- removig column
-- changing column name
-- changing column data type

-- syntax for alter table
-- alter table table_name add column column_name datatype;

alter table student add column scholoarship bool;

-- drop a column
alter table student drop column scholoarship ;

-- change a column datatype
alter table student modify column doj datetime ;

alter table student modify column name int ; -- not possible because already it has varchar datatype

alter table student change column doj  date_of_joining datetime ;

-- constraints:
-- to maintain data integrity while creating the table.

-- unique 			- to maintain unique data in that column.
-- not null 		- we cannoct have null value for that column.
-- primary key		- combination of unique and not null | it should be used to only one column in that entire table
-- default			- it will take the default data if we are not give it
-- auto increment	- it should be added to a column of primary key

create table student1 (
	sno int primary key,
    name varchar(255),
    email varchar(255) unique,
    fees int not null,
    scholoarship char(5) default 'no'
);

select * from student1;

insert into student1 values (1,'magesh','123@123.sadf',1000,'no');
insert into student1 values (1,'magesh','123@123.sadf',1000,'no'); -- primary key constraint
insert into student1 values (2,'magesh','123@123.sadf',1000,'no'); -- unique constraint
insert into student1 values (2,'magesh','123@1231.sadf',null,'no'); -- not null constraint
insert into student1 (sno,name,email,fees) values (2,'Ram','1231@1231.sadf',10000); 
insert into student1 (sno,name,email,fees,scholoarship) values (3,'Ram','12311@1231.sadf',10000,'yes'); 


create table student2 (
	sno int primary key auto_increment,
    name varchar(255),
    email varchar(255) unique,
    fees int not null,
    scholoarship char(5) default 'no'
);

select * from student2;

insert into student2 (name,email,fees) values ('Ram','1231@1231.sadf',10000); 
insert into student2 (name,email,fees,scholoarship) values ('Ram','12311@1231.sadf',10000,'yes'); 


create table student3 (
	sno int unique,
    name varchar(255),
    email varchar(255) primary key,
    fees int not null,
    scholoarship char(5) default 'no'
);

select * from student3;

create table student4 (
	sno int unique auto_increment, -- not best practise
    name varchar(255),
    email varchar(255) primary key,
    fees int not null,
    scholoarship char(5) default 'no'
);

-- not acceptable
create table student5 (
	sno int unique , 
    name varchar(255),
    email varchar(255) primary key auto_increment,
    fees int not null,
    scholoarship char(5) default 'no'
);