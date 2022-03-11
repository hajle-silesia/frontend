from tkinter import *


class ApplicationWindow(Tk):
    __name = "Hajle Silesia Homebrewing System"

    def __init__(self):
        super().__init__()

        self.__icon_path = "./img/icon.png"

        self._set_component()

    @property
    def name(self):
        return self.__name

    def position_component(self):
        for component in self.winfo_children():
            component.position_component()

    def _set_component(self):
        self.__set_titlebar_icon()
        self.__set_title()
        self.__set_size()

    def __set_titlebar_icon(self):
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file=self.__icon_path))

    def __set_title(self):
        self.title(self.__name)

    def __set_size(self):
        self.attributes('-zoomed', True)
