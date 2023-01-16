import sqlite3
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """
SELECT *
FROM students
WHERE firstname LIKE "J%"
"""

group_by_query = """
SELECT gender, COUNT(*)
FROM students
GROUP BY gender
"""

sum_by_name = """
SELECT SUBSTR(firstname,1,1) ,sum(age)
from students
GROUP BY SUBSTR(firstname,1,1)
"""

cursor.execute(select_students)
students = cursor.fetchmany(5)
print(students)

students_by_gender = cursor.execute(group_by_query).fetchall()
print(students_by_gender)

students_by_letter = cursor.execute(sum_by_name).fetchall()
print(students_by_letter)