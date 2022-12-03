import tkinter
import tkinter.ttk

from src.composite import Composite


class TabBar(tkinter.ttk.Notebook, Composite):
    def __init__(self, parent, config):
        tkinter.ttk.Notebook.__init__(self, parent)
        Composite.__init__(self, config)

    def position(self):
        super().position()

        for component in self.winfo_children():
            self.add(component, text=component.title)

        self.pack(fill=tkinter.BOTH, expand=1)
