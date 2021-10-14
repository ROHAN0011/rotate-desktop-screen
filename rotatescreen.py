# Import required modules
from tkinter import *
import rotatescreen # pip install rotate-screen


# User defined funtion
# for rotating screen
def Screen_rotation(args):
	screen = rotatescreen.get_primary_display()
	if args == "up":
		screen.set_landscape()
	elif args == "right":
		screen.set_portrait_flipped()
	elif args == "down":
		screen.set_landscape_flipped()
	elif args == "left":
		screen.set_portrait()


# Creating tkinter object
master = Tk()
master.geometry("150x150")
master.title("Screen Rotation")
master.configure(bg='light grey')





# Creating buttons to change orientation
Button(master, text="Up", command=lambda: Screen_rotation(
	"up"), bg="white").grid(row=20, column=20)
Button(master, text="Right", command=lambda: Screen_rotation(
	"right"), bg="white").grid(row=25, column=25)
Button(master, text="Left", command=lambda: Screen_rotation(
	"left"), bg="white").grid(row=25, column=15)
Button(master, text="Down", command=lambda: Screen_rotation(
	"down"), bg="white").grid(row=30, column=20)


mainloop()