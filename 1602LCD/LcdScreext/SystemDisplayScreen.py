from Lcd.LcdScreenControl import LcdScreenControl

class SystemDisplayScreen(LcdScreenControl, object):
    mod_screen = {}
    running = True

    def __init__(self, *args, **kwargs):
        super(SystemDisplayScreen, self).__init__(*args, **kwargs)

    def add_system_screen(self, module_name):
        if module_name not in self.mod_screen:
            screen_id = self.add_screen()

            mod = __import__(module_name)
            class_obj = getattr(mod, module_name)

            self.mod_screen[module_name] = {
                'mod': class_obj(self.get_screen(screen_id)),
                'screen_id': screen_id
            }

            self.mod_screen[module_name]['mod'].start()

            return True

        return False

    def set_system_screen(self, module_name):
        self.set_screen(self.mod_screen[module_name]['screen_id'])
        return self

    def kill(self):
        self.running = False
        super(SystemDisplayScreen, self).kill()
        for mod, screen_info in self.mod_screen.iteritems():
            screen_info['mod'].kill()
