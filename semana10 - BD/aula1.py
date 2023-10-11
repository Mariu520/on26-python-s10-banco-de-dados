

import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor ()

cursor.execute ("CREATE TABLE pessoas (nome text, idade interger, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Amora', 34, 'amora1988@gmail.com')")

cursor.execute("INSERT INTO pessoas VALUES ('Joana', 44, 'joana1988@gmail.com')")

cursor.execute("INSERT INTO pessoas VALUES ('Karina', 45, 'karina1988@gmail.com')")

banco.commit ()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall ())















#cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

##""" cursor.execute("INSERT INTO pessoas VALUES ('Alguem' , 20, 'teste@email.com')")

##banco.commit() """

##cursor.execute("SELECT * FROM pessoas")

##print(cursor.fetchall())
