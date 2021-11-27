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

from tkinter import PhotoImage, Button
import tkinter as tkr

class App():

    def __init__(self):

        self.root = tkr.Tk()
            # names the Tk root window
        self.root.title("Automated Fishing Service Starter")
            # sets the size of the window
        self.root.geometry("675x200")
            # removes title bar from window
        self.root.overrideredirect(1)

        self.root.configure(bg='grey')
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "grey")

        self.frame1 = tkr.Frame(self.root)
        self.frame2 = tkr.Frame(self.root)
        self.frame3 = tkr.Frame(self.root)

        # Frame 1

        welcome = resource_path('welcome.png')

        img1 = PhotoImage(file=welcome)
        btn1= Button(self.frame1, image=img1, borderwidth=0, bg='grey', activebackground='grey', height=75)
        btn1.pack(pady=0)

        self.frame1.after(2000, self.frame1_command) # Waits 2 seconds then runs the command frame2_command

        # Frame 2

        welcome = resource_path('welcome.png')

        starting = resource_path('starting.png')

        img2 = PhotoImage(file=welcome)
        btn2= Button(self.frame2, image=img2, borderwidth=0, bg='grey', activebackground='grey', height=75)
        btn2.pack(pady=0)

        img3 = PhotoImage(file=starting)
        btn3= Button(self.frame2, image=img3, borderwidth=0, bg='grey', activebackground='grey', height=0)
        btn3.pack(pady=0)

        self.frame2.after(4000, self.frame2_command) # Waits 2 seconds then runs the command frame3_command

        # Frame 3

        overlay = resource_path('overlay.png')

        img4 = PhotoImage(file=overlay)
        btn4= Button(self.frame3, image=img4, borderwidth=0, bg='grey', activebackground='grey', height=75)
        btn4.pack(pady=0)

        self.frame3.after(6000, self.open_command)

        self.frame1.pack() # Allows for the contents of frame 1 to show
    
        self.root.mainloop()
        
    def open_command(self):
        exec(open(resource_path('Ark_Fishing_Bot.py')).read()) # Runs the python file labeled Ark_Fishing_Bot,py

    def frame1_command(self):
        #print ("You've chosen to start the program")
        self.frame1.pack_forget() # Forgets tkinter contents in frame 1
        self.frame1.destroy() # Closes the contents for frame 1
        self.frame2.pack() # Runs the next frame
    
    def frame2_command(self):
        #print ("You've chosen to start the program")
        self.frame2.pack_forget() # Forgets tkinter contents in frame 2
        self.frame2.destroy() # Closes the contents for frame 2
        self.frame3.pack() # Runs the next frame
        self.root.geometry("1920x200+0+1020")
        
a = App()


