import tkinter as tk
from class_get_model import GetModelUSB
from class_get_serial import GetSerialUSB
from sql import sql_db as sql

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        index = 0
        lista_de_usbs = GetModelUSB().init()
        for usbs in lista_de_usbs:
            self.usb = tk.Button(self)
            self.usb["text"] = usbs
            cada_drive = [index, usbs]
            self.usb["command"] = lambda lusb = cada_drive: self.acao_botao(lusb)
            self.usb.pack(side="top")
            index = index + 1

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def acao_botao(self, model_usb):
        lista_serial_USB = GetSerialUSB().init()
        print(model_usb, lista_serial_USB[model_usb[0]])

        print(f"Inserindo {model_usb[0]}, {model_usb[1]}, {lista_serial_USB[model_usb[0]]}")
        sql().insert(model_usb[0], model_usb[1], lista_serial_USB[model_usb[0]])


root = tk.Tk()
app = Application(master=root)
app.master.title("PULock")
app.master.minsize(400, 250)
app.mainloop()