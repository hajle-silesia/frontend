import tkinter
import tkinter.ttk

from src.composite import Leaf


class Title(tkinter.ttk.Label, Leaf):
    def __init__(self, parent, config):
        self._parent = parent

        tkinter.ttk.Label.__init__(self, parent, anchor=tkinter.CENTER)
        Leaf.__init__(self, config)

    def position(self):
        self.grid(row=self._row, column=self._column, sticky=self._sticky)

    def _set_title(self, config):
        super()._set_title(config)

        self.config(text=self._parent.title)
