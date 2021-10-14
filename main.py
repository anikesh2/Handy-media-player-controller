# 1st
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import Status as st
import cv2
import webbrowser
window = tk.Tk()
vlc = st.VlcChecker()

# title
window.title("Media PLayer Controller")

# window geometer & properties
window.geometry("600x400+0+0")
window.resizable(False, False)
window.config(bg="#8BD2B8")
window.tk.call('wm', 'iconphoto', window._w,
               tk.PhotoImage(file='html\\media.png'))

# To display Instruction
instruct_1 = tk.Label(
    window,
    text="Please Click on CHECK Button,To check Weather This devices Have VLC MEDIA PLAYER installed and Camera is "
         "available.",
    font=("Comic Sans MS", 15, "bold", "italic"),
    wraplength=550,
    justify="center",
    bg="#8BD2B8"
)

# ============== On click function for button =====================================

# check button


def url_call(url):
    webbrowser.open_new_tab(url)


def check_onClick():
    vlc_check = vlc.getAppPath(appName="vlc")
    cap = cv2.VideoCapture(0)
    #vlc_check = False

    if vlc_check != False:
        message_vlc_T = tk.Label(
            window,
            text="VLC Media Player Is Installed.         ",
            font=("Comic Sans MS", 10, "italic"),
            fg="Green",
            justify="center",
            bg="#8BD2B8"
        )
        message_vlc_T.place(x=180, y=175)
        link = Label(
            window,
            text="                                                                            ",
            bg="#8BD2B8",
            justify="center",
        )
        link.place(x=210, y=200)
    else:
        message_vlc_F = Label(
            window,
            text="VlC Media Player Is Not Installed !",
            font=("Comic Sans MS", 10, "italic"),
            fg="Red",  # 150877
            justify="center",
            bg="#8BD2B8"
        )
        message_vlc_F.place(x=180, y=175)
        link = Label(
            window,
            text="Click Here To Download",
            font=("Comic Sans MS", 10, "italic"),
            fg="Blue",
            bg="#8BD2B8",
            justify="center",
            cursor="hand2"
        )
        link.place(x=210, y=200)
        link.bind("<Button-1>", lambda e:
                  url_call("https://www.videolan.org/"))

    if cap.isOpened():
        message_cap_T = tk.Label(
            window,
            text="Camera is Available.      ",
            font=("Comic Sans MS", 10, "italic"),
            fg="Green",
            justify="center",
            bg="#8BD2B8"
        )
        message_cap_T.place(x=210, y=230)
    else:
        messag_cap_F = tk.Label(
            window,
            text="Camera is Not Available",
            font=("Comic Sans MS", 10, "italic"),
            fg="Red",  # 150877
            justify="center",
            bg="#8BD2B8"
        )
        messag_cap_F.place(x=210, y=230)
    if vlc_check != False and cap.isOpened():
        message_all_T = tk.Label(
            window,
            text="All Set, Ready to Run                ",
            font=("Comic Sans MS", 15, "bold", "italic"),
            fg="Black",
            justify="center",
            bg="#8BD2B8"
        )
        message_all_T.place(x=200, y=270)
    else:
        message_all_F = tk.Label(
            window,
            text="Please meet the Requirements",
            font=("Comic Sans MS", 15, "bold", "italic"),
            fg="Black",
            justify="center",
            bg="#8BD2B8"
        )
        message_all_F.place(x=200, y=270)
    cap.release()

# run button


def run_onClick():
    vlc_check = vlc.getAppPath(appName="vlc")
    cap = cv2.VideoCapture(0)
    if vlc_check != False and cap.isOpened():
        cap.release()
        window.destroy()
        vlc.start(name="vlc")
    else:
        messagebox.showerror(
            "ERROR", "Requirements Don't Match \n Click on CHECK button to Know more")

# ====================     Creating Button's ===============================


# button check
check = Button(window, text="Check",
               command=check_onClick, width=15)

# button run
run = tk.Button(window, text="Run", command=run_onClick,
                width=15)

# button instruction

info = Label(
    window,
    text="How to Use? Click Here !",
    font=("Comic Sans MS", 10, "italic"),
    fg="Blue",
    bg="#8BD2B8",
    justify="center",
    cursor="hand2"
)
info.bind("<Button-1>", lambda e:
          url_call("info.html"))


# packing
instruct_1.place(x=50, y=10)
check.place(x=30, y=170)
run.place(x=30, y=215)
info.place(x=360, y=350)

window.mainloop()
