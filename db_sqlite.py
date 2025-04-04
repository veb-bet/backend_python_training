import sqlite3
# Подключение к базе данных
conn = sqlite3.connect('users.db')
# Создание таблицы
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT);''')
# Вставка данных
conn.execute("INSERT INTO users (name, age, email) VALUES ('Alice', 25, 'alice@example.com');")
# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()