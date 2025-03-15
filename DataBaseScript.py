import sqlite3

def Find_password(Login):
    connection = sqlite3.connect('Password_db.db')
    cursor = connection.cursor()

    #скл запрос
    try:
        cursor.execute(f"")
    except:
        print('Запрос не обработался по причине - ', Exception)

    # сохраняем и закрываем
    connection.commit()
    connection.close()

def INSERT():
    connection = sqlite3.connect('Password_db.db')
    cursor = connection.cursor()
    for i in range(1, 5):

        #ввод данных пользователя

        Login = input("Введите логин - ")
        Password = int(input("Введите пароль - "))


        #занесение в таблицу
        try:
            #cursor.execute(f"""INSERT INTO Passwords (id_user, login, Password) VALUES ({i}, '{Login}', '{Password}')""")
            cursor.execute(f"""UPDATE  Passwords SET login='{Login}', Password={Password} 
                                WHERE id_user={i}""")
        except:
            print("Ошибка2 - ", repr(Exception))

    cursor.execute("""SELECT * FROM Passwords""")
    all = cursor.fetchall()

    # Выводим результаты
    for atribut in all:
        dict = {
            'Id_user': atribut[0],
            'Login': atribut[1],
            'Password': atribut[2]
        }
        print(dict['Id_user'], ' ', dict['Login'], ' ', dict['Password'])

    connection.commit()
    connection.close()

def select():
    connection = sqlite3.connect('Password_db.db')
    cursor = connection.cursor()

    i = input('Ваш логин - ')

    #поиск пороля по логину
    cursor.execute(f"""SELECT Passwords.Password FROM Passwords WHERE Passwords.Login = '{i}' """)
    print(cursor.fetchall())
    connection.commit()
    connection.close()

if __name__ == '__main__':
    select()