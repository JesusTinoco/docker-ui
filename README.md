# Docker UI
 
 > Docker UI is a web interface that allows you to interact with the [Docker API client in Python](https://github.com/docker/docker-py).
 
## Prerequisites
 
 To run this application you need to install Docker on your computer. You can find a guide that explains how to install it in the link below:

 https://docs.docker.com/engine/installation/
 
 Also, this image uses Docker-in-Docker as base image, so your Docker version should support the `--privileged` flag.
 
## Quickstart
 
### Build the image
 
 ```
 $ docker build -t dockerui .
 ```
 
### Run the image
 
* Run dockerui and get a shell where you can play. Also, it maps your port 8080 with the container internal port.
 
    ```
    $ docker run --privileged -it -p 8080:8080 dockerui /bin/bash
    ```
 
* Run dockerui as daemon
 
    ```
    $ docker run --privileged -d -p 8080:8080 dockerui
    ```
