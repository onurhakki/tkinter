import customtkinter
from utils.common import set_grid_weights


class LoginSection(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master, corner_radius=50)

        set_grid_weights(self, {
                         0: 2, 1: 3, 2: 3, 3: 3, 4: 1,5: 2,}, pos="col")
        set_grid_weights(self, {
                         0: 1, 1: 3, 2: 3, 3: 1, 4: 1}, pos="row")

        customtkinter.CTkLabel(
            self, text="Username:").grid(row=1, column=1)
        customtkinter.CTkLabel(
            self, text="Password:").grid(row=2, column=1)

        self.password_variable = customtkinter.StringVar(self)
        self.combobox_username = customtkinter.CTkComboBox(
            self, values=["OEYUBOGLU", "AGUNGOR"], state="readonly")
        self.combobox_username.set("OEYUBOGLU")
        self.combobox_username.grid(row=1, column=2)

        self.password_variable = customtkinter.StringVar(self)
        self.password_box = customtkinter.CTkEntry(
            self, insertontime=0, textvariable=self.password_variable)

        self.password_box.bind("<ButtonPress-1>", self._EntryPress)
        self.password_box.bind("<Return>", self._ButtonPressEnter)
        self.password_box.bind("<Leave>", self._EntryLeave)
        self.password_box.grid(row=2, column=2)

        self.login_button = customtkinter.CTkButton(
            self, command=self._ButtonPress)
        self.login_button.grid(row=1, column=4, rowspan=2)
        self.status = customtkinter.CTkLabel(
            self, text="Giriş yapılması bekleniyor")
        self.status.grid(row=3, column=1,  columnspan=4)

        self.checkbox = customtkinter.CTkCheckBox(
            self, text="", onvalue=1, offvalue=0, command=self._CheckBoxPasswordShow)
#        (self, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
        self.checkbox.grid(row=2, column=3)

    def _CheckBoxPasswordShow(self):
        val = self.checkbox.get()
        if val == 1:
            self.password_box.configure(show="")
        if val == 0:
            self.password_box.configure(show="*")


    def _ButtonPressEnter(self, event):
        print(self.password_variable.get())
        password = self.password_variable.get()
        # Duruma göre güncellemelisin
        self.status.configure(text=password + self.combobox_username.get())

    def _ButtonPress(self):
        print(self.password_variable.get())
        password = self.password_variable.get()
        # Duruma göre güncellemelisin
        self.status.configure(text=password + self.combobox_username.get())

    def _EntryPress(self, event):
        self.password_box.configure(show="*", insertontime=600)

    def _EntryLeave(self, event):
        self.password_box.configure(insertontime=0)
