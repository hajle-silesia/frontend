from src.application_window import ApplicationWindow
from src.tab_bar import TabBar
from src.tab import Tab, Container
from src.leaf import Title
from src.config import config


application_window = ApplicationWindow(config['application_window'])

tab_bar = TabBar(application_window, config['tab_bar'])
recipe = Tab(tab_bar, config['recipe'])

user_settings = Container(recipe, config['user_settings'])
miscs = Container(recipe, config['miscs'])
fermentables = Container(recipe, config['fermentables'])
parameters = Container(recipe, config['parameters'])
mash_steps = Container(recipe, config['mash_steps'])
hops = Container(recipe, config['hops'])

Title(user_settings, config['title'])
Title(miscs, config['title'])
Title(fermentables, config['title'])
Title(parameters, config['title'])
Title(mash_steps, config['title'])
Title(hops, config['title'])

application_window.position()

application_window.mainloop()
