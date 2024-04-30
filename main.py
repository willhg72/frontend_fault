import flet as ft
import flet_fastapi
from pages.coordinates import CoordinatesForm
from utils.utils import Attributes





async def main(page: ft.Page):
    page = page
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = Attributes.BG_PAGE_COLOR_BLUE.value

    await page.add_async(CoordinatesForm(page))
    await page.update_async()


app= flet_fastapi.app(main)

    
