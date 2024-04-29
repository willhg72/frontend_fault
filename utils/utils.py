import flet as ft
from enum import Enum


class Attributes(Enum):
    PADDING_SUBMIT_BUTTON = 10
    BORDER_RADIUS_STANDARD = 10
    BG_PAGE_COLOR_BLUE='#4e73df'
    
class UtilsMethods():
    def text_field_container(expand: bool, name: str, control: ft.TextField):
        return ft.Container(
            expand=expand,
            height=85,
            bgcolor='#ebebeb',
            border_radius=6,
            padding=8,
            content=ft.Column(
                    spacing=1,
                    controls=[
                        ft.Text(
                            value=name,
                            size=9,
                            color='black',
                            weight='bold',
                        ),
                        control
                    ],
            ),
        )