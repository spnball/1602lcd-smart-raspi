from LcdScreenDriver import LcdScreenDriver
from time import sleep

class LcdSmartScreenDriver(LcdScreenDriver, object) :
    def moveDown(self):
        if len(self.buff) - self.activeLine <= self.lcdSize.row :
            return self
        self.activeLine += 1
        return self
        
    def moveUp(self):
        if self.activeLine > 0 :
            self.activeLine -= 1
        return self
        
    def alignRight (self, message) :
        for i, line in enumerate(message):
            if len(line) >= self.lcdSize.column : 
                continue
            message[i] = "%s%s" % (' ' * (self.lcdSize.column - len(line)) , line)
        return self
    
    def alignCenter (self, message) :
        for i, line in enumerate(message):
            if len(line) >= self.lcdSize.column : 
                continue
            message[i] = "%s%s" % (' ' * ((self.lcdSize.column - len(line))/2) , line)

    def writeBuffer (self, rawMessage, align = 'left') :
        message = rawMessage.split("\n")
        
        # Set Alignment 
        if align == 'right' :
            self.alignRight(message);
        elif align == 'center' :
            self.alignCenter(message);
            
        return super(LcdSmartScreenDriver, self).writeBuffer(message)
        
    def printClear(self, message, align = 'left'):
        return self.clear().writeBuffer(message, align).refresh()
        
    def backlightBlink(self, time = 3, period = 0.5):
        for i in range(0, 2 * time) :
            self.backlightChange()
            sleep(period)
        return self
        
    def slideUp(self, time = 0.2):
        outputLengh = len(self.buff)
        while self.activeLine < outputLengh - self.lcdSize.row :
            self.moveDown().refresh()
            sleep(time)
        
        for i in range(0, self.lcdSize.ros - 1) :
            self.flushLine().refresh()
            sleep(time)
                
        self.clear().refresh()
        return self.buff['displayedLine']
    
    def slideDown(self, time = 0.2):
        while self.activeLine > 0 :
            self.moveUp().refresh()
            sleep(time)
        
        for i in range(0, self.lcdRows - 1) :
            self.getScreen(screen)['buff'].appendleft("")
            self.refresh()
            sleep(time)
            
        self.clear().refresh()
        return self
