'''PASSWORD GENERATOR
each version add,delete we can see all versions. version control software.

master,alpha,beta branches if change in beta,we pull to master ie,stable version

password manager:
store passwords in files txt/json(better) 
'''
import tkinter as tk
import random
import string

def generate_psswd():
    symbol_no = int(symbol_count.get())
    digit_no = int(digit_count.get())
    alpha_no = int(alpha_count.get())
    passwd = []
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    for i in range(0,symbol_no):
        passwd+=random.choice(symbols)
    for i in range(0,digit_no):
        passwd+=random.choice(digits)
    for i in range(0,alpha_no):
        passwd+=random.choice(letters)

    random.shuffle(passwd)
    password =""
    for ch in passwd:
        password+= ch
    entry4.delete(0,"end")
    entry4.insert(0,password)

window = tk.Tk()
window.title("Password generator")
window.minsize(700,500)

symbol_count = tk.StringVar()
digit_count = tk.StringVar()
alpha_count = tk.StringVar()

label1 = tk.Label(text="Number of symbols:",font=(16))
label1.grid(row=0,column=0,padx=20)
entry1 = tk.Entry(textvariable = symbol_count)
entry1.grid(row=0,column=1,padx=10)

label2 = tk.Label(text="Number of digits:",font=(16))
label2.grid(row=1,column=0,padx=20)
entry2 = tk.Entry(textvariable = digit_count)
entry2.grid(row=1,column=1,padx=10)

label3 = tk.Label(text="Number of alphabets:",font=(16))
label3.grid(row=2,column=0,padx=20)
entry3 = tk.Entry(textvariable = alpha_count)
entry3.grid(row=2,column=1,padx=10)

button1 = tk.Button(text="Generate password", command=generate_psswd)
button1.grid(row=3,column=1,padx=10,pady=20)

label4 = tk.Label(text="Generated password:",font=(16))
label4.grid(row=4,column=0,padx=20)
entry4 = tk.Entry()
entry4.grid(row=4,column=1,padx=10)

window.mainloop()