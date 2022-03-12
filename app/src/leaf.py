from tkinter import *
from tkinter.ttk import Label


class Title(Label):
    __name = "Title"

    def __init__(self, parent):
        super().__init__(parent)

        self._set_component()

    @property
    def name(self):
        return self.__name

    def position_component(self):
        self.grid(row=0, column=0, sticky=NSEW)

    def _set_component(self):
        self.config(text=self.__name)
