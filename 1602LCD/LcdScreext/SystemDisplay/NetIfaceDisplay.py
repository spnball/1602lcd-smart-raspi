from netifaces import interfaces
from netifaces import ifaddresses
from netifaces import AF_INET
from SystemDisplayFetchingInfo import SystemDisplayFetchingInfo
import threading
import time
import collections


class NetIfaceInfo:
    def __init__(self):
        self.interface = {}
        self.carousel = collections.deque([])


class NetIfaceFetchingInfo (SystemDisplayFetchingInfo):
    def __init__(self, info, *args, **kwargs):
        super(NetIfaceFetchingInfo, self).__init__(info, *args, **kwargs)
        self.interval = 60

    def fetch(self):
        new_carousel = collections.deque([])
        new_iface = collections.deque([])
        ip_list = {}

        for interface in interfaces():
            try:
                for link in ifaddresses(interface)[AF_INET]:
                    new_iface.append(interface)
                    ip_list[interface] = link
            except:
                pass

        for interface in self.info.carousel:
            new_carousel.append(interface)
            new_iface.remove(interface)

        for interface in new_iface:
            new_carousel.append(interface)

        self.info.interface = ip_list
        self.info.carousel = new_carousel

        return self.info.interface


class NetIfaceDisplay(threading.Thread):
    screen = None
    running = True
    interval = 5
    info = None
    fetching_info = None

    def __init__(self, screen, *args, **kwargs):
        super(NetIfaceDisplay, self).__init__(*args, **kwargs)
        self.screen = screen
        self.info = NetIfaceInfo()
        self.fetching_info = NetIfaceFetchingInfo(self.info)

    def set_interval(self, interval):
        self.interval = interval
        return self

    def run(self):
        self.fetching_info.start()
        self.screen.printClear("Ip address\nrunning..", "center")

        while self.running:
            if len(self.info.carousel) > 0:
                self.info.carousel.rotate(-1)
                current_display_iface = self.info.carousel[0]
                self.screen.printClear(
                    "%s\n%s" % (current_display_iface, self.info.interface[current_display_iface]['addr']),
                    "center")

            time.sleep(5)

    def kill(self):
        self.fetching_info.kill()
        self.running = False
