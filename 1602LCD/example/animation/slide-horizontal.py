#!/usr/bin/python

# Set library directory
import sys, os, traceback
sys.path.insert(0, "%s/../../lib/Lcd" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdSmartDriver import LcdSize, LcdPin
from LcdSmartController import LcdSmartController
import time


try:
    lcdx = LcdSmartController(
        lcdSize = LcdSize(),
        lcdPin  = LcdPin(),
        simulate = True)

    velocity = 0.1
    screen = lcdx.getScreen()
    screen.backlightOn()

    ## test slide-out right
    screen.printClear("screenx\nLcdSmartController", "center")
    time.sleep(1)
    screen.slideOutRight(velocity)
    screen.printClear("Done", "center")
    time.sleep(1)

    screen.printClear("screenx\nSmart", "center")
    time.sleep(1)
    screen.slideOutRight(velocity)
    screen.printClear("Done", "center")
    time.sleep(1)


    ## test slide-out left
    screen.printClear("screenx\nLcdSmartController","center")
    time.sleep(1)
    screen.slideOutLeft(velocity)
    screen.printClear("Done", "center")
    time.sleep(1)

    screen.printClear("screenx\nSmart", "center")
    time.sleep(1)
    screen.slideOutLeft(velocity)
    screen.printClear("Done", "center")
    time.sleep(1)

    screen.backlightOff()
    lcdx.kill()

except:
    screen.backlightOff()
    lcdx.kill()
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60