from netifaces import interfaces, ifaddresses, AF_INET
from SystemDisplayFetchingInfo import SystemDisplayFetchingInfo
import threading, time, collections

class NetIfaceInfo:
    def __init__(self):
        self.interface = {}
        self.carousel = collections.deque([])

class NetIfaceFetchingInfo (SystemDisplayFetchingInfo) :
    def fetch(self):
        newCarousel = collections.deque([])
        newIface = collections.deque([])
        ipList = {}

        for interface in interfaces():
            try:
                for link in ifaddresses(interface)[AF_INET]:
                    newIface.append(interface)
            except:
                pass

        for iface in self.info.carousel:
            newCarousel.append(iface)
            newIface.remove(iface)

        for iface in newIface:
            newCarousel.append(iface)

        print ipList
        self.info.interface = ipList
        self.info.carousel = newCarousel

        return self.info.interface


class NetIfaceDisplay(threading.Thread):
    def __init__(self, screen, *args, **kwargs):
        super(NetIfaceDisplay,self).__init__(*args, **kwargs)
        self.screen = screen
        self.running = True
        self.interval = 10
        self.info = NetIfaceInfo()
        self.fetchingInfo = NetIfaceFetchingInfo(self.info)

    def setInterval(self, interval):
        self.interval = interval
        return self

    def run(self):
        self.fetchingInfo.start()
        self.screen.printClear("NetIfaceDisplay", "center")

        while self.running:
            print self.info.interface
            if len(self.info.carousel) > 0 :
                print self.info
                # self.fetchingInfo.carousel.rotate(-1)
                # currentDisplayIface = self.fetchingInfo.carousel[0]
                # print self.fetchingInfo.interface[currentDisplayIface]

            time.sleep(2)

    def kill(self):
        self.fetchingInfo.kill()
        self.running = False