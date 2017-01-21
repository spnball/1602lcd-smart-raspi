from netifaces import interfaces, ifaddresses, AF_INET
from SystemDisplayFetchingInfo import SystemDisplayFetchingInfo
from random import randint
import threading, time, collections

class NetIfaceInfo:
    def __init__(self):
        self.interface = {}
        self.carousel = collections.deque([])

class NetIfaceFetchingInfo (SystemDisplayFetchingInfo) :
    def __init__(self, info, *args, **kwargs):
        super(NetIfaceFetchingInfo,self).__init__(info, *args, **kwargs)
        self.interval = 60

    def fetch(self):
        newCarousel = collections.deque([])
        newIface = collections.deque([])
        ipList = {}

        for interface in interfaces():
            try:
                for link in ifaddresses(interface)[AF_INET]:
                    newIface.append(interface)
                    ipList[interface] = link
            except:
                pass

        for iface in self.info.carousel:
            newCarousel.append(iface)
            newIface.remove(iface)

        for iface in newIface:
            newCarousel.append(iface)

        self.info.interface = ipList
        self.info.carousel = newCarousel

        return self.info.interface


class NetIfaceDisplay(threading.Thread):
    def __init__(self, screen, *args, **kwargs):
        super(NetIfaceDisplay,self).__init__(*args, **kwargs)
        self.screen = screen
        self.running = True
        self.interval = 5
        self.info = NetIfaceInfo()
        self.fetchingInfo = NetIfaceFetchingInfo(self.info)

    def setInterval(self, interval):
        self.interval = interval
        return self

    def run(self):
        self.fetchingInfo.start()
        self.screen.printClear("Ip address\nrunning..", "center")

        while self.running:
            if len(self.info.carousel) > 0 :
                self.info.carousel.rotate(-1)
                currentDisplayIface = self.info.carousel[0]
                self.screen.printClear(
                    "%s\n%s" % (currentDisplayIface, self.info.interface[currentDisplayIface]['addr']),
                    "center")

            time.sleep(10)
            if randint(0, 1) == 0:
                self.screen.slideOutLeft()
            else:
                self.screen.slideOutRight()

    def kill(self):
        self.fetchingInfo.kill()
        self.running = False