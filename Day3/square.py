'''Input number. Print square value'''
import tkinter as tk

def square():
    num = int(n.get())
    #square = num*num
    label2 = tk.Label(text = num*num, font=("Comic Sans MS",20))
    label2.grid(row=2,column=1,padx=20)

window = tk.Tk()
window.title("My Third GUI application")
window.minsize(700,400) 

n = tk.StringVar()

label1 = tk.Label(text="Enter a number:", font=("Times New Roman",20))
label1.grid(row=0,column=0,padx=20)

entry1 = tk.Entry(textvariable = n)
entry1.grid(row=0,column=1,padx=10)

button1 = tk.Button(text="Square", command = square)
button1.grid(row=1,column=1,padx=10)

window.mainloop()