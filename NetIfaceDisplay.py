from netifaces import interfaces, ifaddresses, AF_INET

class NetIfaceDisplay:
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
