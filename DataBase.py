import sqlite3

#создаем подключение к БД
connection = sqlite3.connect('Password_db.db')
cursor = connection.cursor()

#создаем таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS Passwords(
Id_user INTEGER PRIMARY KEY,
Login TEXT NOT NULL,
Password TEXT NOT NULL 
)
""")

#сохраняем и закрываем
connection.commit()
connection.close()
