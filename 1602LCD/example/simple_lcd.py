#!/usr/bin/python

# Set library directory
import sys
import os
import traceback
import time

sys.path.insert(0, "%s/../lib/Lcd" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdDriver import LcdDriver, LcdVirtualRegistry

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

except:
    registry.killed = True
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60
