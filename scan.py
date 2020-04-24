from class_get_serial import GetSerialUSB
from time import sleep
import ctypes

def scan_to_lock():
    _lock = False
    lista_de_serial = GetSerialUSB().init()
    if "2011020600004351" not in lista_de_serial:
        lock = True
        print(lock)
        ctypes.windll.user32.LockWorkStation()

    sleep(1)
    scan_to_lock()

def scan_to_unlock():
    _lock = True
    lista_de_serial = GetSerialUSB().init()
    if "2011020600004351" in lista_de_serial:
        lock = False
        print(lock)
        scan_to_lock()

    sleep(1)
    scan_to_unlock()

scan_to_lock()