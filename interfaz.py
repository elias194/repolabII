"""
from customtkinter import *

root = CTk()
root.geometry("1024x768")
root.config(background="#000000")
set_appearance_mode("dark")

label = CTkLabel(master=root)



root.mainloop() """

import customtkinter as tk

class MyApp(tk.Application):
    def create_widgets(self):
        self.button = tk.Button(self, text="Abrir ventana", command=self.open_window)
        self.button.pack()

    def open_window(self):
        second_window = tk.Toplevel(self)
        second_window.title("Segunda ventana")
        label = tk.Label(second_window, text="Esta es otra ventana")
        label.pack()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
