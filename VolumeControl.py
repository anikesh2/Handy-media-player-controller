# 4th
# Gesture's Function Here
import cv2
import numpy as np
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import SendControl


class VolumeControl:

    # using our pycaw module for accessing audio of device's
    detector = htm.handDetector()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volRange = volume.GetVolumeRange()
    control = SendControl.Control()

    def __init__(
        self,
        minVol=volRange[0],
        maxVol=volRange[1],
        vol=0,
        volBar=400,
        volPer=0,
        area=0,
        colorVol=(255, 0, 0),
        img="",
        lmList=None,
        bbox=None,
    ):

        self.minVol = minVol
        self.maxVol = maxVol
        self.vol = vol
        self.volBar = volBar
        self.volPer = volPer
        self.area = area
        self.colorVol = colorVol
        self.img = self.detector.findHands(img)
        self.lmList, self.bbox = self.detector.findPosition(self.img)
        # self.detector.fps(self.img)

    # desgin ke liye hai

    def draw_volDetails(self, img):
        cv2.rectangle(self.img, (50, int(self.volBar)),
                      (85, 400), (255, 0, 0), -1)
        cv2.putText(
            self.img,
            f"{int(self.volPer)} %",
            (40, 450),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 0, 0),
            3,
        )
        cVol = int(self.volume.GetMasterVolumeLevelScalar() * 100)
        cv2.putText(
            self.img,
            f"Vol Set: {int(cVol)}",
            (400, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            self.colorVol,
            3,
        )

    # main fucntion

    def Vol_up_down(self):
        # img = self.detector.findHands(img)
        # lmList, bbox = self.detector.findPosition(self.img, draw=True)
        if len(self.lmList) != 0:

            # Filter ke liye
            self.area = (
                (self.bbox[2] - self.bbox[0]) *
                (self.bbox[3] - self.bbox[1]) // 100
            )

            if 250 < self.area < 1000:

                # Distance Betweeen Index and Thumb
                length, img, lineInfo = self.detector.findDistance(
                    4, 8, self.img)

                # Convert Volume to Sys vol setting
                self.volBar = np.interp(length, [50, 200], [400, 150])
                self.volPer = np.interp(length, [50, 200], [0, 100])

                # Reduce Resolution To Make in Smoother
                smoothness = 10
                self.volPer = smoothness * round(self.volPer / smoothness)

                # checks which fingers are up (if up return 1 else return 0)
                fingers = self.detector.fingersUp()
                # print(fingers)  # -> [thumb-f, first-f, middle-f, ring-f, pinky-f]

                if ((fingers[4] == 0 and fingers[3] == 0) and fingers[2] == 0):
                    self.volume.SetMasterVolumeLevelScalar(
                        self.volPer / 100, None)
                    cv2.circle(
                        img, (lineInfo[4], lineInfo[5]
                              ), 15, (0, 255, 0), cv2.FILLED
                    )
                    self.colorVol = (0, 255, 0)
                else:
                    self.colorVol = (255, 0, 0)

        self.draw_volDetails(self.img)

    def unMute_mute(self):
        if len(self.lmList) != 0:

            fingers = self.detector.fingersUp()

            if 250 < self.area < 1000:

                # un-mute & mute if thumb moved
                t, i, m, r, p = fingers
                self.control.press_key(
                    state=(t == 0 and ((i == 1 and m == 1) and (r == 1 and p == 1))), key="m")

    def pause_play(self):
        # play and pause if first finger is down
        if len(self.lmList) != 0:

            fingers = self.detector.fingersUp()

            if 250 < self.area < 1000:

                # un-mute & mute if thumb moved
                t, i, m, r, p = fingers
                self.control.press_space(
                    state=((t == 1 and i == 0) and ((m == 1 and r == 1) and p == 1)))

    def backwrd_10(self):
        if len(self.lmList) != 0:

            fingers = self.detector.fingersUp()

            if 250 < self.area < 1000:
                t, i, m, r, p = fingers
                self.control.press_key(
                    state=(((i == 1 and m == 1) and r == 1) and (p == 0 and t == 0)), key="{LEFT}")

    def forwrd_10(self):
        if len(self.lmList) != 0:

            fingers = self.detector.fingersUp()

            if 250 < self.area < 1000:
                t, i, m, r, p = fingers
                self.control.press_key(state=((i == 1 and m == 1) and (
                    r == 0 and (p == 0 and t == 0))), key="{RIGHT}")
