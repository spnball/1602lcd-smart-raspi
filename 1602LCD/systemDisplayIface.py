#!/usr/bin/python

# Set library directory
import sys
import traceback

# Import library
from LcdScreext.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry
from LcdScreext.SystemDisplayScreen import SystemDisplayScreen
from LcdScreext.Lcd.LcdScreenAnimate import LcdScreenAnimate

import time


try:
    registry = LcdVirtualRegistry()
    screext = SystemDisplayScreen(registry)
    animate_screen = LcdScreenAnimate(registry.size)

    animate_screen.back_light_off()
    screext.add_system_screen("LcdScreext.SystemDisplay.NetIfaceDisplay", animate_screen)
    screext.set_system_screen("NetIfaceDisplay")
    animate_screen.back_light_blink()

    while True : time.sleep(3600)

    screext.kill()

except:
    screext.kill()
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60