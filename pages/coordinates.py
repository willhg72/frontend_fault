import re
from typing import Any, List
import flet as ft

from service.service import FetchTectonicFaults
from styles.coordinates_styles import CoordinatesStyles
from utils.utils import Attributes, UtilsMethods



class CoordinatesForm(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(expand= True)
        self.page = page
        self.styles = CoordinatesStyles()
        #self.utils = 
        self.distances: dict[str, float] = {}
        self.build()

        
        
    def build(self):    
        # Coordinates, longitude and latitude
        self.coordinates_latitude = ft.TextField(focused_bgcolor=ft.colors.YELLOW_50, helper_text="79.3546643 ")
        self.coordinates_latitude_wrapped = UtilsMethods.text_field_container(expand= False, name="Latitude",control=self.coordinates_latitude)
        self.coordinates_longitude = ft.TextField(focused_bgcolor=ft.colors.YELLOW_50, helper_text="4.8022234 ")
        self.coordinates_longitude_wrapped = UtilsMethods.text_field_container(expand= False, name='Longitude',control=self.coordinates_longitude)
        self.coordinates_container = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Container(
                        **self.styles.title_container_styles(),
                        content=ft.Text(value="Coordinates form",color='white', size=40,weight='bold'),
                    ),
                    ft.Container(
                        **self.styles.description_container_styles(),
                        content=ft.Text(
                            value="A fully functional EXAMPLE Project written in Python using FastAPI, that receive a point as latitude and Longitude parameters, and return the 10 closest tectonic faults that point in kms. Please enter below the latitude and longitude you are interested in:"
                        )
                    ),
                    self.coordinates_latitude_wrapped,
                    self.coordinates_longitude_wrapped
                ],
            ),
        )
        #submit button
        self.coordinates_submit_btn =ft.Container(
                **self.styles.submit_button_styles(),
                content=ft.ElevatedButton(
                    bgcolor='black',
                    text="submit",
                    color='#ebebeb',


                    style= ft.ButtonStyle(
                        shape={
                            "":ft.RoundedRectangleBorder(radius=8)
                        }
                    ),
                on_click=self.fetch_data,
                ),
        )

        self.coordinates_response = ft.DataTable(
                    **self.styles.coordinates_data_table_styles(),
        )
        
        #rendering the form
        self.display_form_controls()

        

    def display_form_controls(self):    
        # Deploy all controls
        self.coordinates_main_container = ft.Container(

            alignment = ft.alignment.center,
            content=ft.Column(
                alignment='center',

                horizontal_alignment = 'center',
                controls=[
                    ft.Container(
                        alignment= ft.alignment.top_center,
                        width=500,
                        
                        padding=40,
                        bgcolor='white',
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment='center',
                            controls=[
                                self.coordinates_container,
                                ft.Row(controls=[self.coordinates_submit_btn], alignment='end'),
                                ft.Divider(),
                                self.coordinates_response,
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

        # text define a container to wrap the textfield in


    async def fetch_data(self,e):
        res: dict[str, Any] = self.validate_data(self.coordinates_latitude.value, self.coordinates_longitude.value)
        if res["isvalid"]:
            self.coordinates_response.rows = []
            self.data = FetchTectonicFaults(self.coordinates_latitude.value, self.coordinates_longitude.value)
            self.distances = self.data.get_distances()
            if len(self.distances) > 1:
                index = 1
                
                for fault,distance in self.distances.items():
                    self.coordinates_response.rows.append(
                        self.render_distance_component(fault,distance, index),
                    )        
                    index += 1 
                await self.page.update_async()
            else:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                self.distances["detail"],
                                ft.TextStyle(
                                    size=20,
                                    color=ft.colors.RED,
                                )
                            )      
                        ]
                    )
                )
                self.page.snack_bar.open = True
                await self.page.update_async()                      
        else:
            self.coordinates_latitude.value = ""
            self.coordinates_longitude.value = ""
            self.page.snack_bar = ft.SnackBar(
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                res['detail'],
                                ft.TextStyle(
                                    size=20,
                                    color=ft.colors.YELLOW,
                                )
                            )      
                        ]
                    )
                )            
            
            
            
            self.page.snack_bar.open = True
            await self.page.update_async()    


    def render_distance_component(self,fault: str, distance:float, index: int):
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(index)),
                ft.DataCell(ft.Text(fault)),
                ft.DataCell(ft.Text(value=str(distance))),
            ],
        )

    def validate_data(self, latitude: str, longitude: str):
        pattern = r'/^[-]?\d+[\.]?\d*, [-]?\d+[\.]?\d*$/'
        validate_dt = True
        detail: str = ""
        if latitude and longitude: 
            if re.match(pattern, latitude) and re.match(pattern, longitude):
                validate_dt = False
                detail = "Invalid coordinates, Latitude must be in the [-90; 90] range and Longitude must be in the [-180; 180] range."
            if  float(latitude) <= -90.0 or float(latitude) >= 90.0:
                validate_dt = False
                detail="Invalid latitude, must be in the [-90; 90] range."
            if float(longitude) <= -180.0 or float(longitude) >= 180.0:
                validate_dt = False
                detail="Invalid longitude, must be in the [-180; 180] range."
        else:
            validate_dt = False
            detail = "Please enter the coordinates; both Latitude and Longitude should be filled out."        
        return {
                "isvalid": validate_dt,
                "detail": detail
        }        

