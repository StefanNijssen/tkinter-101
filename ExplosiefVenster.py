from random import random
import random
import tkinter


window = tkinter.Tk()
# alle tkinter code komt hier tussen
listcolor = ['pink', 'red', 'blue', 'yellow', 'green']
window.title("Dit is mijn window")
window.geometry('50x50')
i = 50
x = 6
def updateWindow():
    global i
    global x
    seize = str(i) + 'x' + str(i)
    window.geometry(seize)
    color = random.choice(listcolor)
    window.configure(bg=color)
    i += 50
    x -= 1
    print(x)
    if x == 0:
        print("Boom!")
        window.destroy()
    else:
        window.after(2000, updateWindow)
        
    
window.after(2000, updateWindow)
print('5')
window.mainloop()
