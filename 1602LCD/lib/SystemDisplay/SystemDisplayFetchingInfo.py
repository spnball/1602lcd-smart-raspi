import threading
import time

class SystemDisplayFetchingInfo (threading.Thread):
    def __init__(self, info, *args, **kwargs):
        super(SystemDisplayFetchingInfo,self).__init__(*args, **kwargs)
        self.info = info
        self.running = True
        self.interval = 30

    def run(self):
        intervalCheck = self.interval
        while self.running :
            if intervalCheck > self.interval :
                intervalCheck = 0
                self.fetch()

            intervalCheck += 5
            time.sleep(5)

    def kill(self):
        self.running = False
