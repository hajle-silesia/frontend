from tkinter import *


class ApplicationWindow(Tk):
    def __init__(self):
        self.__preset_window()

        super().__init__()

        self.__name = "Hajle Silesia Homebrewing System"
        self.__icon_path = "./img/icon.png"

        self.__set_window()

    def __preset_window(self):
        self.__set_dpi_awareness()

    @staticmethod
    def __set_dpi_awareness():
        pass

    def __set_window(self):
        self.__set_titlebar_icon()
        self.__set_title()
        self.__set_size()

    def __set_titlebar_icon(self):
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file=self.__icon_path))

    def __set_title(self):
        self.title(self.__name)

    def __set_size(self):
        self.attributes('-zoomed', True)
