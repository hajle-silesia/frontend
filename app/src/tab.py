from tkinter import *
from tkinter.ttk import Frame


class Tab(Frame):
    __name = "Tab"

    def __init__(self, parent):
        super().__init__(parent)

    @property
    def name(self):
        return self.__name

    def position_component(self):
        for component in self.winfo_children():
            component.position_component()


class Container(Frame):
    __name = "Container"

    def __init__(self, parent):
        super().__init__(parent)

    @property
    def name(self):
        return self.__name

    def position_component(self):
        for component in self.winfo_children():
            component.position_component()

        self.grid()
