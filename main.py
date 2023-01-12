import sqlite3

# create a connection to a database - if one does not exist, a new one will be created
conn = sq = sqlite3.connect("student.sqlite")

# a cursor is a pointer to a place in the database which allows access
# to a table row-by-row
cursor = conn.cursor()

# SQL commands can be written as text and then "run" using an execute command
# Example - creating a table
create_students_table = """
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL, 
    lastname TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);
"""

cursor.execute(create_students_table)

conn.close()
