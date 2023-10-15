import tkinter as tk

def add_task():
    task = entry1.get()
    create_frame(task)
    entry1.delete(0, tk.END)
    
def delete_task(frame):
    frame.destroy()

def create_frame(task):
    frame = tk.Frame(task_list, bd=2)
    task_label = tk.Label(frame, text=task)
    remove_button = tk.Button(frame, text="Remove", command=lambda: delete_task(frame))

    task_label.grid(row=2,column=0)
    remove_button.grid(row=2,column=1)

    frame.grid(padx=10, pady=5, sticky="nsew")

window = tk.Tk()
window.title("TO-DO List")
window.minsize(400,400)

label = tk.Label(text = "TO-DO List", font=("Comic Sans MS",20))
label.grid(row=0,column=0)

entry1 = tk.Entry()
entry1.grid(row=1,column=0)
b1 = tk.Button(text = "Add", command = add_task)
b1.grid(row=1,column=1)

task_list = tk.Frame()
task_list.grid(row=2,column=0,sticky="nsew")

window.mainloop()
