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

    def maxlen(self):
        max = 0
        for i in range(self.activeLine, self.activeLine + self.lcdSize.row):
            length = len(self.buff[i]);
            if max < length :
                max = length
        return max

    def indentLength(self, line):
        count = 0
        for j in range(0, len(self.buff[line]) - 1):
            if self.buff[line][j] != ' ':
                break
            count += 1
        return count

    def shiftLeft(self, end = None):
        for i in range(self.activeLine, self.activeLine + self.lcdSize.row) :
            if end == None or end > len(self.buff[i]):
                tempBuffer = self.buff[i]
            else :
                tempBuffer = "%s %s" % (self.buff[i][:end],self.buff[i][end:])
            self.buff[i] = tempBuffer[1:]
        return self

    def shiftRight(self, begin = None):
        for i in range(self.activeLine, self.lcdSize.row) :
            if begin == None :
                self.buff[i] = " %s" % (self.buff[i])
            else :
                self.buff[i] = "%s %s" % (self.buff[i][:begin],self.buff[i][begin:])
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
