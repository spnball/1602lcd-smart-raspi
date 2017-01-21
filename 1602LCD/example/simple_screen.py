#!/usr/bin/python

# Set library directory
import sys, os, traceback
sys.path.insert(0, "%s/../lib/Lcd" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdDriver import LcdSize, LcdPin
from LcdSmartAnimation import LcdSmartAnimation
import time


try:
    lcdx = LcdSmartAnimation(
        lcdSize = LcdSize(),
        lcdPin  = LcdPin(),
        simulate = True)

    screenx = []
    screenId = [
        lcdx.getScreenId(),
        lcdx.addScreen()
    ]

    for sid in screenId:
        screenx.append(lcdx.getScreen(sid))

    screenx[1].printClear("Hello\nworld")

    screenx[0].backlightOn()
    screenx[0].printClear("screenx\nLcdSmartAnimation","center")
    screenx[0].backlightBlink()
    time.sleep(2)

    lcdx.setScreen(screenId[1]);
    time.sleep(2)

    lcdx.setScreen(screenId[0]);
    time.sleep(1)
    screenx[0].backlightOff()
    time.sleep(0.2)
    lcdx.kill()

except:
    lcdx.kill()
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60