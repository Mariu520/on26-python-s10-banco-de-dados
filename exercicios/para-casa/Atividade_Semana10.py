import sqlite3
import csv

relacao_aeroporto = sqlite3.connect("disponibilidade_pets.db")
cursor = relacao_aeroporto.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tabelas_pets(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Zip INT,
                City TEXT,
                State TEXT,
                Division TEXT,
                Parking YES,
                Pets YES,
                Food YES
                Lounge YES)''')

file = open("Airport-Pets.csv")

conteudo = csv.reader(file)
inserir_conteudo = "INSERT INTO AIPORT-PETS (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

select_all = "SELECT * FROM tabelas_pets" # selecionando tudo da tabela pet(select_all)
enter = cursor.execute(select_all).fetchall()

relacao_aeroporto.commit()
relacao_aeroporto.close()
  
#função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
    relacao_aeroporto = sqlite3.connect('tabelas_pets.db') 
    cursor = relacao_aeroporto.cursor()  

    atualizar_conteudo = f"UPDATE tabelas_pets SET {campo} = ? WHERE id = ?"
    
    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    
#     # Salva as alterações no banco de dados.
relacao_aeroporto .commit()
relacao_aeroporto.close()
    
# #chamando a função para atualizar os dados
atualizar_dado(1, 'Y', 'Pets')
relacao_aeroporto.close()