CREATE TABLE Lecturers (
    lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    UNIQUE(name)
);

CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lecturer_id INTEGER,
    UNIQUE(name),
    FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
);

INSERT INTO Lecturers (name) VALUES ('John Smith');
INSERT INTO Lecturers (name) VALUES ('Emily Johnson');
INSERT INTO Lecturers (name) VALUES ('Michael Brown');
INSERT INTO Lecturers (name) VALUES ('Sarah Davis');
INSERT INTO Lecturers (name) VALUES ('David Wilson');
INSERT INTO Lecturers (name) VALUES ('Jessica Taylor');
INSERT INTO Lecturers (name) VALUES ('Daniel Moore');
INSERT INTO Lecturers (name) VALUES ('Emma Anderson');
INSERT INTO Lecturers (name) VALUES ('Chris Thomas');
INSERT INTO Lecturers (name) VALUES ('Sophia Martinez');

INSERT INTO Courses (name, lecturer_id) VALUES ('Mathematics', 1);
INSERT INTO Courses (name, lecturer_id) VALUES ('Physics', 2);
INSERT INTO Courses (name, lecturer_id) VALUES ('Chemistry', 3);
INSERT INTO Courses (name, lecturer_id) VALUES ('Economics', 7);
INSERT INTO Courses (name, lecturer_id) VALUES ('Biology', 4);
INSERT INTO Courses (name, lecturer_id) VALUES ('Sociology', 10);
INSERT INTO Courses (name, lecturer_id) VALUES ('Art History', NULL);
INSERT INTO Courses (name, lecturer_id) VALUES ('Music Theory', NULL);
INSERT INTO Courses (name, lecturer_id) VALUES ('Philosophy', 8);
INSERT INTO Courses (name, lecturer_id) VALUES ('Environmental Studies', NULL);
INSERT INTO Courses (name, lecturer_id) VALUES ('Computer Science', 5);
INSERT INTO Courses (name, lecturer_id) VALUES ('Statistics', 6);
INSERT INTO Courses (name, lecturer_id) VALUES ('Psychology', 9);

SELECT * FROM Lecturers;
SELECT * FROM Courses;