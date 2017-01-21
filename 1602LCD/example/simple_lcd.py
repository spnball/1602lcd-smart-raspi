#!/usr/bin/python

# Set library directory
import sys, os, traceback
sys.path.insert(0, "%s/../lib/Lcd" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdSmartDriver import LcdSmartDriver, LcdVirtualRegistry
import time

# ------------------------#
#      Action start       #
# ------------------------#

registry = LcdVirtualRegistry()

try:
    registry.simulate = True

    LcdThreading = LcdSmartDriver(registry=registry, name='a')
    LcdThreading.start()
    registry.backlight = 0
    registry.buff = "     Hello      \n     World      "
    time.sleep(10)

    registry.buff = " Test changing  \n   the world    "
    time.sleep(3)

    registry.backlight = 1
    time.sleep(0.3)

    registry.killed = True
except:
    registry.killed = True
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60