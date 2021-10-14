# 3rd
# Called Volume-Control.py and send camera img form camera to Volume-Control.py
import pyautogui
import VolumeControl
import cv2
import Status


class vol_main:

    def vol_m(self):

        # setting window size
        wCam, hCam = 640, 480

        # calling cv2 to take of camera access from device
        cap = cv2.VideoCapture(0)
        cap.set(3, wCam)
        cap.set(4, hCam)

        while True:
            success, img = cap.read()
            control = VolumeControl.VolumeControl(img=img)
            window_name = "Camera Control"  # setting our camera window name
            width, height = pyautogui.size()
            cv2.namedWindow(window_name)
            cv2.moveWindow(window_name, int(width // 1.55), 0)
            cv2.putText(img, f'Press Q to EXIT', (350, 450),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

            control.Vol_up_down()
            control.unMute_mute()
            control.pause_play()
            control.forwrd_10()
            control.backwrd_10()
            cv2.imshow(window_name, img)
            k = cv2.waitKey(1)

            if k == ord('q') or k == ord('Q') or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                vol = Status.VlcChecker()
                vol.end()
                break

        cap.release()
        cv2.destroyAllWindows()
