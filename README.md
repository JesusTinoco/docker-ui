# Docker UI
 
 > Docker UI is a web interface that allows you to interact with the [Docker API client in Python](https://github.com/docker/docker-py).
 
# How to contribute

## Prerequisites
 
To run this application you need to install Docker on your computer. You can find a guide that explains how to install it in the link below:

https://docs.docker.com/engine/installation/
  
Once you have already installed Docker in your local machine, clone this repository and place inside it.

```
cd ~
git clone https://github.com/JesusTinoco/docker-ui
cd docker-ui
```

## Build the image

Now, build an image from the Dockerfile provided. 

 ```
 $ docker build -t docker-ui .
 ```

### Run the image

Once you have build the `docker-ui` image, you will be able to run it. Note, that you will have to mount the docker socket so that the application is fully functional.

```
docker run --privileged --rm -it -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/docker-ui -p 8080:8080 docker-ui
```

Instead of mounting the socket, you can also pass the URL where the Docker api is being executed.

```
docker run --privileged --rm -it -v $PWD:/docker-ui -p 8080:8080 --host=tcp://127.0.0.1:2375
```