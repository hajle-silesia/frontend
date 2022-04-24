from tkinter import SOLID
from tkinter.ttk import Frame

from composite import Composite


class Tab(Frame, Composite):
    def __init__(self, parent, config):
        Frame.__init__(self, parent)
        Composite.__init__(self, config)

    def position(self):
        super().position()

    def _arrange_rows(self):
        if self._rows_quantity:
            for i in range(1, self._rows_quantity):
                self.rowconfigure(i, weight=1)

    def _arrange_columns(self):
        if self._columns_quantity:
            for i in range(self._columns_quantity):
                self.columnconfigure(i, weight=1, uniform='column')


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

    def _arrange_columns(self):
        for i in range(self._columns_quantity):
            self.columnconfigure(i, weight=1)
