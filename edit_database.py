import sqlite3

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

# Updating a record
update_query = """ 
UPDATE students 
SET lastname = ? 
WHERE id = 4; 
"""
cursor.execute(update_query, ('Potter',))
conn.commit()