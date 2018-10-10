# Cardealership

## Prerequisites

- Have docker installed in your machine (latest version)

## Install on Ubuntu or Linux enviroment 

1. Download (pull) the docker image [neocloud19/carrental-django:version1](https://hub.docker.com/r/neocloud19/carrental-django/)
2. Start container using that image with the command:

```shell
sudo docker run -it -d -p 8000:8000/tcp neocloud19/carrental-django:version1
```
*You can change the port according to your needs, I will assume in the context of this README that the ports host:container are both 8000*

3. Go to the hosting enviroment (ie. Ubuntu ) if it has a visual interface please go to your browser and write:

```
127.0.0.1:8000
```
Here initially you will see two empty lists, this is because there is no data on the DB. The data must be inserted manually from the UI for the API

## App guide

*remember to follow the links literally*

- 127.0.0.1:8000/api/cars/ -> list of all the cars with some CRUD operation support (ADMIN view)
- 127.0.0.1:8000/api/rentals/ -> list of all the rentals with some CRUD operation support (ADMIN view)
- 127.0.0.1:8000/api/cars/[id]/ ->  car detail data with all CRUD operation support (ADMIN view)
- 127.0.0.1:8000/api/rentals/[id]/ -> rental detail with all CRUD operation support (ADMIN view)
- 127.0.0.1:8000/ -> rental and car list for customers (USER view)

## Notes on the APP development

- The application was developed in Python with DJANGO framework for the backend.
- The small and simple frontend was developed with React/ ES6 / webpack
- The DB is the embbeded with DJango SQlite
- There is no authentication for user but theres the ADMIN console for DJango (admin/admin :) )
- The dockerization was done without docker compose
- The frontend was provided as-is , 'production ready', the sources were included but no building was done on docker.

## Useful links

- [Dockerfile Repo](https://github.com/alejandro-onatra/cardealership-docker)
- [Docker image repo](https://hub.docker.com/r/neocloud19/carrental-django/)
