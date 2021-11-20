import PIL.ImageGrab
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

loop = 1

R = 0
G = 0
B = 0

colour = (R,G,B)

print('39')

while loop == 1:
    PressQ = PIL.ImageGrab.grab().load()[1181, 1016]  # Get the RGB value for the pixel at x=1181, y=1016 on your screen
    PressW = PIL.ImageGrab.grab().load()[1113, 868]  # Get the RGB value for the pixel at x=1113, y=868 on your screen
    PressA = PIL.ImageGrab.grab().load()[1162, 970]  # Get the RGB value for the pixel at x=1162, y=970 on your screen
    PressD = PIL.ImageGrab.grab().load()[1192, 906]  # Get the RGB value for the pixel at x=1192, y=906 on your screen
    PressZ = PIL.ImageGrab.grab().load()[1158, 973]  # Get the RGB value for the pixel at x=1158, y=973 on your screen
    PressX = PIL.ImageGrab.grab().load()[1167, 972]  # Get the RGB value for the pixel at x=1167, y=972 on your screen

    PressE = PIL.ImageGrab.grab().load()[1186, 998]  # Get the RGB value for the pixel at x=1186, y=998 on your screen
    PressS = PIL.ImageGrab.grab().load()[1161, 917]  # Get the RGB value for the pixel at x=1161, y=917 on your screen
    PressC = PIL.ImageGrab.grab().load()[1135, 918]  # Get the RGB value for the pixel at x=1135, y=918 on your screen

    E1 = PIL.ImageGrab.grab().load()[1162, 970]  # Get the RGB value for the pixel at x=1162, y=970 on your screen; A
    E2 = PIL.ImageGrab.grab().load()[1158, 973]  # Get the RGB value for the pixel at x=1158, y=973 on your screen; Z
    E3 = PIL.ImageGrab.grab().load()[1113, 868]  # Get the RGB value for the pixel at x=1113, y=868 on your screen; W
    E4 = PIL.ImageGrab.grab().load()[1167, 972]  # Get the RGB value for the pixel at x=1167, y=972 on your screen; X
    E5 = PIL.ImageGrab.grab().load()[1192, 906]  # Get the RGB value for the pixel at x=1192, y=906 on your screen; D

    S1 = PIL.ImageGrab.grab().load()[1158, 973]  # Get the RGB value for the pixel at x=1158, y=973 on your screen; Z
    S2 = PIL.ImageGrab.grab().load()[1113, 868]  # Get the RGB value for the pixel at x=1113, y=868 on your screen; W
    S3 = PIL.ImageGrab.grab().load()[1167, 972]  # Get the RGB value for the pixel at x=1167, y=972 on your screen; X

    C1 = PIL.ImageGrab.grab().load()[1181, 1016]  # Get the RGB value for the pixel at x=1181, y=1016 on your screen; Q
    C2 = PIL.ImageGrab.grab().load()[1192, 906]  # Get the RGB value for the pixel at x=1192, y=906 on your screen; D

    print('55')

    if PressQ == colour:
        print('Press Q')
        pyautogui.keyDown("q")
        pyautogui.keyUp("q")
        continue

    if PressW == colour:
        print('Press W')
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
        continue

    if PressA == colour:
        print('Press A')
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        continue

    if PressD == colour:
        print('Press D')
        pyautogui.keyDown("d")
        pyautogui.keyUp("d")
        continue

    if PressZ == colour:
        print('Press Z')
        pyautogui.keyDown("z")
        pyautogui.keyUp("z")
        continue

    if PressX == colour:
        print('Press X')
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        continue


    if PressE == colour and E1 != colour and E2 != colour and E3 != colour and E4 != colour and E5 != colour:
        print('Press E')
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        continue

    if PressS == colour and S1 != colour and S2 != colour and S3 != colour:
        print('Press S')
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")
        continue

    if PressC == colour and C1 != colour and C2 != colour:
        print('Press C')
        pyautogui.keyDown("c")
        pyautogui.keyUp("c")
        continue


