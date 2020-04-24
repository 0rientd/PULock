import sqlite3
from pathlib import Path
connection = sqlite3.connect("PULock.db")

class sql_db():
    def __init__(self):
        pass

    def connect(self):
        try:
            connection = sqlite3.connect("PULock.db")
            print("Conectado com sucesso!")
            return connection

        except:
            print("Não pode se conectar ao banco de dados")

    def create_table(self, con):
        cursor = con.cursor()
        cursor.execute("CREATE TABLE usbs(id integer PRIMARY KEY, model text, serial text, activate integer)")
        con.commit()

    def insert(self, id, modelo, serial):
        con = self.connect()
        cursor = con.cursor()

        cursor.execute(f"INSERT INTO usbs VALUES({id}, '{modelo}', '{serial}', 0)")
        con.commit()

        print("Valores inseridos no banco de dados")

