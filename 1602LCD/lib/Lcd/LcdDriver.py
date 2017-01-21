import threading, time, math


class LcdSize :
    # Define LCD column and row size for 16x2 LCD.
    row = 2
    column = 16


class LcdPin:
    def __init__(self):
        # Raspberry Pi pin configuration:
        self.lcd_rs = 12,  # (15) Note this might need to be changed to 21 for older revision Pi's.
        self.lcd_en = 16,  # (13)
        self.lcd_d4 = 26,  # (22 - Red)
        self.lcd_d5 = 19,  # (18 - Orange)
        self.lcd_d6 = 13,  # (16 - Yello)
        self.lcd_d7 = 6,  # (12 - Green)
        self.lcd_backlight = 20

class LcdVirtualRegistry :
    def __init__ (self) :

        self.pin = LcdPin()
        self.size = LcdSize()

        self.simulate = False
        self.debug = False
        self.buff = self.getEmptyBuffer()
        self.backlight = 1
        self.frequency = 0.025
        self.virtualScreenId = 0
        self.killed = False

    def updateBuffer(self, buff):
        self.buff = buff
        return self

    def updateBacklight(self, value):
        self.backlight = value
        return self

    def getEmptyBuffer (self) :
        initBuff = []
        for i in range(1,self.size.row) :
            initBuff.append(' ' * self.size.column)
        return initBuff
        
class CurrentState :
    def __init__ (self) :
        self.buff = None
        self.backlight = None

class LcdDriver(threading.Thread):
    def __init__(self, registry, *args, **kwargs):
        super(LcdDriver,self).__init__(*args, **kwargs)

        # shared registry variable
        self.registry = registry
        self.simulateReady = False

        try :
            import Adafruit_CharLCD as LCD

            # new LCD driver object
            self.lcd = LCD.Adafruit_CharLCD(
                               registry.pin.lcd_rs, registry.pin.lcd_en,
                               registry.pin.lcd_d4, registry.pin.lcd_d5,
                               registry.pin.lcd_d6, registry.pin.lcd_d7,
                               registry.size.column, registry.size.row ,
                               registry.pin.lcd_backlight)
            self.lcd.clear()

        except ImportError :
            self.registry.simulate = True
            self.lcd = None
            print "simulator is enabled because cannot import Adafruit_CharLCD"

        self.currentState = CurrentState()

    def simulateDisplay (self):
        if self.currentState.backlight == 0 :
            print "\033[1m",
        if self.simulateReady == True and self.registry.debug == False:
            print "\033[F\r" * (self.registry.size.row + 2),

        screenName = "0x%02X" % (self.registry.virtualScreenId)
        print "\r*=%s %s %s=*" % (
            '=' * int((self.registry.size.column - len(screenName) - 2)/2), 
            screenName,
            '='  * int(math.ceil((self.registry.size.column- len(screenName) - 2)/2) ))
        
        for line in self.currentState.buff.split("\n") :
            print "| %s |" % (line)
                
        print "*=%s=*" % ('=' * self.registry.size.column)
        if self.currentState.backlight == 0 :
            print "\033[0m",
            
        self.simulateReady = True
        return self

    def update(self):
        simulate = False
        registryBuff = None
        if isinstance(self.registry.buff, basestring) :
            registryBuff = self.registry.buff
        else :
            registryBuff = self.registry.buff.display
             
        if self.currentState.buff != registryBuff :
            self.currentState.buff = registryBuff
            if self.lcd != None:
                self.lcd.set_cursor(0,0)
                self.lcd.message(self.currentState.buff)
            simulate = True
        
        backlight = None
        if isinstance(self.registry.buff, basestring) :
            backlight = self.registry.backlight
        else :
            backlight = self.registry.buff.backlight
            
        if self.currentState.backlight != backlight :
            self.currentState.backlight = backlight
            if self.lcd != None:
                self.lcd.set_backlight(self.currentState.backlight)
            simulate = True

        if simulate and (self.registry.simulate or self.registry.debug) : 
            self.simulateDisplay()
        
        return self
        
    def run(self):
        if self.registry.debug or self.registry.simulate:
            print threading.current_thread(), ' LCD driver start.'
            
        while not self.registry.killed :
            self.update()
            time.sleep(self.registry.frequency)
            
        print threading.current_thread(), ' LCD driver exit.'

