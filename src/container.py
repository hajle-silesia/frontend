import abc

from object_factory import HTML


class Container(HTML):
    def __init__(self, parent, config):
        self._parent = parent
        self._config = config
        self.name = config["name"]

    def update_content(self, content=None):
        if content.get(self.name):
            header = self._get_headers(content[self.name])

            HTML("table", self._parent, {"id": self.name, "class": "inner"})

            HTML("tr", self.name, {"id": f"{self.name}_headers"})
            for column in header:
                HTML("th", f"{self.name}_headers", {"inner_html": column})

            if content is not None:
                self._add_content_to_table(content, self.name)

            return self

    @abc.abstractmethod
    def _get_headers(self, content):
        pass

    @abc.abstractmethod
    def _add_content_to_table(self, content, table):
        pass


class RecordsContainer(Container):
    def _get_headers(self, content):
        return content[0]

    def _add_content_to_table(self, content, table):
        for i, entry in enumerate(content[self.name]):
            HTML("tr", table, {"id": f"{self.name}_{i}"})
            for column_value in entry.values():
                HTML("td", f"{self.name}_{i}", {"inner_html": column_value})


class ParametersContainer(Container):
    def _get_headers(self, _content):
        return ["NAME", "VALUE"]

    def _add_content_to_table(self, content, table):
        for k, v in content[self.name].items():
            HTML("tr", table, {"id": f"{self.name}_{k}"})
            HTML("td", f"{self.name}_{k}", {"inner_html": k})
            HTML("td", f"{self.name}_{k}", {"inner_html": v})
