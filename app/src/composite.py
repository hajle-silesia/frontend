from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, config):
        self._name = None
        self._row = None
        self._column = None
        self._rowspan = None
        self._columnspan = None
        self._sticky = None

        self._initialize(config)

    @property
    def name(self):
        return self._name

    @abstractmethod
    def position(self):
        pass

    @abstractmethod
    def winfo_children(self):
        pass

    def _initialize(self, config):
        self._set_name(config)
        self._set_row(config)
        self._set_column(config)
        self._set_rowspan(config)
        self._set_columnspan(config)
        self._set_sticky(config)

    def _set_name(self, config):
        if 'name' in config:
            self._name = config['name']

    def _set_row(self, config):
        if 'row' in config:
            self._row = config['row']

    def _set_column(self, config):
        if 'column' in config:
            self._column = config['column']

    def _set_rowspan(self, config):
        if 'rowspan' in config:
            self._rowspan = config['rowspan']

    def _set_columnspan(self, config):
        if 'columnspan' in config:
            self._columnspan = config['columnspan']

    def _set_sticky(self, config):
        if 'sticky' in config:
            self._sticky = config['sticky']


class Composite(Component):
    def __init__(self, config):
        Component.__init__(self, config)

    def position(self):
        for component in self.winfo_children():
            component.position()


class Leaf(Component):
    def __init__(self, config):
        Component.__init__(self, config)
