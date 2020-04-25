from sql import sql_db as sql
from class_get_model import GetModelUSB
from class_get_serial import GetSerialUSB

class Class_Scan_Drives():
    def __init__(self):
        pass

    def scan_and_save_drives(self):
        models_usbs = GetModelUSB().init()
        serial_usbs = GetSerialUSB().init()

        for index_drive in range(0, len(models_usbs)):
            print(f"Inserindo usb modelo {models_usbs[index_drive]}, serial {serial_usbs[index_drive]} no banco de dados")
            sql().insert(index_drive, models_usbs[index_drive], serial_usbs[index_drive])