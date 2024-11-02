import sqlite3

connect = sqlite3.connect('not_telegram.db')
curs = connect.cursor()

create_db = ('CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY,'
             'username TEXT NOT NULL,'
             'email TEXT NOT NULL,'
             'age INTEGER,'
             'balance INTEGER NOT NULL)')
curs.execute(create_db)

# for i in range(1, 11):
#     curs.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
#                  (f'User{i}', f'example{i}@gmail.com', i*10, i*1000))

# curs.execute('SELECT id FROM Users')
# b = True
# for x in curs.fetchall():
#     if b:
#         curs.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, x[0]))
#         b = False
#     else:
#         b = True

# curs.execute('SELECT id FROM Users')
# b = 1
# for x in curs.fetchall():
#     if b == 3:
#         curs.execute('DELETE FROM Users WHERE id = ?', (x[0],))
#         b = 1
#     else:
#         b += 1

curs.execute('SELECT * FROM Users WHERE age != ?', (50, ))

for x in curs.fetchall():
    print(f'Имя: {x[1]} | Почта: {x[2]} | Возраст: {x[3]} | Баланс: {x[4]}')

connect.commit()
connect.close()



