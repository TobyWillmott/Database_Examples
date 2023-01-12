# write_to_student_db.py
import sqlite3
from faker import Faker
import random

# Create a connection to the database
conn = sqlite3.connect("student.sqlite")

# Create a cursor
cursor = conn.cursor()

# Example - adding a user to the students table
insert_query = """ 
INSERT INTO  
    students (firstname, lastname, age, gender) 
VALUES 
    ('Hermione', 'Grainger', 14, 'female'); 
"""
cursor.execute(insert_query)
conn.commit()

# Example - parameterized query
parameterised_insert_query = """ 
INSERT INTO  
    students (firstname, lastname, age, gender) 
VALUES 
    (?, ?, ?, ?); 
"""
cursor.execute(parameterised_insert_query, ('Harry', 'Potter', 13, 'male'))

# The Faker module gives a way of creating random data
fake = Faker('en_GB')
random.seed(4321)
fake.random.seed(4321)
for _ in range(10):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11, 18)
    gender = random.choice(('male', 'female'))
    cursor.execute(parameterised_insert_query,
                   (f_name, l_name, age, gender))
conn.commit()

# Another way of doing a parameterized query
data = [(fake.first_name(),
         fake.last_name(),
         random.randint(11, 18),
         random.choice(('male', 'female')))
        for _ in range(5)]
cursor.executemany(parameterised_insert_query, data)
conn.commit()

# Updating a record
update_query = """ 
UPDATE students 
SET lastname = ? 
WHERE id = 4; 
"""
cursor.execute(update_query, ('Potter',))
conn.commit()