import threading
import time
import collections

class SystmeDisplay(threading.Thread):
    screen = None
    running = True
    interval = 5
    info = None
    fetching_info = None

    def __init__(self, screen, *args, **kwargs):
        super(SystmeDisplay, self).__init__(*args, **kwargs)
        self.screen = screen

    def kill(self):
        self.fetching_info.kill()
        self.running = False

    def print_next(self, message, position):
        self.screen.animate_clear().print_clear(message, position)
        return self