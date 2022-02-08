# This program views annotations created by image-annotate.py
# Make sure to check the output of image-annotate.py before feeding it into thiis one
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = tk.Tk()

def parseLine(line):
    rows = line.split(",")
    path = rows[1]
    x1 = rows[3]
    y1 = rows[4]
    x2 = rows[7]
    y2 = rows[8]
    return [path, x1, y1, x2, y2]
    
def getImage(path):
    # open image
    try:
        photo = Image.open(path)
    except FileNotFoundError:
        return None
    photo = photo.resize((1024, 768), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(photo)
    return photo




rectangles = []
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "white", "black"]
i = 0

csv_path = "./training2/label.csv" # output file
directory = "./training2/img" # directory with images plus any prefix
f = open(csv_path, "r")
lines = f.readlines()
data = parseLine(lines[i])
print(data)
photo = getImage(data[0])

w = Canvas(root, width=photo.width(), height=photo.height())
w.pack()


current_image = w.create_image(0, 0, anchor=NW, image=photo)

x1 = float(data[1])*photo.width()
y1 = float(data[2])*photo.height()
x2 = float(data[3])*photo.width()
y2 = float(data[4])*photo.height()
print(x1)
print(y1)
print(x2)
print(y2)
# open first image

rectangles.append(w.create_rectangle(x1, y1, x2, y2, outline=colors[0], width="2"))

# setup canvas


# display image


# options and colors for classification


w2 = Canvas(root, width=100, height=100)
w2.pack()
def next(): # switch to next image
    global i, current_image, photo, path
    i = i+1
    try:
        data = parseLine(lines[i])
    except IndexError:
        exit()
##    print(data)
    photo = getImage(data[0])
    w.delete(current_image)
    current_image = w.create_image(0, 0, anchor=NW, image=photo)

    for rectangle in rectangles:
        w.delete(rectangle)
        rectangles.clear()
    x1 = float(data[1])*photo.width()
    y1 = float(data[2])*photo.height()
    x2 = float(data[3])*photo.width()
    y2 = float(data[4])*photo.height()
##    print(x1)
##    print(y1)
##    print(x2)
##    print(y2)
    rectangles.append(w.create_rectangle(x1, y1, x2, y2, outline=colors[0], width="2"))
    print("done")

done_button = tk.Button(w2, text="Next", command=next).pack()

    
root.mainloop()
