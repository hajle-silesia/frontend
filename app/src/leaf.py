from tkinter import *
from tkinter.ttk import Label

from composite import Leaf


class Title(Label, Leaf):
    _name = "Title"

    def __init__(self, parent):
        super().__init__(parent)

        self._set_component()

    def position_component(self):
        self.grid(row=0, column=0, sticky=NSEW)

    def _set_component(self):
        self.config(text=self._name)
