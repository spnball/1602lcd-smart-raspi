from netifaces import interfaces
from netifaces import ifaddresses
from netifaces import AF_INET
from SystemDisplayFetchingInfo import SystemDisplayFetchingInfo
from SystemDisplay import SystmeDisplay
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


class NetIfaceDisplay(SystmeDisplay):
    info = None
    fetching_info = None

    def __init__(self, screen, *args, **kwargs):
        super(NetIfaceDisplay, self).__init__(screen, *args, **kwargs)
        self.info = NetIfaceInfo()
        self.fetching_info = NetIfaceFetchingInfo(self.info)

    def set_interval(self, interval):
        self.interval = interval
        return self

    def run(self):
        self.fetching_info.start()
        self.screen.print_clear("Ip address\nrunning..", "center")

        while self.running:
            if len(self.info.carousel) > 0:
                self.info.carousel.rotate(-1)
                current_display_iface = self.info.carousel[0]
                self.print_next(
                    "%s\n%s" % (current_display_iface, self.info.interface[current_display_iface]['addr']),
                    "center")

            time.sleep(5)
