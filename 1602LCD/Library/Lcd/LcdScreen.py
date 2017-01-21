from LcdDriver import LcdDriver
from LcdSmartScreenDriver import LcdSmartScreenDriver


class LcdScreen:
    driver = None
    registry = None
    screen_increment = 0
    screen_list = {}
    current_screen_id = 0

    def __init__(self, registry, driver=None):
        # Define registry
        self.registry = registry
        self.set_screen(self.add_screen())

        self.driver = LcdDriver(registry=self.registry) if driver is None else driver
        self.driver.start()
        
    def kill(self):
        self.registry.killed = True
        self.driver.join()
        
    def add_screen(self, screen=None):
        screen_id = self.screen_increment
        if screen is None:
            screen = LcdSmartScreenDriver(lcdSize=self.registry.size)
        self.screen_increment += 1
        self.screen_list[screen_id] = screen
        
        return screen_id
    
    def set_screen(self, screen_id=0):
        self.current_screen_id = screen_id
        self.registry.virtualscreen_id = screen_id
        self.registry.update_buffer(self.screen_list[screen_id])
        return self
        
    def get_screen(self, screen_id=None):
        screen_id = self.current_screen_id if screen_id is None else screen_id
        return self.screen_list[screen_id]
        
    def get_screen_id(self):
        return self.current_screen_id
