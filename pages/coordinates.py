import flet as ft

from styles.coordinates_styles import CoordinatesStyles
from utils.utils import *



class Coordinates(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.styles = CoordinatesStyles()
        
        
        self.coordinates_latitude = ft.TextField(hint_text="Latitude: ")
        self.coordinates_longitude = ft.TextField(hint_text="Longitude: ")
        self.coordinates_container = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Container(
                        **self.styles.title_container_styles(),
                        content=ft.Text(value="Coordinates form", size=40,weight='bold'),
                    ),
                    self.coordinates_latitude,
                    self.coordinates_longitude
                ],
            ),
        )
                
        #submit button
        self.coordinates_submit_btn =ft.Container(
                **self.styles.submit_button_styles(),
                content=ft.ElevatedButton("submit coordinates"),
        ) 
        #Response control
        self.coordinates_response = ft.Column()
        
        self.coordinates_main_container = ft.Container(
            alignment = ft.alignment.center,
            
            #alignment=ft.MainAxisAlignment.CENTER,
            #expand = True,
            content=ft.Column(
                alignment='center',
                
                horizontal_alignment = 'center',
                controls=[
                    ft.Container(
                         #padding=ft.padding.only(right=100),
                         alignment= ft.alignment.top_center,
                         width=500,
                         padding=40,
                         bgcolor='white',
                         content=ft.Column(
                           alignment=ft.MainAxisAlignment.CENTER, 
                           horizontal_alignment='center',
                           controls=[
                                self.coordinates_container,
                                self.coordinates_submit_btn,
                                ft.Divider(),
                                self.coordinates_response
                           ],  
                         ),
                    ),                
                ],
            ),
        )
        
        #main controls
        self.alignment=ft.MainAxisAlignment.CENTER
        self.controls=[
                self.coordinates_main_container
        ]
        