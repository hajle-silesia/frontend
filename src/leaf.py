from tkinter import CENTER
from tkinter.ttk import Label

from src.composite import Leaf


class Title(Label, Leaf):
    def __init__(self, parent, config):
        self._parent = parent

        Label.__init__(self, parent, anchor=CENTER)
        Leaf.__init__(self, config)

    def position(self):
        self.grid(row=self._row, column=self._column, sticky=self._sticky)

    def _set_title(self, config):
        super()._set_title(config)

        self.config(text=self._parent.title)
