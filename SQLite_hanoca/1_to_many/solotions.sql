-- 15. 
SELECT Employees.name AS employee_name, Departments.* FROM Departments
INNER JOIN Employees ON Departments.department_id = Employees.department_id;


-- 16. 
SELECT Employees.name AS employee_name, Departments.name FROM Employees
LEFT JOIN Departments ON Departments.department_id = Employees.department_id;


-- 17. 
SELECT Employees.name, Departments.name AS department FROM Employees
LEFT JOIN Departments ON Departments.department_id = Employees.department_id
WHERE Employees.department_id IS NULL;


-- 18. 
-- from building
SELECT Departments.building, count(employee_id) AS total_employees FROM Employees
LEFT JOIN Departments ON Departments.department_id = Employees.department_id
GROUP BY Departments.building;

-- from Department
SELECT Departments.name AS department, count(employee_id) AS total_employees FROM Employees
LEFT JOIN Departments ON Departments.department_id = Employees.department_id
GROUP BY Departments.name;


-- 19. 
SELECT avg(Employees.salary) AS average, Departments.name AS department FROM Departments
LEFT JOIN Employees ON Departments.department_id = Employees.department_id
GROUP BY Departments.name;



-- 20. 
SELECT Employees.name AS worker_name, max(Employees.salary) AS max_salary, Departments.name AS department
FROM Employees
LEFT JOIN Departments ON Departments.department_id = Employees.department_id;
GROUP BY Departments.name;


-- 21. 
SELECT Employees.name AS employee_name, Employees.seniority AS seniority, Departments.name AS department
FROM Employees
LEFT JOIN Departments ON Departments.department_id = Employees.department_id
ORDER BY seniority;


-- 22. 
-- used round eve if not learned yet just to make the output good looking - 
-- the problame was that avg() can't take 2 arguments, so i found a different way to make this
SELECT seniority, ROUND(avg(salary), 2) AS average_salary FROM Employees
GROUP BY Employees.seniority;


-- 23. 
-- a. 
ALTER TABLE Departments ADD COLUMN total_employees_per_department INTEGER DEFAULT 0;
ALTER TABLE Departments ADD COLUMN total_average_per_department INTEGER DEFAULT 0;
ALTER TABLE Departments ADD COLUMN max_salary INTEGER DEFAULT 0;
ALTER TABLE Departments ADD COLUMN average_seniority INTEGER DEFAULT 0;

-- -- b. 
UPDATE Departments
SET total_employees_per_department = (
SELECT count(Employees.department_id) FROM Employees
WHERE Employees.department_id = Departments.department_id
);

UPDATE Departments
SET total_average_per_department = (
SELECT avg(Employees.salary) FROM Employees
WHERE Employees.department_id = Departments.department_id
);

UPDATE Departments
SET max_salary = (
SELECT max(Employees.salary) FROM Employees
WHERE Employees.department_id = Departments.department_id
);

UPDATE Departments
SET average_seniority = (
SELECT avg(Employees.seniority) FROM Employees
WHERE Employees.department_id = Departments.department_id
);