import tkinter as tk
from sql import sql_db as sql

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        lista_de_usbs = sql().get_table()
        lista_de_usbs.pop()
        for usbs in lista_de_usbs:
            usbs = list(usbs)
            self.create_widgets(usbs)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_widgets(self, usbs):
        btn = tk.Button(self)
        btn["text"] = usbs[1]
        btn["command"] = lambda: [btn.destroy(), self.create_widgets(self.acao_botao(usbs))]

        btn.pack()

    def acao_botao(self, usb):
        print(f"Atualizando status do modelo => {usb[1]} com serial {usb[2]}")
        usb[3] = sql().update_status_usb(usb)

        return usb

root = tk.Tk()
app = Application(master=root)
app.master.title("PULock")
app.master.minsize(400, 250)
app.mainloop()