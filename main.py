import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent



def main(page: ft.Page) -> None:
    page.title = 'Tectonic fault coordinates input form'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 800
    page.window_resizable = False
    
    text_latitude: TextField = TextField(hint_text='-79.2324555', label='Latitude', text_align=ft.TextAlign.LEFT, width=200)
    text_longitude: TextField = TextField(hint_text='9.223844', label='Longitude', text_align=ft.TextAlign.LEFT, width=200)
    button_submit: ElevatedButton = ElevatedButton(text='Submit', width=200, disabled=True, on_click=lambda e: page.update())
    
    
    def validate(e: ControlEvent) -> None:
        if all([text_latitude.value, text_longitude.value]):
            button_submit.disabled = False
        page.update()
            
            
    def submit(e: ControlEvent) -> None:
        pass
    
    text_latitude.on_change = validate
    text_longitude.on_change = validate
    button_submit.on_click = submit
    
    page.add(
        Row(
            controls=[
                Column([
                        text_latitude,
                        text_longitude,
                        button_submit,
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )       
    
    
if __name__ == '__main__':
    ft.app(target=main)