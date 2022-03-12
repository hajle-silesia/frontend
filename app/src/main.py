from application_window import ApplicationWindow
from tab_bar import TabBar
from tab import Tab, Container
from leaf import Title


application_window = ApplicationWindow()

tab_bar = TabBar(application_window)
recipe = Tab(tab_bar)
brewery = Tab(tab_bar)
fermentation = Tab(tab_bar)

fermentables = Container(recipe)
miscs = Container(recipe)

title_fermentables = Title(fermentables)
title_miscs = Title(miscs)

application_window.position_component()

application_window.mainloop()
