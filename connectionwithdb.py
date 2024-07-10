import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('mydb.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, 
                   name TEXT, 
                   age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Commit the changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Initial data:")
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE users SET age = 28 WHERE name = 'Alice'")
conn.commit()

# Query updated data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("After update:")
for row in rows:
    print(row)

# Delete data
cursor.execute("DELETE FROM users WHERE name = 'Bob'")
conn.commit()

# Query data after deletion
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("After deletion:")
for row in rows:
    print(row)

# Close the connection
conn.close()
