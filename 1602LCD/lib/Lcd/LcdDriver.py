import threading
import time
import math


class LcdSize:
    # Define LCD column and row size for 16x2 LCD.
    row = 2
    column = 16

    def __init__(self):
        pass


class LcdPin:
    # Raspberry Pi pin configuration:
    lcd_rs = 12,  # (15) Note this might need to be changed to 21 for older revision Pi's.
    lcd_en = 16,  # (13)
    lcd_d4 = 26,  # (22 - Red)
    lcd_d5 = 19,  # (18 - Orange)
    lcd_d6 = 13,  # (16 - Yello)
    lcd_d7 = 6,   # (12 - Green)
    lcd_back_light = 20

    def __init__(self):
        pass


class LcdVirtualRegistry:
    pin = LcdPin()
    size = LcdSize()

    simulate = False
    debug = False

    back_light = 1
    frequency = 0.025
    virtual_screen_id = 0
    killed = False

    def __init__(self):
        self.buff = self.get_empty_buffer()

    def update_buffer(self, buff):
        self.buff = buff
        return self

    def update_back_light(self, value):
        self.back_light = value
        return self

    def get_empty_buffer(self):
        init_buff = []
        for i in range(1, self.size.row):
            init_buff.append(' ' * self.size.column)
        return init_buff


class CurrentState:
    def __init__(self):
        self.buff = None
        self.back_light = None


class LcdDriver(threading.Thread):
    registry = None
    simulate_ready = False
    current_state = CurrentState()
    lcd = None

    def __init__(self, registry, *args, **kwargs):
        super(LcdDriver, self).__init__(*args, **kwargs)

        # shared registry variable
        self.registry = registry

        try:
            import Adafruit_CharLCD as LCD

            # new LCD driver object
            self.lcd = LCD.Adafruit_CharLCD(
                    registry.pin.lcd_rs, registry.pin.lcd_en,
                    registry.pin.lcd_d4, registry.pin.lcd_d5,
                    registry.pin.lcd_d6, registry.pin.lcd_d7,
                    registry.size.column, registry.size.row,
                    registry.pin.lcd_back_light)
            self.lcd.clear()

        except ImportError:
            self.registry.simulate = True
            self.lcd = None
            print "simulator is enabled because cannot import Adafruit_CharLCD"
        except:
            pass

    def simulate_display(self):
        registry = self.registry
        lcd_row = registry.size.row
        lcd_column = registry.size.column
        current_state = self.current_state

        if current_state.buff is None:
            return self

        if current_state.back_light == 0:
            print "\033[1m",
        if self.simulate_ready is True and registry.debug is False:
            print "\033[F\r" * (lcd_row + 2),

        screen_name = "0x%02X" % registry.virtual_screen_id
        print "\r*=%s %s %s=*" % (
            '=' * int((lcd_column - len(screen_name) - 2)/2),
            screen_name,
            '=' * int(math.ceil((lcd_column - len(screen_name) - 2)/2)))

        current_lines = current_state.buff.split("\n")
        for line in current_lines:
            print "| %s |" % line

        print "*=%s=*" % ('=' * lcd_column)
        if current_state.back_light == 0:
            print "\033[0m",
            
        self.simulate_ready = True
        return self

    def update(self):
        simulate = False
        registry = self.registry
        current_state = self.current_state

        if isinstance(registry.buff, basestring):
            registry_buff = registry.buff
        else:
            registry_buff = registry.buff.display
             
        if current_state.buff != registry_buff:
            current_state.buff = registry_buff

            if self.lcd is not None:
                self.lcd.set_cursor(0, 0)
                self.lcd.message(current_state.buff)
            simulate = True
        
        if isinstance(registry.buff, basestring):
            back_light = registry.back_light
        else:
            back_light = registry.buff.back_light
            
        if current_state.back_light != back_light:
            current_state.back_light = back_light
            if self.lcd is not None:
                self.lcd.set_back_light(current_state.back_light)
            simulate = True

        if simulate and (registry.simulate or registry.debug):
            self.simulate_display()
        
        return self
        
    def run(self):
        registry = self.registry

        if registry.debug or registry.simulate:
            print threading.current_thread(), ' LCD driver start.'
            
        while not registry.killed:
            self.update()
            time.sleep(registry.frequency)
            
        print threading.current_thread(), ' LCD driver exit.'
