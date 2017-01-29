#!/usr/bin/python

# Set library directory
import sys
import traceback

# Import library
from LcdScreext.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry
from LcdScreext.Lcd.LcdScreenControl import LcdScreenControl
import time


try:
    registry = LcdVirtualRegistry()
    lcdx = LcdScreenControl(registry)

    screenx = []
    screen_id = [
        lcdx.get_screen_id(),
        lcdx.add_screen(),
        lcdx.add_screen()
    ]

    for sid in screen_id:
        screenx.append(lcdx.get_screen(sid))

    screenx[1].print_clear("Hello\nlongggggg text-test")
    screenx[2].print_clear("Center\nVery long text-test", "right")

    screenx[0].back_light_on()
    screenx[0].print_clear("screenx\nLcdSmartController", "center")
    time.sleep(2)

    lcdx.set_screen(screen_id[1]);
    time.sleep(2)

    lcdx.set_screen(screen_id[2]);
    time.sleep(2)

    lcdx.set_screen(screen_id[0]);
    time.sleep(1)
    screenx[0].back_light_off()
    time.sleep(0.2)

except KeyboardInterrupt:
    pass

except Exception:
    print '-' * 60
    traceback.print_exc(file=sys.stdout)
    print '-' * 60

finally:
    lcdx.kill()