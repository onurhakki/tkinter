import customtkinter
from utils.common import set_grid_weights
from tkinter import filedialog


class UploadSection(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master, corner_radius=50)
        set_grid_weights(self, {
                         0: 1, 1: 3, 2: 3, 3: 1}, pos="col")
        set_grid_weights(self, {
                         0: 1, 1: 3, 2: 3, 3: 1}, pos="row")

        self.search_file_button = customtkinter.CTkButton(
            self, text = "Dosya Yükle", command=self._ButtonPress)
        self.search_file_button.grid(row=1, column=1, columnspan=2)
        self.status_label = customtkinter.CTkLabel(
            self, text="Dosya Yüklenmedi")
        self.status_label.grid(row=2, column=1, columnspan=2)
        self.status = False

    def _ButtonPress(self):
        self.search_file_path = filedialog.askdirectory(title="Dosya Seçiniz")
        if self.search_file_path == "":
            self.status = False
            self.status_label.configure(text="Dosya Yüklenmedi")
        else:
            self.status = True
            self.status_label.configure(text=self.search_file_path)
        print("button pressed")
        print(self.status)

