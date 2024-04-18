# 3.3.2 Working with Databases: Advanced Python

# MySQL and PostgreSQL:

# For MySQL and PostgreSQL databases, you can use third-party libraries such as mysql-connector-python and psycopg2 respectively.

# Example: Working with MySQL (using mysql-connector-python)
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname"
)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
