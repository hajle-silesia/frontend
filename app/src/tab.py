from tkinter import *
from tkinter.ttk import Frame

from composite import Composite


class Tab(Frame, Composite):
    def __init__(self, parent, config):
        Frame.__init__(self, parent)
        Composite.__init__(self, config)

    def position(self):
        super().position()


class Container(Frame, Composite):
    def __init__(self, parent, config):
        Frame.__init__(self, parent)
        Composite.__init__(self, config)

    def position(self):
        super().position()

        self.grid(row=self._row, column=self._column, rowspan=self._rowspan, columnspan=self._columnspan,
                  sticky=self._sticky)

    def _initialize(self, config):
        super()._initialize(config)

        self.config(borderwidth=4, relief=SOLID)
