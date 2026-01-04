import sqlite3

DATABASE = "database.db"

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

# Create users table
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()
conn.close()
print("Database and users table created successfully!")




