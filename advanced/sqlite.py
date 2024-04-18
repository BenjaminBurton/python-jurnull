# 3.3.1 Working with Databases: Advanced Python

# SQLite:

# SQLite is a lightweight, serverless, self-contained SQL database engine. Python comes with built-in support for SQLite through the sqlite3 module.

# Example: Working with SQLite
import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))

# Commit the transaction
conn.commit()

# Fetch data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
