'''miles to km'''
import tkinter as tk

def convert_km():
    mile = float(miles.get())
    km = round(mile*1.609344,2)
    entry2.insert(0,km)
    
window = tk.Tk()
window.title("Miles to km converter")
window.minsize(700,500)

miles = tk.StringVar()

label1 = tk.Label(text = "Distance in miles: ")
label1.grid(row=0,column=0,padx=40,pady=20)
entry1 = tk.Entry(textvariable = miles)
entry1.grid(row=0,column=2,padx=60,pady=20)
label3 = tk.Label(text = "miles")
label3.grid(row=0,column=3)

label2 = tk.Label(text = "Distance in km: ")
label2.grid(row=1,column=0)
entry2 = tk.Entry()
entry2.grid(row=1,column=2)

button1 = tk.Button(text="Convert", command=convert_km)
button1.grid(row=2,column=2,pady=10)
window.mainloop()