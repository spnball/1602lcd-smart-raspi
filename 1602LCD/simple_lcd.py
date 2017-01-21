#!/usr/bin/python

# Set library directory
import sys
import time
import traceback

# Import library
from Library.Lcd.LcdDriver import LcdDriver
from Library.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry

# ------------------------#
#      Action start       #
# ------------------------#

registry = LcdVirtualRegistry()

try:
    registry.simulate = True
    registry.buff = ""

    LcdThreading = LcdDriver(registry=registry, name='a')
    LcdThreading.start()
    registry.back_light = 0
    registry.buff = "     Hello      \n     World      "
    time.sleep(3)

    registry.back_light = 1
    registry.buff = "    Turn off    \n   Back light   "
    time.sleep(3)

    registry.back_light = 0
    registry.buff = "    Turn on     \n   Back light   "
    time.sleep(3)

    registry.back_light = 1
    time.sleep(0.3)

    registry.killed = True

finally:
    registry.killed = True
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60
