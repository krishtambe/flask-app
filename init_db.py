import os
import sqlite3

# Get the current directory of the script
current_dir = os.path.dirname(__file__)
schema_path = os.path.join(current_dir, 'schema.sql')

# Connect to the database
connection = sqlite3.connect('database.db')

# Open and execute the schema file
with open(schema_path) as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insert sample posts
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
