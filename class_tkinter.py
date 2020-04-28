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

        self.texto = tk.Label(self, text="GREEN is activated and RED is deactivated",
                              font=("Calibri", "8", "bold"), bg="#61656E", fg="purple")
        self.texto.pack(side="bottom")

        self.quit = tk.Button(self, text="SAIR", fg="cyan", command=self.master.quit)
        self.quit["font"] = ("Calibri", "11", "bold")
        self.quit["bg"] = "grey"
        self.quit.pack(side="bottom", pady=50)

    def create_widgets(self, usbs):
        btn = tk.Button(self)
        if usbs[3] == 1:
            btn["fg"] = "green"
        else:
            btn["fg"] = "red"
        btn["text"] = usbs[1]
        btn["command"] = lambda: [btn.destroy(), self.create_widgets(self.acao_botao(usbs))]
        btn["font"] = ("Calibri", "11", "bold")
        btn["bd"] = 5
        btn["padx"] = 65

        btn.pack(pady=3)

    def acao_botao(self, usb):
        print(f"Atualizando status do modelo => {usb[1]} com serial {usb[2]}")
        usb[3] = sql().update_status_usb(usb)

        return usb

root = tk.Tk()
root.configure(background = '#61656E')
app = Application(master=root)
app.configure(background = '#61656E')
app.master.title("PULock")
app.master.minsize(400, 250)

app.mainloop()