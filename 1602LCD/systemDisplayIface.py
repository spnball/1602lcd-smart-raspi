#!/usr/bin/python

# Set library directory
import sys
import traceback

# Import library
from LcdScreext.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry
from LcdScreext.SystemDisplayScreen import SystemDisplayScreen
from LcdScreext.SystemDisplay.NetIfaceDisplay import NetIfaceDisplay

import time


try:
    registry = LcdVirtualRegistry()
    screext = SystemDisplayScreen(registry)

    screext.add_system_screen("NetIfaceDisplay")
    screext.set_system_screen("NetIfaceDisplay")

    while True : time.sleep(3600)

    screext.kill()

except:
    screext.kill()
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60