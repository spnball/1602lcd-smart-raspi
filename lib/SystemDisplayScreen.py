from LcdSmartController import LcdSmartController
import collections

class SystemDisplayScreen(LcdSmartController, object) :
    def __init__(self, *args, **kwargs):
        super(SystemDisplayScreen,self).__init__(*args, **kwargs)

        self.modScreen = {}

    def addSystemScreen(self, moduleName):
        if moduleName not in self.modScreen:
            screenId = self.addScreen()

            mod = __import__(moduleName)
            self.modScreen[moduleName] = {
                'mod' : mod(self.getScreen(screenId)),
                'screenId' : screenId
            }


    def setSystemScreen(self, moduleName):
        self.setScreen(self.modScreen[moduleName]['screenId'])
        return self

    def kill(self):
        super(SystemDisplayScreen, self).kill()
        for screen in self.modScreen:
            screen.kill()