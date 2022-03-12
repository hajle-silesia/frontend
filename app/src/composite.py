from abc import ABC, abstractmethod


class Component(ABC):
    _name = None

    @property
    def name(self):
        return self._name

    @abstractmethod
    def position_component(self):
        pass

    @abstractmethod
    def winfo_children(self):
        pass


class Composite(Component):
    def position_component(self):
        for component in self.winfo_children():
            component.position_component()


class Leaf(Component):
    pass
