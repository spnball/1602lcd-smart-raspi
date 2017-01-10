from netifaces import interfaces, ifaddresses, AF_INET
import threading
import time

class NetIfaceDisplay(threading.Thread):
    def __init__(self, screen, *args, **kwargs):
        super(NetIfaceDisplay,self).__init__(*args, **kwargs)
        self.screen = screen
        self.runing = True
        self.interval = 10

    def ip4Addresses(self):
        ipList = {}
        for interface in interfaces():
            try:
                for link in ifaddresses(interface)[AF_INET]:
                    ipList[interface] = link.addr
            except:
                pass
        return ipList
        
    def play(self, lcd):
        ipList = self.ip4Addresses()
        lcd.clearPrint(ipList.wlan0);
        print ipList

    def setInterval(self, interval):
        self.interval = interval
        return self
    def run(self):
        while self.runing:
            self.screen.printClear("center")
            time.sleep(self.interval)

    def kill(self):
        self.runing = False