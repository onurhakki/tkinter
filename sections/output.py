import customtkinter
from utils.common import set_grid_weights
from tkinter import filedialog


class OutputSection(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master, corner_radius=50)
        set_grid_weights(self, {0: 1, 1: 4, 2: 4, 3: 1}, pos="col")
        set_grid_weights(self, {0: 1, 1: 1, 2: 7, 3: 1}, pos="row")

        self.textbox = customtkinter.CTkTextbox(
            self
            , state="disabled"
            )
        self.textbox.grid(row=2, column=1, columnspan=2,
                          sticky="nsew", padx=20, pady=10)
        customtkinter.CTkLabel(self, text="İşlemler").grid(row=1, column=1)
        customtkinter.CTkButton(
            self, text="İşlem Yap", command= lambda: self._EntryAddValue("assdfsd")).grid(row=1, column=2)
        #self.status_label = customtkinter.CTkLabel(
        #    self, text="Dosya Yüklenmedi")
        #self.status_label.grid(row=2, column=1, columnspan=2)
        #self.status = False

    def _EntryAddValue(self, text):
        self.textbox.configure(state = "normal")
        self.textbox.insert(customtkinter.END, text+"\n")
        self.textbox.configure(state = "disabled")


    def _ButtonPress(self):
        #self.textbox.delete(0,"end")
        self.textbox.configure(state = "normal")
        self.textbox.insert(customtkinter.END,"asdasdasdasd\n")
        self.textbox.configure(state = "disabled")
