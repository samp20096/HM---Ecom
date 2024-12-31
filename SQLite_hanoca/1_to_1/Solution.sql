-- 1. 
SELECT Courses.lecturer_id, Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Courses
INNER JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


-- 2. 
SELECT Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Courses
LEFT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


-- 3. 
INSERT INTO Lecturers (name) VALUES ('Tal')
SELECT Courses.lecturer_id, Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Lecturers
LEFT JOIN Courses ON Courses.lecturer_id = Lecturers.lecturer_id;


-- 4. 
SELECT Courses.lecturer_id, Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Courses
LEFT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id IS NULL;


-- 5. 
SELECT Courses.lecturer_id, Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Courses
RIGHT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id IS NULL;

-- 6. 
SELECT Courses.lecturer_id, Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Courses
FULL JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


-- 7. 
SELECT Courses.lecturer_id, Courses.name AS Course_name, Lecturers.name AS Lecturer_name FROM Courses
FULL JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id IS NULL OR Lecturers.lecturer_id IS NULL;

-- 8. 
SELECT * FROM Lecturers
WHERE name LIKE '%i%';


-- 9. 
SELECT count(name) AS Total_Lecturers FROM Lecturers;


-- 11. 
ALTER TABLE Courses ADD COLUMN weekly_hours;

UPDATE Courses
SET weekly_hours = 4
WHERE course_id < 4;

UPDATE Courses
SET weekly_hours = 6
WHERE course_id >= 4 AND course_id < 8;

UPDATE Courses
SET weekly_hours = 8
WHERE course_id >= 8;


-- 12. 
SELECT weekly_hours, count(weekly_hours) AS amount_of_courses FROM Courses
GROUP BY weekly_hours;


-- 13. 
SELECT Lecturers.name AS Lecturer_name, Courses.name AS course_name, Courses.weekly_hours FROM Courses
RIGHT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.weekly_hours = 8;


-- 14. 
DELETE FROM Courses
WHERE weekly_hours = 4 AND lecturer_id IS NULL;
