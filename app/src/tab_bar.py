from tkinter import *
from tkinter.ttk import Notebook


class TabBar(Notebook):
    __name = "TabBar"

    def __init__(self, parent):
        super().__init__(parent)

        self.__composites = []

    @property
    def name(self):
        return self.__name

    def position_component(self):
        for component in self.winfo_children():
            self.add(component, text=component.name)

        self.pack(fill=BOTH, expand=1)

    def __add_tabs_to_tab_bar(self):
        for tab in self.__composites:
            self.add(tab, text=tab.get_name())

    def __position_tab_bar(self):
        self.pack(fill=BOTH, expand=1)
