# 2nd
# Check vlc and Camera is connected OR not if/ if-not send status
import os
import winapps
import subprocess
import Volume_main


class VlcChecker:

    vl = Volume_main.vol_main()

    def getPossibleExePaths(self, appPath):
        pattern = appPath + ":*exe"
        returned = subprocess.check_output(['where', pattern]).decode('utf-8')
        listOfPaths = filter(None, returned.split(os.linesep))
        return [i.strip() for i in list(listOfPaths)]

    def getAppPath(self, appName):
        for app in winapps.search_installed(appName):
            installPath = str(app.install_location)
            if installPath and installPath != "None":
                return installPath
        return False

    def path(self, name):
        path = self.getAppPath(name)
        if not path:
            return False
        else:
            path_list = self.getPossibleExePaths(path)
            return path_list[2]

    def start(self, name):
        path = self.path(name)
        if not path:
            return False
        else:
            # self.vol_main.start_vol_Control()
            os.startfile(path)
            self.vl.vol_m()

    def process_exists(self, process_name):
        progs = str(subprocess.check_output('tasklist'))
        if process_name in progs:
            # self.vol.end_vol_control()
            return True
        else:
            return False

    def end(self):
        if self.process_exists(process_name="vlc"):
            os.system("TASKKILL /F /IM vlc.exe")
