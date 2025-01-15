import sqlite3

file_name = "sqlite_04_hw_db.db"

conn = sqlite3.connect(file_name)
conn.row_factory = sqlite3.Row # allow to use column row
cursor = conn.cursor()


# --- query ---
query = "SELECT * FROM Courses"

cursor.execute(query)

rows = cursor.fetchall()

result = [tuple(row) for row in rows]
print(result)

conn.commit()
conn.close()
# End