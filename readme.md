# microservices using django 
- This micro service will build the service 1 and service 2 micro server.
- I have used 2 django microservices. for this project.

## Requirements 
 - docker 
 - docker-compose 
 - docker python3.8 
 - django > 4.2

## Installation Prodcedure. 
 - First you need to install docker if not installed please follow below steps according to your os.
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up -d`   
 - opne browser or postman to view the json response.
 - http://localhost:8080/api/v1/city-to-zipcode/{city_name} for the city service  
 - http://localhost:8080/api/v1/zipcode-to-city/{zip_code} for zip code service

 Home of the script that lives at `get.docker.com` and `test.docker.com`!

# docker installation pocedure
The purpose of the install script is for a convenience for quickly
installing the latest Docker-CE releases on the supported linux
distros. It is not recommended to depend on this script for deployment
to production systems. For more thorough instructions for installing
on the supported distros, see the [install
instructions](https://docs.docker.com/engine/install/).

This repository is solely maintained by Docker, Inc.

## Usage:

From `https://get.docker.com`:
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

From `https://test.docker.com`:
```shell
curl -fsSL https://test.docker.com -o test-docker.sh
sh test-docker.sh
```

From the source repo (This will install latest from the `stable` channel):
```shell
sh install.sh
```