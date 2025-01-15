INSERT INTO Courses (topic, hours) VALUES ('English', 3);
INSERT INTO Courses (topic, hours) VALUES ('Russian', 1);
INSERT INTO Courses (topic, hours) VALUES ('Hebrew', 4);


INSERT INTO Students (name, email) VALUES ('Tal', 'tal@gmai.com');
INSERT INTO Students (name, email) VALUES ('David', 'david@gmai.com');
INSERT INTO Students (name, email) VALUES ('Omer', 'omer@gmai.com');
INSERT INTO Students (name, email) VALUES ('Jony', 'jony@gmai.com');

-- Grades for Tal
INSERT INTO Grades (student_id, course_id, grade) VALUES (1, 1, 98)
INSERT INTO Grades (student_id, course_id, grade) VALUES (1, 3, 68);
INSERT INTO Grades (student_id, course_id, grade) VALUES (1, 2, 90);

-- Grades for David
INSERT INTO Grades (student_id, course_id, grade) VALUES (2, 1, 99);
INSERT INTO Grades (student_id, course_id, grade) VALUES (2, 3, 100);
INSERT INTO Grades (student_id, course_id, grade) VALUES (2, 2, 87);

-- Grades for Omer
INSERT INTO Grades (student_id, course_id, grade) VALUES (3, 1, 90);
INSERT INTO Grades (student_id, course_id, grade) VALUES (3, 3, 66);
INSERT INTO Grades (student_id, course_id, grade) VALUES (3, 2, 74);

-- Grades for Jony
INSERT INTO Grades (student_id, course_id, grade) VALUES (4, 1, 100);
INSERT INTO Grades (student_id, course_id, grade) VALUES (4, 3, 100);
INSERT INTO Grades (student_id, course_id, grade) VALUES (4, 2, 100);