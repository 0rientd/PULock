import tkinter as tk
from sql import sql_db as sql

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        index = 0
        lista_de_usbs = sql().get_table()
        lista_de_usbs.pop()
        for usbs in lista_de_usbs:
            list(usbs)
            cada_drive = [index, usbs]
            self.create_widgets(cada_drive)

            index = index + 1

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_widgets(self, usbs):
        btn = tk.Button(self)
        btn["text"] = usbs[1][1]
        btn["command"] = lambda:[btn.destroy(), self.create_widgets(self.acao_botao(usbs))]

        btn.pack()

    def acao_botao(self, usb):
        print(f"Atualizando status do modelo => {usb[1][1]} com serial {usb[1][2]}")
        ativo = sql().update_status_usb(usb[1])

        novos_dados = [usb[0], (usb[1][0], usb[1][1], usb[1][2], ativo)]
        return novos_dados

root = tk.Tk()
app = Application(master=root)
app.master.title("PULock")
app.master.minsize(400, 250)
app.mainloop()