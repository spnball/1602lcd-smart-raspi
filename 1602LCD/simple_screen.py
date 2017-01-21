#!/usr/bin/python

# Set library directory
import sys
import traceback

# Import library
from Library.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry
from Library.Lcd.LcdScreen import LcdScreen
import time


try:
    registry = LcdVirtualRegistry()
    lcdx = LcdScreen(registry)

    screenx = []
    screen_id = [
        lcdx.get_screen_id(),
        lcdx.add_screen()
    ]

    for sid in screen_id:
        screenx.append(lcdx.get_screen(sid))

    screenx[1].printClear("Hello\nworld")

    screenx[0].backlightOn()
    screenx[0].printClear("screenx\nLcdSmartController","center")
    screenx[0].backlightBlink()
    time.sleep(2)

    lcdx.set_screen(screen_id[1]);
    time.sleep(2)

    lcdx.set_screen(screen_id[0]);
    time.sleep(1)
    screenx[0].backlightOff()
    time.sleep(0.2)

except KeyboardInterrupt:
    pass

except Exception:
    print '-' * 60
    traceback.print_exc(file=sys.stdout)
    print '-' * 60

finally:
    lcdx.kill()