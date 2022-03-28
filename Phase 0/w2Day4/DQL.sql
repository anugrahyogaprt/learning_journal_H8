-- Select all data
SELECT * FROM teachers

-- Get id, first_name, last_name
SELECT id, first_name, last_name
FROM teachers

-- Membatasi jumlah output menjadi 4
SELECT * 
FROM teachers
LIMIT 4, 5

-- Urutkan data berdasarkan column "first_name" from A-Z
SELECT *
FROM teachers
ORDER BY first_name ASC

-- Conditional dosen yang mengajar di Harvard
SELECT *
FROM teachers
WHERE school = 'Harvard University'

-- Mencari dosen yang mengajar di Harvard atau Stanford (Cara 1)
SELECT *
FROM teachers
WHERE school='Harvard University' OR school = 'Standford University'

-- mencari lebih dari 1 (cara 2)
SELECT *
FROM teachers
WHERE school IN ('Harvard University', 'Standford University')

-- Mencari  unique universitas
SELECT DISTINCT (school)
FROM teachers

-- Mencari jumlah unique universitas
SELECT COUNT(DISTINCT (school)) as jumlah_universitas
FROM teachers
-- Melihat jumlah data 
SELECT COUNT(*)
FROM teachers