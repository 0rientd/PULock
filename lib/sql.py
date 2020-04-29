import sqlite3
from pathlib import Path

class sql_db():
    def __init__(self):
        pass

    def connect(self):

        my_db = Path("PULock.db")
        if my_db.is_file():
            print("Database has found")
            pass

        else:
            print("Creating database")
            con = sqlite3.connect("PULock.db")
            print("Database created successful")
            self.create_table(con)

        try:
            print("Connecting in database..")
            con = sqlite3.connect("PULock.db")
            print("Connection successful")
            return con

        except:
            print("Can't connect in database :(")

    def create_table(self, con):
        cursor = con.cursor()
        cursor.execute("CREATE TABLE usbs(id integer PRIMARY KEY, model text, serial text, activate integer)")
        cursor.execute("INSERT INTO usbs VALUES(9999, 'IGNORE', 'IGNORE', 0)")
        con.commit()

        print("Created entity successful")

    def verify_ids(self):
        count = 0
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('SELECT id FROM usbs')
        linhas = cursor.fetchall()
        for count in range(0, len(linhas)):
            print("Numbers of IDS => ", count)

        return count

    def verify_serial(self):
        count = 0
        serial_list = []
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('SELECT serial FROM usbs')
        serials = cursor.fetchall()

        for serial in serials:
            print("verify_serial => Verifying serial => ", serial)
            serial_list.append(serial[count])

        return serial_list

    def insert(self, id, model, serial):
        con = self.connect()
        cursor = con.cursor()

        if id == 0 or id == '0':
            id = int(id)
            id = id + 1

        ids_from_table = self.verify_ids()
        serial_list = self.verify_serial()

        for count in range(0, len(serial_list)):
            if serial in serial_list:
                print("==============", "THIS SERIAL => ", serial, "HAS FOUND | SKIPPING", "============")
                break

            else:
                print("SERIAL NOT FOUND")
                try:
                    id_to_add = id + ids_from_table
                    print("Adding id ", id_to_add, "Model => ", model, "Serial ", serial)
                    cursor.execute(f"INSERT INTO usbs VALUES({id_to_add}, '{model}', '{serial}', 0)")
                    con.commit()

                    print("Insert has been successful")

                    break

                except:
                    print("Something wrong happened and returned the except")

    def get_table(self):
        table_list = []
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM usbs')
        usbs_table = cursor.fetchall()

        for usb in usbs_table:
            table_list.append(usb)

        return table_list

    def update_status_usb(self, usb):
        con = self.connect()
        cursor = con.cursor()

        if usb[3] == 0:
            usb[3] = 1
        elif usb[3] == 1:
            usb[3] = 0
        else:
            print("Ops...")

        cursor.execute(f"UPDATE usbs SET activate = {usb[3]} where id = {usb[0]}")
        con.commit()
        print(f"Changing the status to {usb[3]}")

        return usb[3]
