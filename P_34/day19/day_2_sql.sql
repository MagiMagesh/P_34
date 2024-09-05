
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