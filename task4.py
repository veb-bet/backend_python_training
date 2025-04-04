import sqlite3
def add_user(name, age, email):
    conn = sqlite3.connect('users.db')
    conn.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    conn.close()
def get_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.execute("SELECT * FROM users")
    for row in cursor:
        print(row)
    conn.close()
# Добавление нового пользователя
add_user("Alice", 25, "alice@example.com")
# Вывод всех пользователей
get_all_users()