from class_get_serial import GetSerialUSB
from sql import sql_db as sql
from time import sleep
import ctypes

def scan_to_lock():
    lista_de_serial = GetSerialUSB().init()
    all_table = sql().get_table()
    all_table.pop()

    for usb in all_table:
        if usb[3] == 1:
            if usb[2] not in lista_de_serial:
                ctypes.windll.user32.LockWorkStation()
            elif usb[2] in lista_de_serial:
                print(f"Usb chave conectado | Chave => {usb[2]}")
                pass
            else:
                print("Alguma coisa errada aconteceu 1")
        else:
            print(f"Serial {usb[2]} encontrado mas não ativo")

    sleep(1)
    scan_to_lock()

scan_to_lock()