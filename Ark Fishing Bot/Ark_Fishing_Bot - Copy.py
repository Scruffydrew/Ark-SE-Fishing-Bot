from PIL import Image, ImageTk
from tkinter import *
import tkinter as tkr
import PIL.ImageGrab
import pyautogui
import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Stop the print command from showing up in the console
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Activates the print block function
blockPrint()

print('39')

root = tkr.Tk()
        # names the Tk root window
root.title("Automated Fishing Service Starter")
        # sets the size of the window
root.geometry("96x151+1101+869")
        # removes title bar from window
root.overrideredirect(1)

root.configure(bg='grey')
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "grey")


pixel = resource_path('pixels.png')

img = PhotoImage(file=pixel)
btn= Button(root, image=img, borderwidth=0, bg='grey', activebackground='grey', height=75)
btn.pack(pady=0)

root.mainloop()