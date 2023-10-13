import tkinter as tk

def form_string(s):
    global exp
    exp += s
def clear_string():
    global exp
    exp = ""
    entry.delete(0,"end")   
def calculate(exp):
    beg = 0
    res = 0
    op =0
    for ch in exp:
        if(ch=='+' or ch=='-' or ch=='*' or ch=='/'):
            op = exp.find(ch,beg)
            n = int(exp[beg:op])
            if(beg==0):
                res = n
            else:
                if(exp[beg-1]=='+'):
                    res += n
                elif(exp[beg-1]=='-'):
                    res -= n
                elif(exp[beg-1]=='*'):
                    res *= n
                elif(exp[beg-1]=='/'):
                    res /= n
            beg = op+1
    n = int(exp[beg::])
    if(exp[op]=='+'):
        res += n
    elif(exp[op]=='-'):
        res -= n
    elif(exp[op]=='*'):
        res *= n
    elif(exp[op]=='/'):
        res /= n
    entry.insert(0,res)

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

exp = ""
entry = tk.Entry()
entry.grid(row=0,columnspan=4,sticky="ew")

b1 = tk.Button(text="7", command=lambda: form_string("7"))
b1.grid(row=1,column=0,sticky="nsew")
b2 = tk.Button(text="8", command=lambda: form_string("8"))
b2.grid(row=1,column=1,sticky="nsew")
b3 = tk.Button(text="9", command=lambda: form_string("9"))
b3.grid(row=1,column=2,sticky="nsew")
b4 = tk.Button(text="/", command=lambda: form_string("/"))
b4.grid(row=1,column=3,sticky="nsew")

b5 = tk.Button(text="4", command=lambda: form_string("4"))
b5.grid(row=2,column=0,sticky="nsew")
b6 = tk.Button(text="5", command=lambda: form_string("5"))
b6.grid(row=2,column=1,sticky="nsew")
b7 = tk.Button(text="6", command=lambda: form_string("6"))
b7.grid(row=2,column=2,sticky="nsew")
b8 = tk.Button(text="*", command=lambda: form_string("*"))
b8.grid(row=2,column=3,sticky="nsew")

b9 = tk.Button(text="1", command=lambda: form_string("1"))
b9.grid(row=3,column=0,sticky="nsew")
b10 = tk.Button(text="2", command=lambda: form_string("2"))
b10.grid(row=3,column=1,sticky="nsew")
b11 = tk.Button(text="3", command=lambda: form_string("3"))
b11.grid(row=3,column=2,sticky="nsew")
b12 = tk.Button(text="-", command=lambda: form_string("-"))
b12.grid(row=3,column=3,sticky="nsew")

b13 = tk.Button(text="C", command=clear_string)
b13.grid(row=4,column=0,sticky="nsew")
b14 = tk.Button(text="0", command=lambda: form_string("0"))
b14.grid(row=4,column=1,sticky="nsew")
b15 = tk.Button(text="=", command=lambda: calculate(exp))
b15.grid(row=4,column=2,sticky="nsew")
b16 = tk.Button(text="+", command=lambda: form_string("+"))
b16.grid(row=4,column=3,sticky="nsew")

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

window.mainloop()