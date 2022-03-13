from tkinter import *
from tkinter.ttk import Label

from composite import Leaf


class Title(Label, Leaf):
    def __init__(self, parent, config):
        self._parent = parent

        Label.__init__(self, parent)
        Leaf.__init__(self, config)

        self._set_component(config)

    def position_component(self):
        self.grid(row=0)

    def _set_component(self, config):
        super()._set_component(config)

    def _set_name(self, config):
        self.config(text=self._parent.name)
