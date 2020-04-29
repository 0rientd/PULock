import tkinter as tk
from lib.sql import sql_db as sql
from lib.scan_drives import Class_Scan_Drives

Class_Scan_Drives().scan_and_save_drives()
background = "#F7F5D0"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        usb_list = sql().get_table()
        usb_list.pop()

        for usbs in usb_list:
            usbs = list(usbs)
            self.create_widgets(usbs)

        self.label = tk.Label(self, text="GREEN is activated and RED is deactivated",
                              font=("Calibri", "9"), bg=background, fg="#CB5BFF")
        self.label.pack(side="bottom")

        self.quit = tk.Button(self, text="SAIR", fg="#49B3D1", font=("Calibri", "11", "bold"), bg="#D2D2D2",
                              command=self.master.quit)
        self.quit.pack(side="bottom", pady=50)

    def create_widgets(self, usbs):
        button = tk.Button(self, font=("Calibri", "11", "bold"), bd=5, padx=65)

        if usbs[3] == 1:
            button["fg"] = "#3DCD67"
        else:
            button["fg"] = "#E93737"

        button["text"] = usbs[1]
        button["command"] = lambda: [button.destroy(), self.create_widgets(self.button_action(usbs))]

        button.pack(pady=3)

    def button_action(self, usb):
        print(f"Updating status of model => {usb[1]} with serial {usb[2]}")
        usb[3] = sql().update_status_usb(usb)

        return usb

root = tk.Tk()
root.configure(background = background)

app = Application(master=root)
app.configure(background = background)
app.master.title("PULock")
app.master.minsize(400, 250)

app.mainloop()