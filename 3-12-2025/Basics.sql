CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    age INT,
       city VARCHAR(50)
       );

INSERT INTO students (first_name, last_name, email, age, city) VALUES
('John', 'Doe', 'john.doe@example.com', 22, 'New York'),
('Alice', 'Smith', 'alice.smith@example.com', 24, 'Los Angeles'),
('Robert', 'Brown', 'robert.brown@example.com', 21, 'Chicago'),
('Emily', 'Johnson', 'emily.johnson@example.com', 23, 'Houston');

SELECT*from students;

SELECT first_name, last_name, city
FROM students;

select *from students
WHERE city='Chicago';

select * from students
order by age DESC

UPDATE students
SET city = "Banglore"
WHERE student_id = 2;
 

UPDATE students
SET city = "Arteta"
WHERE email = "robert.brown@example.com";
 
 
DELETE FROM students
WHERE student_id = 4;
 

DELETE FROM students
WHERE city = "DELHI";

DROP DATABASE college_db;
