SELECT Courses.topic, Grades.course_id, avg(Grades.grade) FROM Grades
JOIN Courses ON Grades.course_id = Courses.course_id
GROUP BY Grades.course_id;
