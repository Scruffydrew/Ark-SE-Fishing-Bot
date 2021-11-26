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
loop = 1

R = 255
G = 255
B = 255

colour = (R,G,B)

while loop == 1:
    print(colour)
    time.sleep(.1)
    PressQ = PIL.ImageGrab.grab().load()[1181, 1016]  # Get the RGB value for the pixel at x=1181, y=1016 on your screen
    PressW = PIL.ImageGrab.grab().load()[1113, 868]  # Get the RGB value for the pixel at x=1113, y=868 on your screen
    PressA = PIL.ImageGrab.grab().load()[1162, 970]  # Get the RGB value for the pixel at x=1162, y=970 on your screen
    PressD = PIL.ImageGrab.grab().load()[1187, 907]  # Get the RGB value for the pixel at x=1192, y=906 on your screen
    PressZ = PIL.ImageGrab.grab().load()[1147, 973]  # Get the RGB value for the pixel at x=1158, y=973 on your screen
    PressX = PIL.ImageGrab.grab().load()[1167, 972]  # Get the RGB value for the pixel at x=1167, y=972 on your screen

    PressE = PIL.ImageGrab.grab().load()[1186, 998]  # Get the RGB value for the pixel at x=1186, y=998 on your screen
    PressS = PIL.ImageGrab.grab().load()[1161, 917]  # Get the RGB value for the pixel at x=1161, y=917 on your screen
    PressC = PIL.ImageGrab.grab().load()[1134, 918]  # Get the RGB value for the pixel at x=1135, y=918 on your screen

    print('55')

    if PressQ == colour and PressW != colour and PressA != colour and PressD == colour and PressZ == colour and PressX != colour and PressE != colour and PressS != colour:
        time.sleep(.1)
        print('Press Q')
        pyautogui.keyDown("q")
        pyautogui.keyUp("q")
        continue

    if PressW == colour and PressQ != colour and PressA != colour and PressD != colour and PressZ == colour and PressX != colour and PressE == colour and PressS == colour:
        time.sleep(.1)
        print('Press W')
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
        continue

    if PressA == colour and PressQ != colour and PressW != colour and PressD != colour and PressZ == colour and PressX != colour and PressE == colour and PressS != colour:
        time.sleep(.1)
        print('Press A')
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        continue

    if PressD == colour and PressQ != colour and PressW != colour and PressA != colour and PressZ == colour and PressX != colour and PressE != colour and PressS != colour:
        time.sleep(.1)
        print('Press D')
        pyautogui.keyDown("d")
        pyautogui.keyUp("d")
        continue

    if PressZ == colour and PressQ != colour and PressW != colour and PressA != colour and PressD != colour and PressX != colour and PressE == colour and PressS == colour:
        time.sleep(.1)
        print('Press Z')
        pyautogui.keyDown("z")
        pyautogui.keyUp("z")
        continue

    if PressX == colour and PressQ != colour and PressW != colour and PressA != colour and PressD != colour and PressZ == colour and PressE == colour and PressS == colour:
        time.sleep(.1)
        print('Press X')
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        continue


    if PressE == colour and PressQ != colour and PressW != colour and PressA != colour and PressD != colour and PressZ == colour and PressX != colour and PressS != colour:
        time.sleep(.1)
        print('Press E')
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        continue

    if PressS == colour and PressQ != colour and PressW != colour and PressA != colour and PressD != colour and PressZ == colour and PressX != colour and PressE != colour:
        time.sleep(.1)
        print('Press S')
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")
        continue

    if PressC == colour and PressQ != colour and PressW != colour and PressA != colour and PressD != colour and PressZ == colour and PressX != colour and PressE != colour and PressS != colour:
        time.sleep(.1)
        print('Press C')
        pyautogui.keyDown("c")
        pyautogui.keyUp("c")
        continue

root.mainloop()