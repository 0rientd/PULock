import sqlite3
from pathlib import Path

class sql_db():
    def __init__(self):
        pass

    def connect(self):

        my_db = Path("PULock.db")
        if my_db.is_file():
            print("Banco de dados encontrado")
            pass

        else:
            print("Criando arquivo de banco de dados")
            con = sqlite3.connect("PULock.db")
            print("Criado DB com sucesso")
            self.create_table(con)

        try:
            print("Conectando ao banco..")
            con = sqlite3.connect("PULock.db")
            print("Conectado com sucesso!")
            return con

        except:
            print("Não pode se conectar ao banco de dados")

    def create_table(self, con):
        cursor = con.cursor()
        cursor.execute("CREATE TABLE usbs(id integer PRIMARY KEY, model text, serial text, activate integer)")
        cursor.execute("INSERT INTO usbs VALUES(9999, 'IGNORE', 'IGNORE', 0)")
        con.commit()

        print("Criado entidade modelo com sucesso")

    def verificar_ids(self):
        count = 0
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('SELECT id FROM usbs')
        linhas = cursor.fetchall()
        for count in range(0, len(linhas)):
            print("Quantidade de IDS => ", count)

        return count

    def verificar_serial(self):
        count = 0
        lista_de_seriais = []
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('SELECT serial FROM usbs')
        serials = cursor.fetchall()

        for serial in serials:
            print("verificar_serial => Verificando o serial => ", serial)
            lista_de_seriais.append(serial[count])

        return lista_de_seriais

    def insert(self, id, modelo, serial):
        con = self.connect()
        cursor = con.cursor()

        if id == 0 or id == '0':
            id = int(id)
            id = id + 1

        ids_from_table = self.verificar_ids()
        lista_de_seriais = self.verificar_serial()

        for count in range(0, len(lista_de_seriais)):
            if serial in lista_de_seriais:
                print("==============", "ENCONTRADO E PULANDO SERIAL", serial, "============")
                pass

            else:
                print("SERIAL NÃO ENCONTRADO")
                try:
                    id_a_adicionar = id + ids_from_table
                    print("Adicionando id ", id_a_adicionar, "Modelo => ", modelo, "Com serial ", serial)
                    cursor.execute(f"INSERT INTO usbs VALUES({id_a_adicionar}, '{modelo}', '{serial}', 0)")
                    con.commit()

                    print("Valores inseridos no banco de dados")

                except:
                    pass