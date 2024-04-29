#   'https://tectonic-fault-api-xfjktxtvla-uc.a.run.app/distances/?latitude=79.0877978&longitude=4.5489855' \
#   -H 'accept: application/json'

from http.client import HTTPException
from typing import List
import requests
from dotenv import dotenv_values

config = dotenv_values(".env") 


class FetchTectonicFaults:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_distances(self):
        self.faults: List[dict[str, str]] = []
        params: dict[str, str] = {
            'accept': 'application/json'
        }
        
        url = f'{config["URL"]}?latitude={self.latitude}&longitude={self.longitude}'
        try:
            response = requests.get(url, headers=params)
            if response.status_code == requests.codes.ok:
                self.faults = response.json()
            if response.status_code == 404:
                self.faults  = {"detail": "404 Page Not Found"}    
        except requests.exceptions.HTTPError as e:
                self.faults  = {"detail": "Bad request"}
        except requests.exceptions.ConnectionError as e:
                self.faults  = {"detail": 'Connection error'}
        except requests.exceptions.Timeout as e:
                self.faults  = {"detail": "Connection timeout"}
        except requests.exceptions.TooManyRedirects as e:
                self.faults  = {"detail": "Too many redirects"}
        except requests.exceptions.RequestException as e:
                self.faults  = {"detail": "Unknown Error"}        
        return self.faults