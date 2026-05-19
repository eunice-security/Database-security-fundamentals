import sqlite3


# connect to database
conn = sqlite3.connect("people.db")
cursor = conn.cursor()

# remove users table if it already exists
cursor.execute("DROP TABLE IF EXISTS users")

# create users table
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    auth_level INTEGER
)
""")

# save and close
conn.commit()
conn.close()

print("people.db and users table created successfully.")
