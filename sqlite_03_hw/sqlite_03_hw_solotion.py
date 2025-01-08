import sqlite3, os

file_name = 'sqlite_03_hw_db.db'

# checking for file existence
if os.path.exists(file_name):
    os.remove(file_name)
    print(f'File {file_name} has beeb deleted')
else:
    print('File do not exist')

# ---------- SQL ----------
conn = sqlite3.connect(file_name)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# ---------- Query's ----------

# creates table
cursor.execute("""
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
INTEGER);
""")

# inserts values
cursor.execute("""INSERT INTO shopping VALUES (1, 'Avokado', 5);""")
cursor.execute("""INSERT INTO shopping VALUES (2, 'Milk', 2);""")
cursor.execute("""INSERT INTO shopping VALUES (3, 'Bread', 3);""")
cursor.execute("""INSERT INTO shopping VALUES (4, 'Chocolate', 8);""")
cursor.execute("""INSERT INTO shopping VALUES (5, 'Bamba', 5);""")
cursor.execute("""INSERT INTO shopping VALUES (6, 'Orange', 10);""")

# printing the data
cursor.execute("""SELECT * FROM shopping""")

cursor.execute("""SELECT * FROM shopping WHERE amount > 5""")

# deleting row from 'shopping'
cursor.execute("""DELETE from shopping WHERE name like 'Orange';""")

# updates the table
cursor.execute("""UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'""")

cursor.execute("""UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'""")

# counting all from shopping
cursor.execute("""SELECT COUNT(*)from shopping""")

# printing all where id bigger than 0 - will print all the .db
cursor.execute("""SELECT * FROM shopping WHERE id > 0""")

# fetching all data from the db to result list and printing it
rows = cursor.fetchall()
result = [tuple(row) for row in rows]
print(result)

conn.commit()
conn.close()

print(f"All changes are saved and file {file_name} created")

# End
