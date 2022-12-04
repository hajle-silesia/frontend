from src.api_thread import APIThread, queue, events_handler
from src.application_window import ApplicationWindow
from src.brewery_tab import BreweryTab, Canvas
from src.config import config
from src.leaf import Title
from src.tab import Tab, Container, RecordsContainer, ParametersContainer
from src.tab_bar import TabBar

application_window = ApplicationWindow(config['application_window'])

tab_bar = TabBar(application_window, config['tab_bar'])

brewery_tab = BreweryTab(tab_bar, config['brewery'])
recipe_tab = Tab(tab_bar, config['recipe'])

user_settings = Container(recipe_tab, config['user_settings'])
miscs = Container(recipe_tab, config['miscs'])
fermentables = Container(recipe_tab, config['fermentables'])
parameters = Container(recipe_tab, config['parameters'])
mash_steps = Container(recipe_tab, config['mash_steps'])
hops = Container(recipe_tab, config['hops'])

recipe_tab_containers = [user_settings,
                         miscs,
                         fermentables,
                         parameters,
                         mash_steps,
                         hops,
                         ]

for container in recipe_tab_containers:
    Title(container, config['title'])

RecordsContainer(miscs, config['records_and_parameters'])
RecordsContainer(fermentables, config['records_and_parameters'])
ParametersContainer(parameters, config['records_and_parameters'])
RecordsContainer(mash_steps, config['records_and_parameters'])
RecordsContainer(hops, config['records_and_parameters'])

brewery_canvas = Canvas(brewery_tab, config['brewery_canvas'])

application_window.position()

recipe_tab.queue = queue

api_thread = APIThread()
events_handler.subscribe(recipe_tab)
application_window.mainloop()
