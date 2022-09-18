from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, config):
        self._name = None
        self._title = None
        self._font = None
        self._row = None
        self._column = None
        self._rowspan = None
        self._columnspan = None
        self._rows_quantity = None
        self._columns_quantity = None
        self._sticky = None

        self._queue = None

        self._initialize(config)

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self, queue):
        self._queue = queue

    @abstractmethod
    def position(self):
        pass

    def update_content(self, content=None):
        pass

    @abstractmethod
    def winfo_children(self):
        pass

    @abstractmethod
    def grid_size(self):
        pass

    @abstractmethod
    def rowconfigure(self, index, cnf={}, **kw):
        pass

    @abstractmethod
    def columnconfigure(self, index, cnf={}, **kw):
        pass

    def _initialize(self, config):
        self._set_name(config)
        self._set_title(config)
        self._set_font(config)
        self._set_row(config)
        self._set_column(config)
        self._set_rowspan(config)
        self._set_columnspan(config)
        self._set_sticky(config)

    def _set_name(self, config):
        self._name = config.get('name')

    def _set_title(self, config):
        self._title = config.get('title')

    def _set_font(self, config):
        if 'font' in config:
            self._font = config['font']
            self.config(font=self._font)

    def _set_row(self, config):
        self._row = config.get('row')

    def _set_column(self, config):
        self._column = config.get('column')

    def _set_rowspan(self, config):
        self._rowspan = config.get('rowspan')

    def _set_columnspan(self, config):
        self._columnspan = config.get('columnspan')

    def _set_sticky(self, config):
        self._sticky = config.get('sticky')

    def _set_rows_quantity(self):
        self._rows_quantity = self.grid_size()[1]

    def _set_columns_quantity(self):
        self._columns_quantity = self.grid_size()[0]

    def _arrange_rows(self):
        pass

    def _arrange_columns(self):
        pass


class Composite(Component):
    def position(self):
        for component in self.winfo_children():
            component.position()

        self._set_rows_quantity()
        self._set_columns_quantity()
        self._arrange_rows()
        self._arrange_columns()

    def update_content(self, content=None):
        for component in self.winfo_children():
            component.update_content(content)


class Leaf(Component):
    pass
