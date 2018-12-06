#!/bin/bash

docker run --rm -v $PWD:/dir -e DISPLAY=docker.for.mac.localhost:0 -v /tmp/.X11-unix:/tmp/.X11-unix mlenv python3 test_script.py
