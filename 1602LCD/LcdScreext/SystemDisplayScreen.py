from Lcd.LcdScreenControl import LcdScreenControl

class SystemDisplayScreen(LcdScreenControl, object):
    mod_screen = {}
    running = True

    def __init__(self, *args, **kwargs):
        super(SystemDisplayScreen, self).__init__(*args, **kwargs)

    def getModName(self, name):
        modulePath = name.split('.')
        return modulePath[-1]

    def add_system_screen(self, module_name, screen=None):
        if module_name not in self.mod_screen:
            if screen is None:
                screen_id = self.add_screen()
            else:
                screen_id = self.add_screen(screen)

            class_name = self.getModName(module_name)
            mod = __import__(module_name, globals(), locals(), [class_name], 0)

            #
            class_obj = getattr(mod, class_name)

            self.mod_screen[class_name] = {
                'mod': class_obj(self.get_screen(screen_id)),
                'screen_id': screen_id
            }

            self.mod_screen[class_name]['mod'].start()

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
