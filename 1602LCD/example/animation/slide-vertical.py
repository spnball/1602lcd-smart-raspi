#!/usr/bin/python

# Set library directory
import sys, os, traceback
sys.path.insert(0, "%s/../../lib/Lcd" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdDriver import LcdSize, LcdPin
from LcdSmartController import LcdSmartController
import time


try:
    lcdx = LcdSmartController(
        lcdSize = LcdSize(),
        lcdPin  = LcdPin(),
        simulate = True)

    velocity = 0.2

    # test moving up
    screen = lcdx.getScreen()
    screen.printClear("screenx\nLcdSmartController\ntest\nsliding up\nand\nclear","center")
    time.sleep(2)
    screen.slideUp(velocity)

    screen.printClear("Done", "center")
    time.sleep(1)

    # # test moving up
    screen.printClear("screenx\nLcdSmartController\ntest\nsliding down\nand\nclear","center")
    time.sleep(2)
    screen.slideDown(velocity)
    screen.printClear("Done", "center")
    time.sleep(1)

    screen.printClear("screenx\nLcdSmartController\ntest\nsliding down\nand\nclear","center")
    screen.moveDown().moveDown().refresh()
    time.sleep(3)
    screen.slideDown(velocity)
    screen.printClear("Done", "center")
    time.sleep(1)

    lcdx.kill()

except:
    lcdx.kill()
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60