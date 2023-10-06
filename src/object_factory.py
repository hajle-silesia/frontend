import js


class HTML:
    def __init__(self, tag_name, parent=None, config=None):
        self._create_js_element(tag_name)
        self._append_element_to_parent(parent)
        self._configure_element_attributes(config)

    def _create_js_element(self, tag_name):
        self.element = js.document.createElement(tag_name)

    def _append_element_to_parent(self, parent):
        if parent:
            parent.appendChild(self.element)
        else:
            js.document.body.appendChild(self.element)

    def _configure_element_attributes(self, config):
        if config is not None:
            self._set_id(config)
            self._set_class(config)
            self._set_inner_html(config)
            self._set_rowspan(config)
            self._set_type(config)
            self._set_html_for(config)
            self._set_src(config)
            self._set_style_left(config)
            self._set_style_top(config)
            self._set_py_click(config)

    def _set_id(self, config):
        if 'id' in config:
            self.element.id = config['id']

    def _set_class(self, config):
        if 'class' in config:
            self.element.classList.add(config['class'])

    def _set_inner_html(self, config):
        if 'inner_html' in config:
            self.element.innerHTML = config['inner_html']

    def _set_rowspan(self, config):
        if 'rowspan' in config:
            self.element.rowSpan = f"{config['rowspan']}"

    def _set_type(self, config):
        if 'type' in config:
            self.element.type = config['type']

    def _set_html_for(self, config):
        if 'html_for' in config:
            self.element.htmlFor = config['html_for']

    def _set_src(self, config):
        if 'src' in config:
            self.element.src = config['src']

    def _set_style_left(self, config):
        if 'style_left' in config:
            self.element.style.left = config['style_left']

    def _set_style_top(self, config):
        if 'style_top' in config:
            self.element.style.top = config['style_top']

    def _set_py_click(self, config):
        if 'py_click' in config:
            self.element.setAttribute('py-click', config['py_click'])
