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
    sleep(.1)
    # Get the RGB value for the pixel at the given coordinates on your screen
    PressQ, PressW, PressA, PressD, PressZ, PressX, PressE, PressS, PressC = \
    ImageGrab.grab().load()[1181, 1016], \
    ImageGrab.grab().load()[1113, 868], \
    ImageGrab.grab().load()[1162, 970], \
    ImageGrab.grab().load()[1187, 907], \
    ImageGrab.grab().load()[1158, 973], \
    ImageGrab.grab().load()[1167, 972], \
    ImageGrab.grab().load()[1186, 998], \
    ImageGrab.grab().load()[1161, 917], \
    ImageGrab.grab().load()[1134, 918]  

    if PressQ == colour:
        sleep(.1)
        print('Press Q')
        keyDown("q")
        keyUp("q")
        pass

    if PressW == colour:
        sleep(.1)
        print('Press W')
        keyDown("w")
        keyUp("w")
        pass

    if PressA == colour:
        sleep(.1)
        print('Press A')
        keyDown("a")
        keyUp("a")
        pass

    if PressD == colour and PressQ != colour and PressZ == colour:
        sleep(.1)
        print('Press D')
        keyDown("d")
        keyUp("d")
        pass

    if PressZ == colour and PressW != colour and PressX != colour:
        sleep(.1)
        print('Press Z')
        keyDown("z")
        keyUp("z")
        pass

    if PressX == colour:
        sleep(.1)
        print('Press X')
        keyDown("x")
        keyUp("x")
        pass


    if PressE == colour and PressA != colour and PressZ == colour and PressS != colour:
        sleep(.1)
        print('Press E')
        keyDown("e")
        keyUp("e")
        pass

    if PressS == colour:
        sleep(.1)
        print('Press S')
        keyDown("s")
        keyUp("s")
        pass

    if PressC == colour and PressZ == colour:
        sleep(.1)
        print('Press C')
        keyDown("c")
        keyUp("c")
        pass
    end = perf_counter()
    print (end - start)