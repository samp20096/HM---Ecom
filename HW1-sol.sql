-- 1. 
SELECT exam_year, printf('%.2f', grade) AS average_grades FROM grades
GROUP BY exam_year;


--2. 
SELECT student_name, exam_year, avg(grade) AS average_per_student FROM grades
WHERE exam_year = 2024
GROUP BY student_name;


-- 3. 
SELECT exam_year, max(grade) AS max_grade, min(grade) AS min_grade FROM grades
GROUP BY exam_year;


-- 4. 
SELECT exam_year, subject_name, count(subject_name) AS count_subject_per_year FROM grades
GROUP BY subject_name;


-- 5. 
SELECT subject_name, avg(grade) AS above_85_avg FROM grades
GROUP BY subject_name
HAVING avg(grade) > 85;


-- 6. 
SELECT count(grade) AS count_grade_above_90, student_name FROM grades
GROUP BY student_name
HAVING grade > 90;

-- the question was not that understandable, did as I understood.
