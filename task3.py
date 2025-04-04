import sqlite3
conn = sqlite3.connect('users.db')
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT);''')

conn.close()