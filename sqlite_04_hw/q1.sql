CREATE TABLE Courses (
	course_id INTEGER PRIMARY KEY AUTOINCREMENT, 
	topic TEXT NOT NULL, 
	hours INTEGER NOT NULL
);

CREATE TABLE Students (
	student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name TEXT NOT NULL, 
	email UNIQUE NOT NULL
);

CREATE TABLE Grades (
	student_id INTEGER NOT NULL, 
	course_id INTEGER NOT NULL, 
	grade INTEGER NOT NULL, 
	PRIMARY KEY (student_id, course_id)
	FOREIGN key (student_id) REFERENCES Students(student_id)
	FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
