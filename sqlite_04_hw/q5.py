import sqlite3

file_name = "sqlite_04_hw_db.db" # file name

conn = sqlite3.connect(file_name) # connection to the db
conn.row_factory = sqlite3.Row # allows to use column row
cursor = conn.cursor() # creating a cursor

query = "SELECT * FROM Courses"

# ---Query for fetching data---
cursor.execute(query)
rows = cursor.fetchall()
result = [dict(row) for row in rows]

# ---Input from the user---
course_name: str = input("What's the course name? ").capitalize()
hours: int = int(input("What's the length of the course by hours? "))

# ---Run on result to check for each topic in db---
in_result = True # Flag to check is there is the topic or not
for i in result:
    if i['topic'] == course_name:
        in_result = False
# ---Commiting change if not in db---
if in_result:
    query2 = "INSERT INTO Courses (topic, hours) VALUES (?, ?)"
    cursor.execute(query2, (course_name, hours))
    print("The topic added successfully")
    conn.commit()
    conn.close()
# ---Raise error if in db---
else:
    raise ValueError("The topic already exist")
# End