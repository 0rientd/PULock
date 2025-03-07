from lib.class_get_serial import GetSerialUSB
from lib.sql import sql_db as sql
from time import sleep
import ctypes

def scan_to_lock():
    serial_list = GetSerialUSB().init()
    all_table = sql().get_table()
    all_table.pop()

    for usb in all_table:
        if usb[3] == 1:
            if usb[2] not in serial_list:
                ctypes.windll.user32.LockWorkStation()
            elif usb[2] in serial_list:
                print(f"Usb key connected | Key used => {usb[2]}")
                pass
            else:
                print("Something wrong happened")
        else:
            print(f"Serial {usb[2]} has found but is not activated")

    sleep(1)
    scan_to_lock()

scan_to_lock()