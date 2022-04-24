from tkinter import Tk, PhotoImage
import tkinter.font

from composite import Composite


class ApplicationWindow(Tk, Composite):
    def __init__(self, config):
        Tk.__init__(self)
        Composite.__init__(self, config)

    def _initialize(self, config):
        super()._initialize(config)

        # self.__set_titlebar_icon()
        self.__set_title()
        # self.__set_size()
        self.__set_default_fonts()

    def __set_titlebar_icon(self, config):
        if 'icon_path' in config:
            self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file=config['icon_path']))

    def __set_title(self):
        self.title(self._name)

    def __set_size(self):
        self.attributes('-zoomed', True)

    def __set_default_fonts(self):
        default_font_size = tkinter.font.nametofont("TkDefaultFont").actual()['size']

        self.__set_heading_font_size(default_font_size)

    @staticmethod
    def __set_heading_font_size(default_font_size):
        tkinter.font.nametofont("TkHeadingFont").config(size=2 * default_font_size)
