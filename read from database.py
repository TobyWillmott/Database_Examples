import sqlite3
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """
SELECT  id, firstname, lastname
FROM students
WHERE age>= 15
"""

cursor.execute(select_students)
first_students = cursor.fetchone()
more_students = cursor.fetchmany(12)
other_students = cursor.fetchall()

print(first_students)
print(more_students)
print(other_students)




