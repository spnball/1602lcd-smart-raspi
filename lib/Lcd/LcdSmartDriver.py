import Adafruit_CharLCD as LCD
import threading, time, math

class LcdSize :
    # Define LCD column and row size for 16x2 LCD.
    row = 2
    column = 16
    
class LcdPin :
    # Raspberry Pi pin configuration:
    lcd_rs        = 27,  # (15) Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 22,  # (13)
    lcd_d4        = 18,  # (22 - Red) 
    lcd_d5        = 23,  # (18 - Orange)
    lcd_d6        = 24,  # (16 - Yello)
    lcd_d7        = 25,  # (12 - Green)
    lcd_backlight = 17

class LcdVirtualRegistry :
    def __init__ (self) :
            
        self.pin = LcdPin()
        self.size = LcdSize()
        
        self.simulate = False
        self.debug = False
        self.buff = self.getEmptyBuffer()
        self.backlight = 1
        self.frequency = 0.1
        self.virtualScreenId = 0
        self.killed = False
        
    def getEmptyBuffer (self) :
        initBuff = []
        for i in range(1,self.size.row) :
            initBuff.append(' ' * self.size.column)
        return initBuff
        
class CurrentState :
    def __init__ (self) :
        self.buff = None
        self.backlight = None

class LcdSmartDriver(threading.Thread):
    def __init__(self, registry, *args, **kwargs):
        super(LcdSmartDriver,self).__init__(*args, **kwargs)
        
        # new LCD driver object
        self.lcd = LCD.Adafruit_CharLCD(
                           registry.pin.lcd_rs, registry.pin.lcd_en, 
                           registry.pin.lcd_d4, registry.pin.lcd_d5, 
                           registry.pin.lcd_d6, registry.pin.lcd_d7,
                           registry.size.column, registry.size.row , 
                           registry.pin.lcd_backlight)

        # shared registry variable
        self.registry = registry
        
        self.currentState = CurrentState()
        self.simulateReady = False
        self.lcd.clear()
        
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

