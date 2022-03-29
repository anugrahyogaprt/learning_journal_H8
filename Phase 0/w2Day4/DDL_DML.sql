-- Create table teachers
create table teachers(
  id INT not NULL PRIMARY key AUTO_INCREMENT,
  first_name VARCHAR(25),
  last_name VARCHAR(50),
  school VARCHAR(50),
  hire_date DATE,
  salary NUMERIC
)

-- Menambahkan column Age 
ALTER TABLE teachers add age INT

-- Menghapus column age 
alter table teachers drop column age

-- Rename table teachers menjadi guru 
alter table teachers rename to guru

-- Mengganti tipe data column salary 
alter table guru modify column salary int

-- Mengganti nama column "first_name" ke "nama_depan"
alter table guru change COLUMN first_name nama_depan varchar(25)

-- Mengganti nama table "guru" ke "teachers"
alter table guru rename to teachers

-- Mengganti nama column "nama_depan" ke "first_name"
alter table teachers change COLUMN nama_depan first_name varchar(25)

-- Insert data ke database 
INSERT INTO teachers (id,first_name, last_name, school, hire_date, salary)
    VALUES (1,'Janet', 'Smith', 'MIT', '2011-10-30', 36200),
           (2,'Lee', 'Reynolds', 'MIT', '1993-05-22', 65000),
           (3,'Samuel', 'Cole', 'Cambridge University', '2005-08-01', 43500),
           (4,'Samantha', 'Bush', 'Cambridge University', '2011-10-30', 36200),
           (5,'Betty', 'Diaz', 'Cambridge University', '2005-08-30', 43500),
           (6,'Kathleen', 'Roush', 'MIT', '2010-10-22', 38500),
           (7,'James', 'Diaz', 'Harvard University', '2003-07-18', 61000),
           (8,'Zack', 'Smith', 'Harvard University', '2000-12-29', 55500),
           (9,'Luis', 'Gonzales', 'Standford University', '2002-12-01', 50000),
           (10,'Frank', 'Abbers', 'Standford University', '1999-01-30', 66000);

-- Update Salary "Janet Smith" 
update teachers
set salary=50000 
where first_name='Janet'

-- Delete id=10 
delete from teachers 
where id=10

-- Insert Data 2 
INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Samuel', 'Abbers', 'Standford University', '2006-01-30', 32000),
           ('Jessica', 'Abbers', 'Standford University', '2005-01-30', 33000),
           ('Tom', 'Massi', 'Harvard University', '1999-09-09', 39500),
           ('Esteban', 'Brown', 'MIT', '2007-01-30', 36000),
           ('Carlos', 'Alonso', 'Standford University', '2001-01-30', 44000);
           
-- Menghapus Semua Data 
truncate table teachers

-- Menhapus table "teachers" 
drop table teachers

-- Get all data 
select * from teachers

-- Get id, firsta_name, last_name 
select id, first_name, last_name 
from teachers

-- Membatasi jumlah output menjadi 4 
select * 
from teachers
limit 0, 4

-- Mengurutkan data berdasarkan column "first_name" dari Z-A
select * 
from teachers
order by first_name DESC

-- Mencari dosen yang mengajar di Harvard University 
select *
from teachers
where school='Harvard University'

-- Mencari dosen yang mengajar di Harvard University atau Stanford University (Cara 1)
select *
from teachers 
where school='Harvard University' OR school='Standford University'

-- Mencari dosen yang mengajar di Harvard University atau Stanford University (Cara 2)
select *
from teachers 
where school in ('Harvard University', 'Standford University')

-- Mencari unique universitas 
select distinct(school)
from teachers

-- Mencari jumlah unique universitas 
select count(distinct(school)) as jumlah_universitas
from teachers 

-- Melihat berapa banyak jumlah data 
select count(*)
from teachers

-- Melihat data dosen bernama "james"
select * 
from teachers
where BINARY first_name='james'