
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    mark INT
);

INSERT INTO students
    (student_id, name, department, mark)
VALUES
    (1, 'Arun', 'CSBS', 85),
    (2, 'Priya', 'CSE', 92),
    (3, 'Kumar', 'CSBS', 78),
    (4, 'Divya', 'IT', 88);

SELECT * FROM students;

SELECT name, mark
FROM students
WHERE mark > 80
ORDER BY mark DESC;

SELECT AVG(mark) AS average_mark
FROM students;

SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department;
