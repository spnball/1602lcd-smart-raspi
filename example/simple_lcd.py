#!/usr/bin/python

# Set library directory
import sys, os
sys.path.insert(0, "%s/../lib" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdSmartDriver import LcdSmartDriver, LcdVirtualRegistry
import time

# ------------------------#
#      Action start       #
# ------------------------#

registry = LcdVirtualRegistry()
registry.simulate = True

LcdThreading = LcdSmartDriver(registry=registry, name='a')
LcdThreading.start()
registry.backlight = 0
registry.buff = "     Hello      \n     World      "
time.sleep(10)

registry.buff = " Test to change \n   the world    "
time.sleep(3)

registry.backlight = 1
time.sleep(0.3)

registry.killed = True
LcdThreading.join()
