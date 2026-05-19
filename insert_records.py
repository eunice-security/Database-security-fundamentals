import sqlite3
from users import users_data

# connect to database
conn = sqlite3.connect("people.db")
cursor = conn.cursor()

# insert each user record
for user in users_data:
    cursor.execute("""
        INSERT INTO users (user_id, username, password, auth_level)
        VALUES (?, ?, ?, ?)
    """, (
        user["user_id"],
        str(user["username"]),
        str(user["password"]),
        user["auth_level"]
    ))

# save and close
conn.commit()
conn.close()

print("All user records inserted successfully.")
