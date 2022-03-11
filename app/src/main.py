from application_window import ApplicationWindow
from tab_bar import TabBar
from tab import Tab


application_window = ApplicationWindow()

tab_bar = TabBar(application_window)
recipe = Tab(tab_bar)
brewery = Tab(tab_bar)
fermentation = Tab(tab_bar)

application_window.position_component()

application_window.mainloop()
