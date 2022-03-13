from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, config):
        self._name = None
        self._set_component(config)

    @property
    def name(self):
        return self._name

    @abstractmethod
    def position_component(self):
        pass

    @abstractmethod
    def winfo_children(self):
        pass

    def _set_component(self, config):
        self._set_name(config)

    def _set_name(self, config):
        if 'name' in config:
            self._name = config['name']


class Composite(Component):
    def __init__(self, config):
        Component.__init__(self, config)

    def position_component(self):
        for component in self.winfo_children():
            component.position_component()


class Leaf(Component):
    def __init__(self, config):
        Component.__init__(self, config)
