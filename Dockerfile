# Author : Claudéric DeRoy
# goal : Dockerfile for the seed to voxel correlation note that it isn't 
#        perfect like I shouldn't have to git clone my repo to access the 
#        the requirements.txt file
# last date of modification : 5 august 2022

FROM ubuntu:20.04

RUN apt-get update -y \
    && apt-get install emacs -y \
    && apt-get install python3-pip -y \
    && apt-get install git -y \
    && python3 -m pip install --upgrade pip \
    && git clone https://github.com/brainhack-school2022/deroy_project.git \
    && cd /deroy_project/ \
    && pip install -r requirements.txt \
    && pip install -i https://test.pypi.org/simple/ seed-to-voxel-neurok8050
    

