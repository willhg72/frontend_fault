
# Flet Frontend - Tectonic Faults REST API Client

## Welcome to the Flet Frontend repository, your gateway to accessing geospatial data on Colombian tectonic faults. This frontend client is designed to seamlessly interact with our Python-based REST API, providing users with a user-friendly interface to explore tectonic fault information based on latitude and longitude coordinates..

This frontend client is designed to seamlessly interact with our Python-based REST API, providing users with a simple user-friendly interface to explore tectonic fault information based on latitude and longitude coordinates.


#### Get Tectonic faults:
 

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `latitude` | `float` | **Required**.  valid range(>-90 and < 90)|
| `longitude` | `float` | **Required**. valid range(>-180 and < 180)  |


#### coordenates(latitude, longitude)

It takes latitude, longitude and display the 10 closer tectonic faults.


## Usage/Examples

```http
https://tectonic-fault-flet-xfjktxtvla-uc.a.run.app

```


## Screenshots


![Coordinates form](https://media.giphy.com/media/ue3gYv4DZz2y4XqzeR/giphy.gif)


## Appendix

### Architecture diagram.


* FastAPI and Flet.
* Docker and Docker Hub.
* Google Cloud Runs.



![App Screenshot](https://live.staticflickr.com/65535/53689635657_c8c6af7566_c.jpg)
## Authors

- [@willhg72](https://www.github.com/willhg72)

