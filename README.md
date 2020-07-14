# MutantDNAAnalizer

This API provides an endpoint for analize if a DNA chain corresponds to a Mutant. 
Also has and endpoint for stats of how many analized data corresponds to mutant or for human.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For running this application you will need

* Docker

### Installing

In the main folder of the project where the DockerFile is located run the following commands:

* docker build -t mutantdnaanalizer .

and then 

* docker run -d --name mutantanalizer -p 80:80 mutanddnaanalizer

this will create an image and the launch in a container. This Image include all what you need to use the application


## Deployment

For development you can just modify the code and create the image again or, download Python, PIP, install with pip all the requirement list in requirement.txt
and do:

* python main.py

in the app folder

## Built With

* [Python](https://www.python.org/)
* [numpy](https://numpy.org/)
* [flask](https://flask.palletsprojects.com/en/1.1.x/)
* [flask_sqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [flask_cors](https://flask-cors.readthedocs.io/en/latest/)
* [sqlalchemy](https://docs.sqlalchemy.org/en/13/)


## Authors

* **Jose Solaro** - [josesolaro](https://github.com/josesolaro)


## Acknowledgments
The start docker image was made by [tiangolo](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)  