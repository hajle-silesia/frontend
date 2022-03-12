from tkinter import *
from tkinter.ttk import Frame

from composite import Composite


class Tab(Frame, Composite):
    _name = "Tab"

    def __init__(self, parent):
        super().__init__(parent)


class Container(Frame, Composite):
    _name = "Container"

    def __init__(self, parent):
        super().__init__(parent)

    def position_component(self):
        super().position_component()

        self.grid()
