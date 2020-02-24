from tkinter import *
from tkinter.ttk import * 
import time
import os # for looping over images, counting num files in dir

# NOTE: to work, must have directory called generated_files full of
# pngs named in the scheme "generated<index>.png"

directory = 'generated_images'
fileIndex = 0
numFiles = len(os.listdir(directory))
waitTime = 300

# todo - called on generate button click
def generateCallback():
    print("generating new")

# todo - save current image
def saveImage():
    print("saving image")

main = Tk()
main.configure(bg='white') # make background white

# to rename the title of the window
main.title("Art")

# pack is used to show the object in the window
button_widget = Button(main, text="Generate New Image", command=generateCallback)
button_widget.pack()

button_widget2 = Button(main, text="Save Image", command=saveImage)
button_widget2.pack()

c = Canvas(main, width=500, height=500)
c.config(background='white')
c.pack()

# write first image to canvas
picture = PhotoImage(file=directory + "/" + "generated" + str(fileIndex) + ".png")
picture2 = c.create_image(250,250,image=picture)
fileIndex += 1

# function that loops through all files in directory
# all files must be named "generated<index>.png"
def nextImg():
    global fileIndex
    if(fileIndex < numFiles):
        global picture3
        picture3 = PhotoImage(file=directory + "/" + "generated" + str(fileIndex) + ".png")
        c.itemconfigure(picture2, image = picture3) # update canvas with new image
        fileIndex += 1
        global waitTime
        main.after(waitTime, nextImg)  # reschedule event in 1 second

main.after(waitTime, nextImg)

main.mainloop()