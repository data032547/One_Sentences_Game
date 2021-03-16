import tkinter as tk

class main_window():
    def __init__(self):
        self.main = tk.Tk()
        self.close_button()
        self.main.mainloop()

    def close_button(self):
        button = tk.Button(self.main)
        button["text"] = "Fenster schließen"
        button["command"] = self.__del__
        button.pack()

    def __del__(self):
        self.main.destroy()


main_window()
        
