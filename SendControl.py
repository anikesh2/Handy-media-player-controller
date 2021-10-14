# Send control to VLC, called By Volume-Control.py
import win32com.client
from pynput.keyboard import Key, Controller


class Control:

    def press_key(self, state, key):
        if state:
            wsh = win32com.client.Dispatch("WScript.Shell")
            wsh.AppActivate("vlc")  # select another application
            wsh.SendKeys(key)  # send the keys you want

    def press_space(self, state):
        if state:
            keyboard = Controller()
            keyboard.press(Key.space)
            keyboard.release(Key.space)
