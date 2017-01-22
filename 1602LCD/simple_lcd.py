#!/usr/bin/python

# Set library directory
import sys
import time
import traceback

# Import library
from Library.LcdScreext.LcdDriver import LcdDriver
from Library.LcdScreext.Properties.LcdVirtualRegistry import LcdVirtualRegistry

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
    time.sleep(1)

    registry.back_light = 1
    registry.buff = "    Turn off    \n   Back light   "
    time.sleep(1)

    registry.back_light = 0
    registry.buff = "    Turn on     \n   Back light   "
    time.sleep(1)

    registry.back_light = 1
    time.sleep(0.3)

except KeyboardInterrupt:
    pass

except:
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60

finally:
    registry.killed = True
