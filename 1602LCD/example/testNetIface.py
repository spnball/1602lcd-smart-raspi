#!/usr/bin/python

from netifaces import interfaces, ifaddresses, AF_INET

newIface = {};

for interface in interfaces():
    for link in ifaddresses(interface)[AF_INET]:
        newIface[interface] = link['addr']

print newIface
