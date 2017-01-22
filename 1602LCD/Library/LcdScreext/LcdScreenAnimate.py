from LcdScreenDisplay import LcdScreenDisplay
from time import sleep

class LcdScreenAnimate(LcdScreenDisplay, object) :
    def moveDown(self):
        if len(self.buff) - self.activeLine <= self.lcdSize.row :
            return self
        self.activeLine += 1
        return self
        
    def moveUp(self):
        if self.activeLine > 0 :
            self.activeLine -= 1
        return self

    def printClear(self, message, align = 'left'):
        return self.clear().writeBuffer(message, align).refresh()
        
    def backlightBlink(self, time = 3, period = 0.5):
        for i in range(0, 2 * time) :
            self.backlightChange()
            sleep(period)
        return self
        
    def slideUp(self, time = 0.2):
        for i in range(0, self.lcdSize.row) :
            self.buff.append("")

        outputLengh = len(self.buff)
        while self.activeLine < outputLengh - self.lcdSize.row :
            self.moveDown().refresh()
            sleep(time)

        self.clear().refresh()
        return self
    
    def slideDown(self, time = 0.2):
        while self.activeLine > 0 :
            self.moveUp().refresh()
            sleep(time)
        
        for i in range(0, self.lcdSize.row) :
            self.buff.appendleft("")
            self.refresh()
            sleep(time)
            
        self.clear().refresh()
        return self

    def slideOutLeft(self, time):
        for i in range(0, self.maxlen()) :
            self.shiftLeft().refresh()
            sleep(time)
        return self.clear();

    def minLeftSpacelen(self):
        min = 0
        for i in range(self.activeLine, self.activeLine + self.lcdSize.row):
            indent = self.indentLength(i)
            if min > indent :
                min = indent
        return min

    def slideOutRight(self, time):
        for i in range(0, self.lcdSize.column - self.minLeftSpacelen()) :
            self.shiftRight().refresh()
            sleep(time)
        return self.clear()