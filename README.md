# docker_ml
Dockerfile of environment for machine learning

## Requirement
* Docker

## Build
```sh
$ cd docker_ml
$ docker build -t mlenv .
```

## Execute Python script
```sh
$ cd docker_ml
$ docker run --rm -v $PWD:/dir mlenv python3 test_script.py
```

In case you want to display graph
```sh
$ xhost +

# Generally
$ docker run --rm -v $PWD:/dir -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY mlenv python3 test_script.py

# Docker for Mac
$ docker run --rm -v $PWD:/dir -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=docker.for.mac.localhost:0 mlenv python3 test_script.py 
```
