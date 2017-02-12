import threading
import time


class SystemDisplayFetchingInfo (threading.Thread):
    def __init__(self, info, *args, **kwargs):
        super(SystemDisplayFetchingInfo, self).__init__(*args, **kwargs)
        self.info = info
        self.running = True
        self.interval = 30

    def fetch(self):
        pass

    def run(self):
        interval_check = self.interval
        while self.running:
            if interval_check > self.interval:
                interval_check = 0
                self.fetch()

            interval_check += 5
            time.sleep(5)

    def kill(self):
        self.running = False
