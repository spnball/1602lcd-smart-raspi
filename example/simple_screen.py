#!/usr/bin/python

# Set library directory
import sys, os
sys.path.insert(0, "%s/../lib" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdSmartDriver import LcdSize, LcdPin
from LcdSmartController import LcdSmartController
import time


lcdx = LcdSmartController(
    lcdSize = LcdSize(), 
    lcdPin  = LcdPin(), 
    simulate = True)

screenx = lcdx.getScreen()
screenx.backlightOn()
screenx.printClear("")
time.sleep(1)
screenx.printClear("screenx\nLcdSmartController","center")
screenx.backlightBlink()
time.sleep(5)
screenx.backlightOff()
time.sleep(1)
lcdx.kill()
