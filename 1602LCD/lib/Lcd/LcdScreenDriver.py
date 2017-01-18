from LcdSmartDriver import LcdSmartDriver, LcdVirtualRegistry
from collections import deque
    
class LcdScreenDriver :
    def __init__(self, lcdSize):
        self.buff = deque([])
        self.lcdSize = lcdSize
        self.activeLine = 0
        self.backlight = None
        
        self.display = "\n".join(self.getDisplay())
        self.backlightOff()
        
    def getDisplay(self):
        displayed = []
        start = self.activeLine
        end   = self.activeLine + self.lcdSize.row
        
        length = len(self.buff)
        
        for i in range(start, end) :
            if i < length : 
                displayed.append(self.displayText(self.buff[i]))
            else :
                displayed.append(self.displayText(''))
            
        return displayed
        
    def displayText(self, line):
        eolStr = '' if len(line) >= self.lcdSize.column else ' ' * (self.lcdSize.column - len(line))
        return "%s%s" % (line[:self.lcdSize.column], eolStr)
        
    def refresh(self):
        self.display = "\n".join(self.getDisplay())
        return self
        
    def writeBuffer(self, message):
        for line in message :
            self.buff.append(line)
        return self
        
    def flushLine(self, screen = None):
        if len(self.buff) > 0 :
            newline = self.buff.popleft()
            
        return self
        
    def clear(self, screen = None):
        self.buff.clear()
        self.refresh()
        self.activeLine = 0
        return self
    
    def printClear(self, message, screen = None):
        self.clear()
        self.writeBuffer(message, screen)
        self.refresh()
        return self
        
    def backlightChange(self) :
        if self.backlight == 0 :
            self.backlightOff()
        else :
            self.backlightOn()
            
    def backlightOn(self):
        self.backlight = 0
        return self
        
    def backlightOff(self):
        self.backlight = 1
        return self
