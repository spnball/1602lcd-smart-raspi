#!/usr/bin/python

import sys
import traceback

# Import library
from LcdScreext.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry
from LcdScreext.Lcd.LcdScreen import LcdScreen
from LcdScreext.Lcd.LcdScreenAnimate import LcdScreenAnimate
import time


try:
    registry = LcdVirtualRegistry()

    lcdx = LcdScreen(registry)
    screext = LcdScreenAnimate(registry.size)

    screen_id = lcdx.add_screen(screext)
    lcdx.set_screen(screen_id)

    screext.print_clear("Screen\nBlink", "center")
    screext.back_light_blink();

    time.sleep(1)

except KeyboardInterrupt:
    pass

except Exception:
    print '-' * 60
    traceback.print_exc(file=sys.stdout)
    print '-' * 60

finally:
    lcdx.kill()