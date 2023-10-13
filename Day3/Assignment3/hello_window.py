import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(700,500)

label = tkinter.Label(text = "Hello World!", font=("Comic Sans MS",20))
label.pack()

window.mainloop()