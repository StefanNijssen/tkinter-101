
import random

import tkinter as tk
window = tk.Tk()
window.title("Grabbelton")
window.geometry('100x100')
button = tk.Button(text='GRAB!', bg="white", fg="black")
button.pack(pady = 10, padx= 10)
ton = ['appel', 'peer', 'banaan', 'citroen', 'tomaat', 'prei', 'sla', 'komkommer', 'meloen', 'aardbei']
def clickButton(event):
    
    if button.config('text')[-1] == 'GRAB!':
        prijs = random.choice(ton)
        print('gefeliciteerd! U heeft een ' + prijs + ' gewonnen!')
        ton.remove(prijs)


# alle tkinter code komt hier tussen





button.bind('<Button-1>', clickButton)
window.mainloop()