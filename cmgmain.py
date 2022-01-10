import random
from tkinter import *
import tkinter
from PIL import ImageTk, Image

tiles = []

#Creates the window
window = Tk()
window.title("Catan Map Generator")
window.geometry("1440x720")
img = Image.open("blank.png")
img = img.resize((600, 600), Image.ANTIALIAS)
img = ImageTk.PhotoImage(Image.open("blank.png"))
panel = Label(window, image = img)
panel.pack(side = "right")
t1 = Text(window, font = ("Ariel Bold", 12), wrap = NONE)

#Selects resources for large map size
def selectionLarge():
    global tiles
    tiles = []
    selectionlist = ["brick \n", "wood \n", "stone \n", "sheep \n", "wheat \n"]
    intrange = 5
    for i in range(30):
        randint = random.randrange(intrange)
        selectedResource = selectionlist[randint]
        if tiles.count(selectedResource) > 6:
            selectionlist.remove(selectedResource)
            intrange = intrange - 1
        tiles.append(selectedResource)
    for i in range(2):
        randdesert = random.randrange(30)
        tiles.pop(randdesert)
        tiles.insert(randdesert, "desert \n")

#Selects resources for small map size
def selectionSmall():
    global tiles
    tiles = []
    selectionlist = ["brick \n", "wood \n", "stone \n", "sheep \n", "wheat \n"]
    intrange = 4
    for i in range(19):
        randint = random.randrange(intrange)
        selectedResource = selectionlist[randint]
        if tiles.count(selectedResource) > 4:
            selectionlist.remove(selectedResource)
            intrange = intrange - 1
        tiles.append(selectedResource)
    for i in range(1):
        randdesert = random.randrange(19)
        tiles.pop(randdesert)
        tiles.insert(randdesert, "desert \n")

#Sets the map on the window
def mapSet(cmd):
    global panel
    if cmd == "Small":
        img = Image.open("catanmap14player.png")
    else:
        img = Image.open("catanmap56player.png")
    img = img.resize((600, 600), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image = img)
    panel.image = img
    panel.pack(side = "right")

#Sets the text on the window
def textSet(cmd):
    global tiles
    global t1
    if cmd == "Small":
        selectionSmall()
    else:
        selectionLarge()
    for i in range(len(tiles)):
        count = i + 1
        string = str(count) + " " + tiles[i]
        t1.insert(END, string)
    t1.pack(side = "left", fill = Y)

#Sets everything on the window according to specified radio button selections
def setEverything():
    global t1
    t1.delete("1.0", "end")
    mapValue = selected.get()
    if mapValue == 1:
        cmd = "Small"
    elif mapValue == 2:
        cmd = "Large"
    textSet(cmd)
    mapSet(cmd)

#Creates the buttons initializes proper functions
selected = IntVar()
rad1 = Radiobutton(window,text = 'Small (1-4 players)', value = 1, variable = selected)
rad2 = Radiobutton(window,text = 'Large (5-6 players)', value = 2, variable = selected)
btn1 = Button(window, text = "Generate Map", command = setEverything)
btn1.pack(side = "top")
rad1.pack(side = "top")
rad2.pack(side = "top")

window.mainloop()


## TODO: Nothing 
