from abc import abstractmethod
from tkinter import *
from tkinter.ttk import Frame
from tkinter.ttk import Label

from src.composite import Composite, Leaf


class Tab(Frame, Composite):
    def __init__(self, parent, config):
        Frame.__init__(self, parent)
        Composite.__init__(self, config)

        self.bind('<<MessageGenerated>>', lambda event: self.update_content())

    def update_content(self, content=None):
        if not self.queue.empty():
            content = self.queue.get()

            super().update_content(content)

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

    def update_content(self, content=None):
        super().update_content(content)

    def _initialize(self, config):
        super()._initialize(config)

        self.config(borderwidth=1, relief=SOLID)

    def _arrange_rows(self):
        if self._rows_quantity:
            for i in range(1, self._rows_quantity):
                self.rowconfigure(i, weight=1)

    def _arrange_columns(self):
        if self._columns_quantity:
            for i in range(self._columns_quantity):
                self.columnconfigure(i, weight=1)


class DataContainer(Container):
    def __init__(self, parent, config):
        self._parent = parent

        super().__init__(parent, config)

        self._data_columns = []

    def position(self):
        super().position()

        self.grid(row=self._row, column=self._column, sticky=self._sticky)

    def update_content(self, content=None):
        self.__destroy()

        if self.name in content and content[self.name]:
            columns_names = self._get_columns_names(content)
            columns_quantity = len(columns_names)
            self.__create_data_columns(columns_quantity)
            self.__add_columns_names_to_data_columns(columns_names)
            self._add_content_to_data_columns(content)

        super().position()

    def __destroy(self):
        for child in self.winfo_children():
            child.destroy()

    @abstractmethod
    def _get_columns_names(self, content):
        pass

    def __create_data_columns(self, columns_quantity):
        self._data_columns = [DataColumn(self, {'row': 1, 'column': i, 'sticky': NW}) for i in range(columns_quantity)]

    def __add_columns_names_to_data_columns(self, columns_names):
        for container, column in zip(self._data_columns, columns_names):
            container.config(text=column)

    @abstractmethod
    def _add_content_to_data_columns(self, content):
        pass

    def _initialize(self, config):
        Composite._initialize(self, config)

    def _arrange_columns(self):
        for i in range(self._columns_quantity):
            self.columnconfigure(i, weight=1)

    def _add_text_to_data_column(self, value, data_column):
        data_column.config(text=data_column.cget('text') + '\n' + str(value))

    def _set_name(self, config):
        super()._set_name(config)

        self._name = self._parent.name


class RecordsContainer(DataContainer):
    def _get_columns_names(self, content):
        return content[self.name][0]

    def _add_content_to_data_columns(self, content):
        for entry in content[self.name]:
            for data_column, v in zip(self._data_columns, entry.values()):
                self._add_text_to_data_column(v, data_column)


class ParametersContainer(DataContainer):
    def _get_columns_names(self, content):
        return ['NAME', 'VALUE']

    def _add_content_to_data_columns(self, content):
        for entry in list(content[self.name].items()):
            for data_column, v in zip(self._data_columns, entry):
                self._add_text_to_data_column(v, data_column)


class DataColumn(Label, Leaf):
    def __init__(self, parent, config):
        Label.__init__(self, parent, justify=LEFT)
        Leaf.__init__(self, config)

    def position(self):
        self.grid(row=self._row, column=self._column, sticky=self._sticky)
