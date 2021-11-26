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
#blockPrint()

class App():

    def __init__(self):

        self.root = tkr.Tk()
            # names the Tk root window
        self.root.title("Automated Fishing Service Starter")
            # sets the size of the window
        self.root.geometry("150x150")
            # removes title bar from window
        self.root.overrideredirect(1)

        self.root.configure(bg='grey')
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "grey")

        normal = resource_path('normal.png')

        hover = resource_path('hover.png')

        imgh = PhotoImage(file=hover)

        def changeOnHover(button, colorOnHover, colorOnLeave):
  
            # adjusting backgroung of the widget
            # background on entering widget
            button.bind("<Enter>", func=lambda e: button.config(image=imgh, height=75))
  
            # background color on leaving widget
            button.bind("<Leave>", func=lambda e: button.config(image=img, height=75))

        img = PhotoImage(file=normal)
        btn= Button(self.root, image=img, command=self.start_command, borderwidth=0, bg='grey', activebackground='grey', height=75)
        btn.pack(pady=0)

        changeOnHover(btn, hover, normal)

        self.root.mainloop()

    def start_command(self):
        #print ("You've chosen to start the program") 
        self.root.destroy() # Closes the menu
        exec(open(resource_path('Ark_Fishing_Bot - Starting Stage.py')).read()) # Runs the selected python file

a = App()