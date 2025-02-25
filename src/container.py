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

            t = HTML("table", self._parent.element, {"class": "inner"})

            row = HTML("tr", t.element)
            for col in header:
                HTML("th", row.element, {"inner_html": col})

            if content is not None:
                self._add_content_to_table(content, t)

            return self

    @abc.abstractmethod
    def _get_headers(self, content):
        pass

    @abc.abstractmethod
    def _add_content_to_table(self, content, t):
        pass


class RecordsContainer(Container):
    def _get_headers(self, content):
        return content[0]

    def _add_content_to_table(self, content, t):
        for entry in content[self.name]:
            row = HTML("tr", t.element)
            for table_col in entry.values():
                HTML("td", row.element, {"inner_html": table_col})


class ParametersContainer(Container):
    def _get_headers(self, _content):
        return ["NAME", "VALUE"]

    def _add_content_to_table(self, content, t):
        for k, v in content[self.name].items():
            row = HTML("tr", t.element)
            HTML("td", row.element, {"inner_html": k})
            HTML("td", row.element, {"inner_html": v})
