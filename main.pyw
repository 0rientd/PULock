from class_tkinter import Application
from scan_drives import Class_Scan_Drives
from sql import sql_db as sql

def main():

    sql().connect()
    Class_Scan_Drives().scan_and_save_drives()
    Application()

if __name__ == "__main__":
    main()