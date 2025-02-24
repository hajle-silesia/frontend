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
            js.document.getElementById(parent).appendChild(self.element)
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
            self._set_alt(config)
            self._set_style_left(config)
            self._set_style_top(config)
            self._set_hidden(config)
            self._set_controls(config)
            self._set_width(config)
            self._set_height(config)
            self._set_autoplay(config)
            self._set_muted(config)
            self._set_script(config)
            self._set_listener(config)

    def _set_id(self, config):
        if "id" in config:
            self.element.id = config["id"]

    def _set_class(self, config):
        if "class" in config:
            self.element.classList.add(config["class"])

    def _set_inner_html(self, config):
        if "inner_html" in config:
            self.element.innerHTML = config["inner_html"]

    def _set_rowspan(self, config):
        if "rowspan" in config:
            self.element.rowSpan = f"{config['rowspan']}"

    def _set_type(self, config):
        if "type" in config:
            self.element.type = config["type"]

    def _set_html_for(self, config):
        if "html_for" in config:
            self.element.htmlFor = config["html_for"]

    def _set_src(self, config):
        if "src" in config:
            self.element.src = config["src"]

    def _set_alt(self, config):
        if "alt" in config:
            self.element.alt = config["alt"]

    def _set_style_left(self, config):
        if "style_left" in config:
            self.element.style.left = f"{100 * float(config["style_left"])}%"

    def _set_style_top(self, config):
        if "style_top" in config:
            self.element.style.top = f"{100 * float(config["style_top"])}%"

    def _set_hidden(self, config):
        if "hidden" in config:
            if config["hidden"].casefold() == "true":
                self.element.hidden = True

    def _set_controls(self, config):
        if "controls" in config:
            self.element.controls = bool(config["controls"])

    def _set_width(self, config):
        if config.get("width"):
            self.element.width = config["width"]

    def _set_height(self, config):
        if config.get("height"):
            self.element.height = config["height"]

    def _set_autoplay(self, config):
        if "autoplay" in config:
            self.element.autoplay = bool(config["autoplay"])

    def _set_muted(self, config):
        if "muted" in config:
            self.element.muted = bool(config["muted"])

    def _set_script(self, config):
        if "script" in config:
            with open(config["script"], encoding="utf-8") as script:
                content = script.read()
            content = content.format(
                element_id=config["element_id"],
                base_url=js.window.location.href,
            )
            self.element.innerHTML = content

    def _set_listener(self, config):
        import listeners

        print(config)
        if "listener" in config:
            listeners.set_listener(
                self.element,
                config["event"] if config.get("event") else "click",
                listeners.registry.get(config["listener"]),
                config["element_id"] if config.get("element_id") else self.element.id,
            )
