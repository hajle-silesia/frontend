from tkinter.ttk import Frame


class Tab(Frame):
    __name = "Tab"

    def __init__(self, parent):
        super().__init__(parent)

        self.__composites = []

    @property
    def name(self):
        return self.__name

    def position_component(self):
        pass
