from tkinter import *
from tkinter.ttk import Label

from composite import Leaf


class Title(Label, Leaf):
    def __init__(self, parent, config):
        self._parent = parent

        Label.__init__(self, parent)
        Leaf.__init__(self, config)

        self.config(font=self._font)

    def position(self):
        self.grid(row=self._row, columnspan=self._columnspan)

    def _set_name(self, config):
        super()._set_name(config)

        self.config(text=self._parent.name)
