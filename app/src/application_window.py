from tkinter import *

from composite import Composite


class ApplicationWindow(Tk, Composite):
    def __init__(self, config):
        Tk.__init__(self)
        Composite.__init__(self, config)

    def _set_component(self, config):
        super()._set_component(config)

        # self.__set_titlebar_icon()
        self.__set_title()
        # self.__set_size()

    def __set_titlebar_icon(self, config):
        if 'icon_path' in config:
            self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file=config['icon_path']))

    def __set_title(self):
        self.title(self._name)

    def __set_size(self):
        self.attributes('-zoomed', True)
