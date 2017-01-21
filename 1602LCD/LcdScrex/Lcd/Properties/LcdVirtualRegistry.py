from LcdSize import LcdSize
from LcdPin import LcdPin


class LcdVirtualRegistry:
    pin = LcdPin()
    size = LcdSize()

    simulate = False
    debug = False

    back_light = 1
    frequency = 0.025
    virtual_screen_id = 0
    killed = False

    def __init__(self):
        self.buff = self.get_empty_buffer()

    def update_buffer(self, buff):
        self.buff = buff
        return self

    def update_back_light(self, value):
        self.back_light = value
        return self

    def get_empty_buffer(self):
        init_buff = []
        for i in range(1, self.size.row):
            init_buff.append(' ' * self.size.column)
        return init_buff