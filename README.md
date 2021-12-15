# VLC Media PLayer Controller Using Hand Gestures
I have used mediapipe Python library to recognize hand from camera and other framework like numpy, openCv, pycaw etc.<br>
The cv2 module will allow us to obtain the frames from the camera, over which we will perform the hand landmarks estimation by using the functionality exposed by the mediapipe module.<br>
<br>



To install the required python framework, simply copy-paste the following command in command prompt  <br>
***(Open CMD in same file where requirements.txt is located)*** <br>
***Install Python version 3.9.1***
```
pip install -r requirements.txt
```

We can control VLC media Player Functionally like Pause, Play, Fast-forward, backward, mute, Umute and we have added different gesture for different function <br>
***NOTE: THE VLC MEDIA PLAYER SHOULD ALREADY INSTALL ON THE DEVICE.***<br>
## Gesture to control different function 
mute / unmute            |  pause / play
:-------------------------:|:-------------------------:
<img src="vedios/mute.gif" width="400" height="250"> <br> | <img src="vedios/pause.gif" width="400" height="250">
<br>


Backwards 10 sec |     Forward 10 sec
:-------------------------:|:-------------------------:
<img src="vedios/backward-10s.gif" width="400" height="250"> <br> | <img src="vedios/forward-10s.gif" width="400" height="250">
<br>

| Volume up / down <br>|
| ------ |
|<img src="vedios/vol-up-down.gif" width="400" height="250"> <br> |

