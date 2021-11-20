from python_imagesearch.imagesearch import *
import pyautogui
import time
import sys

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

# Start of Code
print("Welcome to the Ark Automated Fishing Service")
time.sleep(2)
print("Starting program")
time.sleep(2)

# Activates the print block function
#blockPrint()

print('39')

PressQ = imagesearch_loop(resource_path("Q.png"), .1)  # Search for the image 'Q.png' on your screen
PressW = imagesearch_loop(resource_path("W.png"), .1)  # Search for the image 'W.png' on your screen
PressE = imagesearch_loop(resource_path("E.png"), .1)  # Search for the image 'E.png' on your screen
PressA = imagesearch_loop(resource_path("A.png"), .1)  # Search for the image 'A.png' on your screen
PressS = imagesearch_loop(resource_path("S.png"), .1)  # Search for the image 'S.png' on your screen
PressD = imagesearch_loop(resource_path("D.png"), .1)  # Search for the image 'D.png' on your screen
PressZ = imagesearch_loop(resource_path("Z.png"), .1)  # Search for the image 'Z.png' on your screen
PressX = imagesearch_loop(resource_path("X.png"), .1)  # Search for the image 'X.png' on your screen
PressC = imagesearch_loop(resource_path("C.png"), .1)  # Search for the image 'C.png' on your screen
SUCC = imagesearch_loop(resource_path("SUCC.png"), .1)  # Search for the image 'SUCC.png' on your screen

print('52')

while SUCC[0] == -1:
    print('55')
    if PressQ[0] != -1:
        print('Press Q')
        pyautogui.keyDown("q")
        pyautogui.keyUp("q")

    if PressW[0] != -1:
        print('Press W')
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")

    if PressE[0] != -1:
        print('Press E')
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")

    if PressA[0] != -1:
        print('Press A')
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")

    if PressS[0] != -1:
        print('Press S')
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")

    if PressD[0] != -1:
        print('Press D')
        pyautogui.keyDown("d")
        pyautogui.keyUp("d")

    if PressZ[0] != -1:
        print('Press Z')
        pyautogui.keyDown("z")
        pyautogui.keyUp("z")

    if PressX[0] != -1:
        print('Press X')
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")

    if PressC[0] != -1:
        print('Press C')
        pyautogui.keyDown("c")
        pyautogui.keyUp("c")
if SUCC[0] != -1:
    print("Congrats You've caught a fish")


