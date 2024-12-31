CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    building TEXT NOT NULL,
    budget INTEGER DEFAULT 100000
);

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    salary REAL NOT NULL,
    seniority INTEGER NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);