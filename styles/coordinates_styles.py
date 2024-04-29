from typing import Any
import flet as ft

from utils.utils import *


class CoordinatesStyles:
    def submit_button_styles(self):
        return {
                'border_radius': Attributes.BORDER_RADIUS_STANDARD.value,
                'padding':Attributes.PADDING_SUBMIT_BUTTON.value,
                'alignment':ft.alignment.center,
                #'bgcolor': 'black',
                #'color': 'white'
        }
        
    def title_container_styles(self):
        return{
                "height": 80,
                "bgcolor": "#081d33",
                #"border_radius": ft.border_radius.only(top_left=15, top_right=15),
                "padding": ft.padding.only(left=15, right=15, bottom=15),
                'border_radius': Attributes.BORDER_RADIUS_STANDARD.value,
                'padding':Attributes.PADDING_SUBMIT_BUTTON.value,
                'alignment':ft.alignment.center,
        }
    def coordinates_text_fields_style(self):
        return {
        'border_radius': 8,
        'border': ft.border.all(1, "#ebebeb"),
        'bgcolor': 'white10',
        'padding': 15,
    }
        
        
        
    def coordinates_data_table_styles(self):    
        column_names: list[str] = [
            ' # ',' Fault name ', ' Distance(Kms) '
        ]

        return {
            'border_radius': 8,
            #'border': ft.border.all(2, '#ebebeb'),
            'horizontal_lines': ft.border.BorderSide(1, '#ebebeb'),
            'columns': [
                ft.DataColumn(ft.Text(index, size=12, color="black", weight="bold")) 
                for index in column_names
            ]
        }
        
    def description_container_styles(self):
        return{
                "height": 130,
                # "bgcolor": "#081d33",
                #"border_radius": ft.border_radius.only(top_left=15, top_right=15),
                "padding": ft.padding.only(left=15, right=15, bottom=15),
                'border_radius': Attributes.BORDER_RADIUS_STANDARD.value,
                'padding':Attributes.PADDING_SUBMIT_BUTTON.value,
                'alignment':ft.alignment.center,
        }