import flet as ft
from pages.coordinates import Coordinates
from utils.utils import Attributes

 


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = Attributes.BG_PAGE_COLOR_BLUE.value
        self.init()
        self.page.update()

    def init(self):
        self.coordinates_page = Coordinates(self.page)
        self.page.add(self.coordinates_page)
        self.page.update()
    



#ft.app(target=Main)
    
    
