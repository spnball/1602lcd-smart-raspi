from LcdScreenDisplay import LcdScreenDisplay
from time import sleep


class LcdScreenAnimate(LcdScreenDisplay, object):
    def move_down(self):
        if len(self.buff) - self.active_line <= self.lcd_size.row:
            return self
        self.active_line += 1
        return self
        
    def move_up(self):
        if self.active_line > 0:
            self.active_line -= 1
        return self

    def back_light_blink(self, time=3, period=0.5):
        for i in range(0, 2 * time):
            self.backlight_change()
            sleep(period)
        return self
        
    def slide_up(self, time=0.2):
        for i in range(0, self.lcd_size.row):
            self.buff.append("")

        output_lengh = len(self.buff)
        while self.active_line < output_lengh - self.lcd_size.row:
            self.move_down().refresh()
            sleep(time)

        self.clear().refresh()
        return self
    
    def slide_down(self, time=0.2):
        while self.active_line > 0:
            self.move_up().refresh()
            sleep(time)
        
        for i in range(0, self.lcd_size.row):
            self.buff.appendleft("")
            self.refresh()
            sleep(time)
            
        self.clear().refresh()
        return self

    def slide_out_left(self, time):
        for i in range(0, self.maxlen()):
            self.shift_left().refresh()
            sleep(time)
        return self.clear()

    def min_left_space_len(self):
        min_length = 0
        for i in range(self.active_line, self.active_line + self.lcd_size.row):
            indent = self.indent_length(i)
            if min_length > indent:
                min_length = indent
        return min_length

    def slide_out_right(self, time):
        for i in range(0, self.lcd_size.column - self.min_left_space_len()):
            self.shift_right().refresh()
            sleep(time)
        return self.clear()
