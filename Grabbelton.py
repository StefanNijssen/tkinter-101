
import random

import tkinter as tk
window = tk.Tk()
window.title("Grabbelton")
window.geometry('100x100')
button = tk.Button(text='GRAB!', bg="white", fg="black")
button.pack(pady = 10, padx= 10)

def clickButton(event):
    ton = ['appel', 'peer', 'banaan', 'citroen', 'tomaat', 'prei', 'sla', 'komkommer', 'meloen', 'aardbei']
    if button.config('text')[-1] == 'GRAB!':
        print(random.choice(ton))

        
# alle tkinter code komt hier tussen





button.bind('<Button-1>', clickButton)
window.mainloop()