from tkinter import BOTH
from tkinter.ttk import Notebook

from src.composite import Composite


class TabBar(Notebook, Composite):
    def __init__(self, parent, config):
        Notebook.__init__(self, parent)
        Composite.__init__(self, config)

    def position(self):
        super().position()

        for component in self.winfo_children():
            self.add(component, text=component.name)

        self.pack(fill=BOTH, expand=1)
