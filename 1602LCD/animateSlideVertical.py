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

    # test moving up
    animation_screen.print_clear("screenx\nLcdSmartController\ntest\nsliding up\nand\nclear","center")
    time.sleep(2)
    animation_screen.slide_up(velocity)

    animation_screen.print_clear("Done", "center")
    time.sleep(1)

    # # test moving up
    animation_screen.print_clear("screenx\nLcdSmartController\ntest\nsliding down\nand\nclear","center")
    time.sleep(2)
    animation_screen.slide_down(velocity)
    animation_screen.print_clear("Done", "center")
    time.sleep(1)

    animation_screen.print_clear("screenx\nLcdSmartController\ntest\nsliding down\nand\nclear","center")
    animation_screen.move_down().move_down().refresh()
    time.sleep(3)
    animation_screen.slide_down(velocity)
    animation_screen.print_clear("Done", "center")
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