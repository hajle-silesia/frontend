from tkinter import *
from tkinter.ttk import Frame

from composite import Composite


class Tab(Frame, Composite):
    def __init__(self, parent, config):
        Frame.__init__(self, parent)
        Composite.__init__(self, config)

    def position_component(self):
        super().position_component()


class Container(Frame, Composite):
    def __init__(self, parent, config):
        Frame.__init__(self, parent)
        Composite.__init__(self, config)

        self.__config = config

    def position_component(self):
        super().position_component()

        self.grid(row=self.__config['row'], column=self.__config['column'], sticky=self.__config['sticky'])

    def _set_component(self, config):
        super()._set_component(config)
        self.config(borderwidth=4, relief=SOLID)
