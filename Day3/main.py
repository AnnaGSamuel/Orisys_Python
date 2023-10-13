import tkinter

def print_msg():
    print("This button was clicked")
    label2["text"] = "Hiii"#label2.config(text = "I am fine.My name is Anna.")
window = tkinter.Tk()

window.title("My Application")

#window.geometry("500x300") #widthxheight #here size won't reduce further
window.minsize(500,300) # (width,height) #It's min size. can't reduce further

label1 = tkinter.Label(text = "This is my first GUI application")
label1.pack(side="bottom") #place label inside it . Layout manager. Create a layout

label2 = tkinter.Label(text = "Hi how are you?", font =("Times New Roman",20))
label2.pack()
#label2["text"] = "Heyyy"
#label2.place(x=10,y=20)

btn = tkinter.Button(text="Click me", command = print_msg)
btn.pack()

window.mainloop()
'''
Tk is a class in tkinter
mainloop keeps the code running

specify width of window
if minsize(0,0) - default size window will appear

pack() method disadv
only left,right,bottom and top.

place() - we can specify x and y exactly
disadv - difficult to do for each

grid() -
matrix form 0,1,2....
(0,1) = row,column

so we can use place and grid

tkinter.Button(text="Click me", command = print_msg) - Message will be displayed only when clicked
if print_msg() - it'll be displayed one time before clicking

To change text of label:
l1["text"] = "Hey"
l1.config(text="Hey")

WIDGETS:
label,entry,button

import tkinter as ttk - alias
'''