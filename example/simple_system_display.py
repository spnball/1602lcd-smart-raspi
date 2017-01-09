#!/usr/bin/python

# Set library directory
import sys, os, traceback
sys.path.append("%s/../lib" % (os.path.dirname(os.path.realpath(__file__))))
sys.path.append("%s/../lib/Lcd" % (os.path.dirname(os.path.realpath(__file__))))
sys.path.append("%s/../lib/SystemDisplay" % (os.path.dirname(os.path.realpath(__file__))))

# Import library
from LcdSmartDriver import LcdSize, LcdPin
from SystemDisplayScreen import SystemDisplayScreen
from time import sleep

try:
    lcdx = SystemDisplayScreen(
        lcdSize=LcdSize(),
        lcdPin=LcdPin(),
        simulate=True)

    lcdx.addSystemScreen("NetIfaceDisplay")
    lcdx.setSystemScreen("NetIfaceDisplay")

    sleep(5)
    lcdx.kill()

except:
    lcdx.kill()
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60