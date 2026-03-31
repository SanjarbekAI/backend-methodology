# Bug count: ? (find them all)
# Topic: psycopg2 connection, parameterized queries, cursor, commit
# Give after: L05
#
# Scenario: A student registration script that connects to PostgreSQL,
#           creates a table, inserts students, and fetches them back.
#
# Expected output:
#   Table created.
#   Inserted: Sardor Toshev (sardor@mail.com)
#   Inserted: Nilufar Karimova (nilufar@mail.com)
#   Inserted: Aziz Rahimov (aziz@mail.com)
#   All students:
#     1 | Sardor Toshev    | sardor@mail.com  | Tashkent
#     2 | Nilufar Karimova | nilufar@mail.com | Samarkand
#     3 | Aziz Rahimov     | aziz@mail.com    | Bukhara
#   Students from Tashkent:
#     Sardor Toshev

import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()  # BUG — should use RealDictCursor for dict-style access later

# Create table
cursor.execute("""
    DROP TABLE IF EXISTS students;
    CREATE TABLE students (
        id        SERIAL PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        email     VARCHAR(150) UNIQUE NOT NULL,
        city      VARCHAR(50)
    )
""")
conn.commit()
print("Table created.")

# Insert students using parameterized queries
students = [
    ("Sardor Toshev",    "sardor@mail.com",  "Tashkent"),
    ("Nilufar Karimova", "nilufar@mail.com", "Samarkand"),
    ("Aziz Rahimov",     "aziz@mail.com",    "Bukhara"),
]

for student in students:
    cursor.execute(
        "INSERT INTO students (full_name, email, city) VALUES (%s, %s, %s) RETURNING full_name, email",
        student
    )
    row = cursor.fetchone()
    print(f"Inserted: {row[0]} ({row[1]})")
# BUG — missing conn.commit() after inserts

# Fetch all students
cursor.execute("SELECT * FROM students ORDER BY id")
rows = cursor.fetchall()
print("All students:")
for row in rows:
    print(f"  {row['id']} | {row['full_name']:<16} | {row['email']:<16} | {row['city']}")
# BUG — cursor was not created as RealDictCursor so row['id'] won't work

# Fetch students from a specific city using parameterized query
city = "Tashkent"
cursor.execute("SELECT full_name FROM students WHERE city = %s", city)  # BUG — params must be a tuple
rows = cursor.fetchall()
print("Students from Tashkent:")
for row in rows:
    print(f"  {row['full_name']}")

cursor.close()
conn.close()

