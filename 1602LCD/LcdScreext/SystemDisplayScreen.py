import sys, os, time
sys.path.append("%s/SystemDisplay" % (os.path.dirname(os.path.realpath(__file__))))


from LcdScreenControl import LcdScreenControl


class SystemDisplayScreen(LcdScreenControl, object) :
    def __init__(self, *args, **kwargs):
        super(SystemDisplayScreen,self).__init__(*args, **kwargs)
        self.running = True
        self.modScreen = {}

    def addSystemScreen(self, moduleName):
        if moduleName not in self.modScreen:
            screenId = self.addScreen()

            mod = __import__(moduleName)
            classObj = getattr(mod, moduleName)

            self.modScreen[moduleName] = {
                'mod' : classObj(self.getScreen(screenId)),
                'screenId' : screenId
            }


            self.modScreen[moduleName]['mod'].start()

            return True

        return False

    def setSystemScreen(self, moduleName):
        self.setScreen(self.modScreen[moduleName]['screenId'])
        return self

    def kill(self):
        self.running = False
        super(SystemDisplayScreen, self).kill()
        for mod, screenInfo in self.modScreen.iteritems():
            screenInfo['mod'].kill()