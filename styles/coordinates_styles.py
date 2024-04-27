import flet as ft

from utils.utils import *


class CoordinatesStyles:
    def submit_button_styles(self):
        return {
                'border_radius': Attributes.BORDER_RADIUS_STANDARD.value,
                'padding':Attributes.PADDING_SUBMIT_BUTTON.value,
                'alignment':ft.alignment.center,
        }
        
    def title_container_styles(self):
        return{
                'border_radius': Attributes.BORDER_RADIUS_STANDARD.value,
                'padding':Attributes.PADDING_SUBMIT_BUTTON.value,
                'alignment':ft.alignment.center,
        }
        