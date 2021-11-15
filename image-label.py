# This program outputs a csv file that is NOT ready for use in the tflite model maker
# given that the model creation happens locally on the same computer.
# ALWAYS open the csv file in a program like Excel and edit cells as necessary before using the model maker
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = tk.Tk()


csv_path = "/Users/lica/Documents/training/label.csv" # output file
directory = "/Users/lica/Documents/training/img" # directory with images plus any prefix
i = 1 #image number to start at
path = directory+str(i)+".jpg" # combines directory, image number, and file extension

# open first image
photo = Image.open(path)
photo = photo.resize((1024, 768), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)

# setup canvas
w = Canvas(root, width=photo.width(), height=photo.height())
w.pack()
w2 = Canvas(root, width=100, height=100)
w2.pack()

# display image
current_image = w.create_image(0, 0, anchor=NW, image=photo)

# options and colors for classification
options = ["duck", "cube", "ball", "team"]
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "white", "black"]
clicked = StringVar()
clicked.set("duck") # default classificatiion
drop = OptionMenu(w2, clicked, *options)
drop.pack()

rectangles = []
history = []
x1 = 0
y1 = 0
x2 = 0
y2 = 0
def getfirst(event): #first click
    global x1, y1
    x1 = event.x
    y1 = event.y
    print("first: ", x1, y1)
    w.bind("<Button-1>", getsecond)
    
def getsecond(event): # second click
    global x2, y2
    x2 = event.x
    y2 = event.y
    print("second: ", x2, y2)
    rectangles.append(w.create_rectangle(x1, y1, x2, y2, outline=colors[options.index(clicked.get())], width="2"))

    # get canvas width/height
    w.update()
    canvas_width = w.winfo_width()
    canvas_height = w.winfo_height()
    with open(csv_path, "a") as f:
        # write to file
        #line = "UNASSIGNED,"+path+","+classify+","+str(x1/canvas_width) + "," + str(y1/canvas_height) + ",,," + str(x2/canvas_width) + "," + str(y2/canvas_height)+",,\n"
        line = "UNASSIGNED,"+path+","+clicked.get()+","+str(x1/canvas_width) + "," + str(y1/canvas_height) + ",,," + str(x2/canvas_width) + "," + str(y2/canvas_height)+",,\n"

        history.append(line)
        f.write(line)
    w.bind("<Button-1>", getfirst)

w.bind("<Button-1>", getfirst)

def done(): # switch to next image
    global i, current_image, photo, path
    i = i+1
    path = directory+str(i)+".jpg"
    try:
        photo = Image.open(path)
    except FileNotFoundError:
        print("No more images")
        exit()

    photo = photo.resize((1024, 768), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(photo)
    w.delete(current_image)
    current_image = w.create_image(0, 0, anchor=NW, image=photo)

    for rectangle in rectangles:
        w.delete(rectangle)
        rectangles.clear()
    print("done")

def clear(): # delete rectangles and csv entries
    for rectangle in rectangles:
        w.delete(rectangle)
    rectangles.clear()
    with open(csv_path, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if not(path in line):
                f.write(line)
        f.truncate()
    print("cleared")

def undo(): # delete last rectangle and csv entry
    rectangle = next(rectangle for rectangle in reversed(rectangles) if rectangle)
    w.delete(rectangle)
    rectangles.pop()
    with open(csv_path, "r+") as f:
        lines = f.readlines()
        lines.pop()
        f.seek(0)
        f.writelines(lines)
        f.truncate()
    print("undo")

done_button = tk.Button(w2, text="Done", command=done).pack()
clear_button = tk.Button(w2, text="Clear", command=clear).pack()
undo_button = tk.Button(w2, text="Undo", command=undo).pack()


root.mainloop()
