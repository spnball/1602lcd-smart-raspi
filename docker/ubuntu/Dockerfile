FROM ubuntu:16.04
MAINTAINER Surapun Prasit <surapun.prasit@gmail.com>

VOLUME ["/root/1602LCD"]

RUN apt-get update && apt-get install -y \
    python-pip python-dev build-essential 

RUN pip install --upgrade pip 
RUN pip install --upgrade virtualenv 
RUN pip install netifaces
