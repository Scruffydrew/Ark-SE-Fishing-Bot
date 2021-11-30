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

R, G, B = 255, 255, 255, 

colour = (R,G,B)

from PIL import ImageGrab
from pyautogui import keyDown, keyUp
from time import sleep, perf_counter

while 1:
    start = perf_counter()
    # Get the RGB value for the pixel at the given coordinates on your screen
    PressQ, PressD, PressZ = \
    ImageGrab.grab().load()[1181, 1016], \
    ImageGrab.grab().load()[1187, 907], \
    ImageGrab.grab().load()[1158, 973]

    if PressD == colour and PressQ != colour and PressZ == colour:
        sleep(.1)
        print('Press D')
        keyDown("d")
        keyUp("d")
        pass

    end = perf_counter()
    print (end - start)
