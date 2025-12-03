CREATE DATABASE college_db;
USE college_db;
CREATE TABLE students(
student_id INT auto_increment PRIMARY KEY,
firts_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
age INT,
city VARCHAR(50)
);
INSERT INTO students (firts_name,last_name,email,age,city)
VALUES
("Aisha","Khan","aisha@example.com",20,"Mumbai"),
("Rahul","Sharma","rahul@example.com",22,"Delhi"),
("Meera","Iyer","meera@example.com",21,"Chennai"),
("Imran","Ali","imran@example.com",23,"Hyderabad");

SELECT * from students;
SELECT firts_name,last_name,city FROM students;
SELECT * FROM students WHERE city = "Delhi";
SELECT * FROM students order by age DESC;
UPDATE students
SET city = "Bangalore"
WHERE student_id = 2;
SET SQL_SAFE_UPDATES = 0;
UPDATE students
SET age = 24 WHERE email ="imran@example.com";

delete FROM students
WHERE student_id = 3;
delete FROM students
WHERE city = "Mumbai";
DROP TABLE students;
DROP DATABASE college_db;
