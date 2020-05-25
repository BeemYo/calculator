from tkinter import filedialog
from tkinter import *

output = ""
outputRem = False

root = Tk()
root.title("Calculator")

bFrame = Frame(root)
bFrame.grid(row=1)

def out(am):
	global output, display, outputRem
	if outputRem:
		output = ""
		outputRem = False
	output += am
	display.config(background="#67772b", fg="#000000", text=output, anchor="e", font=("Helvetica", 30))

def but(t, r, c):
	global bFrame, output
	button = Button(bFrame)
	button.grid(row=r, column=c)
	button.config(text=t, command= lambda: out(t), width="10")
	return button

def calc():
	global output, display, outputRem
	try:
		output = str(eval(output))
	except:
		output = "Error"
	outputRem = True
	display.config(background="#67772b", fg="#000000", text=output, anchor="e", font=("Helvetica", 30))
def delete():
	global output
	output = ""
	display.config(background="#67772b", fg="#000000", text=output, anchor="e", font=("Helvetica", 30))

display = Label(root)
display.grid(sticky=N+S+E+W, row=0, column=0)
display.config(background="#67772b", fg="#000000", text=output, anchor="e", font=("Helvetica", 30))
root.rowconfigure(0, weight=100)
root.columnconfigure(0, weight=20)

def addButs():
	global bFrame
	b1 = but("1", 0, 0)
	b2 = but("2", 0, 1)
	b3 = but("3", 0, 2)
	bplus = but("+", 0, 3)
	#new row
	b4 = but("4", 1, 0)
	b5 = but("5", 1, 1)
	b6 = but("6", 1, 2)
	btimes = but("*", 1, 3)
	#new row
	b7 = but("7", 2, 0)
	b8 = but("8", 2, 1)
	b9 = but("9", 2, 2)
	bmin = but("-", 2, 3)
	#new row
	bdel = Button(bFrame)
	bdel.grid(row=3, column=0)
	bdel.config(text="del", command=delete, width="10")
	b0 = but("0", 3, 1)
	bis = Button(bFrame)
	bis.grid(row=3, column=2)
	bis.config(text="=", command=calc, width="10")
	bdiv = but("/", 3, 3)
addButs()


root.mainloop()
