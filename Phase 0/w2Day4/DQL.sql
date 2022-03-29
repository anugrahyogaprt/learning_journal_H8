-- Melihat jumlah data 
select count(*)
from teachers;

-- Melihat total salary dosen 
select sum(salary)
from teachers;

-- Melihat gaji dosen tertinggi yang mengajar di MIT 
select id, first_name, last_name, max(salary)
from teachers
where school='MIT';

-- Melihat rata-rata gaji dosen yang mengajar di Harvard University 
select ceil(avg(salary))
from teachers
where school='Harvard University';

-- Mencari dosen dengan first_name mengandung "sam" 
select *
from teachers
where first_name like '%sam%';

-- Mencari jumlah dosen disetiap universitas 
select school, count(id) as total_dosen
FROM teachers 
group by school;

-- Mencari rata-rata gaji disetiap universitas 
select school, floor(AVG(salary))
from teachers 
group by school;

-- Menampilkan guru dengan gaji tertinggi 
select *
from teachers
where salary=(
  select max(salary)
  from teachers  
 );

-- Menampilkan setiap dosen yang memiliki gaji tertinggi disetiap universitas 
select * 
from teachers
where (school, salary) in (
  select school, max(salary)
  from teachers
  group by school
 );

-- Join table teachers dengan courses 
select * 
from teachers 
join courses on teachers.id=courses.teachers_id
order by teachers.id asc;

-- Melihat dosen yang mengajar Calculus dengan gaji tertinggi (syntax yang salah)
select teachers.id, teachers.first_name, teachers.Last_name, teachers.school, max(teachers.salary)
from teachers 
join courses on teachers.id=courses.teachers_id
where courses.name='Calculus';

-- Melihat dosen yang mengajar Physic dengan gaji terendah 
select * 
from teachers
where salary=(
  select min(salary)
  from teachers 
  join courses on teachers.id=courses.teachers_id
  where courses.name='Physics'
);

-- Melihat dosen dengan jumlah mata kuliah yang diajarkan 
select teachers.id, teachers.first_name, teachers.last_name, count(courses.id) as total_matkul
from teachers 
join courses on teachers.id=courses.teachers_id
group by teachers.id
order by total_matkul desc;

-- Melihat dosen dengan jumlah mata kuliah yang diajarkan lebih dari 1
select teachers.id, teachers.first_name, teachers.last_name, count(courses.id) as total_matkul
from teachers 
join courses on teachers.id=courses.teachers_id
group by teachers.id
having total_matkul>1
order by total_matkul desc;
