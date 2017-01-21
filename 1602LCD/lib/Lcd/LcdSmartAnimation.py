from LcdDriver import LcdDriver, LcdVirtualRegistry, LcdSize
from LcdScreenDisplay import LcdScreenDisplay
from collections import deque
import time

class LcdSmartAnimation:
    def __init__(self, lcdSize, lcdPin, simulate = False, debug = False):
        
        
        # Define registry
        self.registry      = LcdVirtualRegistry()
        self.registry.simulate = simulate
        self.registry.debug = debug
        self.registry.pin   = LcdPin() if lcdPin == None else lcdPin
        self.registry.size  = LcdSize() if lcdSize == None else lcdSize
        
        self.screenIncreasement = 0
        self.screenList = {}
        
        self.setScreen(self.addScreen())
        self.driver = LcdDriver(registry=self.registry, name='a')
        self.driver.start()
        
    def kill (self):
        self.registry.killed = True
        self.driver.join()
        
    def addScreen(self, screen = None):
        screenId = self.screenIncreasement
        if screen == None : 
            screen = LcdScreenDisplay(lcdSize = self.registry.size)
        self.screenIncreasement += 1
        self.screenList[screenId] = screen
        
        return screenId
    
    def setScreen(self, screenId = 0) :
        self.currentScreenId = screenId
        self.registry.virtualScreenId = screenId
        self.registry.updateBuffer(self.screenList[screenId])
        return self
        
    def getScreen(self, screenId = None):
        screenId = self.currentScreenId if screenId == None else screenId
        return self.screenList[screenId]
        
    def getScreenId(self) :
        return self.currentScreenId
        
