import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i}0", 1000))

cursor.execute('''
UPDATE Users SET balance = 500 WHERE id % 2 = 1
''')

cursor.execute('''
DELETE FROM Users WHERE id % 3 = 1
''')

cursor.execute('''
SELECT username, email, age, balance FROM Users WHERE age != 60
''')


results = cursor.fetchall()
for username, email, age, balance in results:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')



connection.commit()
connection.close()