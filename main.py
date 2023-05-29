import tkinter
import tkinter.messagebox
import customtkinter

from sections.login import LoginSection
from sections.upload import UploadSection
from sections.output import OutputSection

from utils.common import set_grid_weights
import ctypes

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self, information):
        super().__init__()

        self.scale = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

        width = self.winfo_screenwidth()*0.5
        height = self.winfo_screenheight()*0.8
        x = self.winfo_screenwidth()*0.5*self.scale
        y = 0

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        for k,v in information.items():
            getattr(self,k)(v)


        set_grid_weights(self, {0: 1, 1: 5, 2: 5, 3: 5, 4:5, 5:1}, pos = "row")
        set_grid_weights(self, {0: 1, 1: 5, 2: 5, 3: 5, 4:5, 5:1}, pos = "col")

        self.loginSection = LoginSection(self)
        self.loginSection.grid(
            row=1, column=1, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        self.uploadSection = UploadSection(self)
        self.uploadSection.grid(
            row=2, column=1, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        
        self.outputSection = OutputSection(self)
        self.outputSection.grid(
            row=3, column=1, columnspan=2, rowspan=2, sticky="nsew", padx=5, pady=5)
        self.outputSection2 = OutputSection(self)
        self.outputSection2.grid(
            row=3, column=3, columnspan=2, rowspan=2, sticky="nsew", padx=5, pady=5)
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


information = {"title": "App Title"}

if __name__ == "__main__":
    app = App(information)
    app.mainloop()
