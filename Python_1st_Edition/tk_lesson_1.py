from tkinter import *
from tkinter.ttk import *

#  creating main window object named root
root = Tk()

#  Forces the main window to size 500 by 500 pixels
root.geometry("500x500")

#  giving title to main window
root.title("~ calculator ~")

#  creating a label (text) to show on main window
label = Label(root, text ="Hello World").pack()

#  creating frame for main window
frame = Frame(root)

#  .pack is a geometry method
frame.pack()

#  creates a button insdie the frame of main window
button = Button(root, text ="NERD")
button.pack()



#  keeps displaying the main window
root.mainloop()
