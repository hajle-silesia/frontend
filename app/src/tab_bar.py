from tkinter import *
from tkinter.ttk import Notebook

from composite import Composite


class TabBar(Notebook, Composite):
    _name = "TabBar"

    def __init__(self, parent):
        super().__init__(parent)

    def position_component(self):
        super().position_component()

        for component in self.winfo_children():
            self.add(component, text=component.name)

        self.pack(fill=BOTH, expand=1)
