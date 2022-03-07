import tkinter as tk
from tkinter import ttk
 
window = tk.Tk()
# alle tkinter code komt hier tussen
window.title("Hello")
window.geometry('200x100')
window.configure(background='blue')
label1 = tk.Label(
    window,
    text='Hello tkinter!',
    bg="red",
    fg="yellow"
)

label1.pack(
    ipadx=60,
    ipady=20,
    expand=True,
    
    
)




window.mainloop()