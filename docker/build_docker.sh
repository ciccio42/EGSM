#! /bin/bash

DOCKER_NAME="egsm"

# remove previous image
docker image rm $DOCKER_NAME

# build image
docker build -t $DOCKER_NAME .
