from Properties.LcdSize import LcdSize
from collections import deque


class LcdScreenDisplay:
    def __init__(self, lcd_size):
        self.buff = deque([])
        self.lcd_size = lcd_size
        self.active_line = 0
        self.back_light = None
        
        self.display = "\n".join(self.get_display())
        self.back_light_off()
        
    def get_display(self):
        displayed = []
        start = self.active_line
        end = self.active_line + self.lcd_size.row
        
        length = len(self.buff)

        for i in range(start, end):
            if i < length:
                displayed.append(self.display_text(self.buff[i]))
            else:
                displayed.append(self.display_text(''))
            
        return displayed
        
    def display_text(self, line):
        eol_str = '' if len(line) >= self.lcd_size.column else ' ' * (self.lcd_size.column - len(line))
        return "%s%s" % (line[:self.lcd_size.column], eol_str)
        
    def refresh(self):
        self.display = "\n".join(self.get_display())
        return self

    def align_right(self, message):
        for i, line in enumerate(message):
            if len(line) >= self.lcd_size.column:
                continue
            message[i] = "%s%s" % (' ' * (self.lcd_size.column - len(line)), line)
        return self

    def align_center(self, message):
        for i, line in enumerate(message):
            if len(line) >= self.lcd_size.column:
                continue
            message[i] = "%s%s" % (' ' * ((self.lcd_size.column - len(line)) / 2), line)

    def write_buffer(self, raw_message, align='left'):
        message = raw_message.split("\n")

        # Set Alignment
        if align == 'right':
            self.align_right(message)
        elif align == 'center':
            self.align_center(message)

        for line in message:
            self.buff.append(line)

    def maxlen(self):
        maxlength = 0
        for i in range(self.active_line, self.active_line + self.lcd_size.row):
            length = len(self.buff[i])
            if maxlength < length:
                maxlength = length
        return maxlength

    def indent_length(self, line):
        count = 0
        for j in range(0, len(self.buff[line]) - 1):
            if self.buff[line][j] != ' ':
                break
            count += 1
        return count

    def shift_left(self, end=None):
        for i in range(self.active_line, self.active_line + self.lcd_size.row):
            if end is None or end > len(self.buff[i]):
                temp_buffer = self.buff[i]
            else:
                temp_buffer = "%s %s" % (self.buff[i][:end], self.buff[i][end:])
            self.buff[i] = temp_buffer[1:]
        return self

    def shift_right(self, begin=None):
        for i in range(self.active_line, self.lcd_size.row):
            if begin is None:
                self.buff[i] = " %s" % self.buff[i]
            else:
                self.buff[i] = "%s %s" % (self.buff[i][:begin], self.buff[i][begin:])
        return self

    def clear(self):
        self.buff.clear()
        self.refresh()
        self.active_line = 0
        return self
    
    def print_clear(self, message, position="left"):
        self.clear()
        self.write_buffer(message, position)
        self.refresh()
        return self
        
    def backlight_change(self):
        if self.back_light == 0:
            self.back_light_off()
        else:
            self.back_light_on()
            
    def back_light_on(self):
        self.back_light = 0
        return self
        
    def back_light_off(self):
        self.back_light = 1
        return self
