import tkinter

def print_name():
    print("This button was clicked")
    label2.config(text = name.get())
window = tkinter.Tk()

window.title("My second GUI Application")

window.minsize(700,400) 

name = tkinter.StringVar() #if normal string it won't have the property "get()"

label1 = tkinter.Label(text = "Enter your name",font=("Comic Sans MS",16))
label1.grid(row=0,column=0,padx=20)#label1.pack()

name_entry = tkinter.Entry(textvariable = name)
name_entry.grid(row=0,column=1,padx=5)#pack()

label2 = tkinter.Label(text = "Name",font=("Comic Sans MS",18))
label2.grid(row=2,column=1,sticky="s")#pack(side="bottom")

btn = tkinter.Button(text="Submit", command = print_name)
btn.grid(row=1,column=1,padx=20)#pack()

window.mainloop()