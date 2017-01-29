#!/usr/bin/python

import sys
import traceback

# Import library
from LcdScreext.Lcd.Properties.LcdVirtualRegistry import LcdVirtualRegistry
from LcdScreext.Lcd.LcdScreenControl import LcdScreenControl
from LcdScreext.Lcd.LcdScreenAnimate import LcdScreenAnimate
import time


try:
    registry = LcdVirtualRegistry()

    velocity = 0.2

    screext = LcdScreenControl(registry)
    animation_screen = LcdScreenAnimate(registry.size)
    screen_id = screext.add_screen(animation_screen)
    screext.set_screen(screen_id)

    animation_screen.back_light_on()

    ## test slide-out right
    animation_screen.print_clear("screenx\nLcdSmartController", "center")
    time.sleep(1)
    animation_screen.slide_out_right(velocity)
    animation_screen.print_clear("Done", "center")
    time.sleep(1)

    animation_screen.print_clear("screenx\nSmart", "center")
    time.sleep(1)
    animation_screen.slide_out_right(velocity)
    animation_screen.print_clear("Done", "center")
    time.sleep(1)


    ## test slide-out left
    animation_screen.print_clear("screenx\nLcdSmartController","center")
    time.sleep(1)
    animation_screen.slide_out_left(velocity)
    animation_screen.print_clear("Done", "center")
    time.sleep(1)

    animation_screen.print_clear("screenx\nSmart", "center")
    time.sleep(1)
    animation_screen.slide_out_left(velocity)
    animation_screen.print_clear("Done", "center")
    time.sleep(1)

    animation_screen.back_light_off()
    time.sleep(1)
    screext.kill()

except KeyboardInterrupt:
    pass


except Exception:
    print '-' * 60
    traceback.print_exc(file=sys.stdout)
    print '-' * 60

finally:
    screext.kill()