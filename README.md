# image-annotate
Python program to annotate images for object detection. Outputs a csv file. Don't expect this program to work well. I am very inexperienced in making GUI applications in Python.

## Preparing Your Images

  1. Make a folder to store your images that is easy to access. Avoid using spaces or special characters (underscores are okay).
  2. Copy your images into this folder
  3. Make sure all your images are the same type (e.g. all jpeg or all png). Images that have JPEG or JPG file extensions can be renamed to JPG or JPEG without file conversions, but all other images should be converted.
  4. Rename each of of the images with the format <prefix><index number> (e.g. img1, img2, etc.)
  In macOs, you can select all of the images and do a bulk rename operation that can number the images for you
  
## Preparing the Program
  
  1. Install "Python 3.9" from Self Service
  2. Download "image-label.py" from this repository
  3. Open the file in "IDLE"
  4. Enter the path you want the output file to be placed in the "csv_path" variable. Replace "lica" with your username. All folders are separated by a "/". For example, "/Users/lica/Documents/training/label.csv" means going from the "Users" folder into the "lica" folder into some more folders anad finally ending at "label.csv", the name of the output file  
  ```python
  csv_path = "/Users/lica/Documents/training/label.csv" # output file
  ```
  5. Enter the path of the folder of the images into the "directory" variable. If you started your image name with a prefix like "img" put that here too. For example, "/Users/lica/Documents/training/img" means that the program will look for images starting with "img" in the training folder.  
  ```python
  directory = "/Users/lica/Documents/training/img" # directory with images plus any prefix
  ```
  6. If necessary, change the "i" variable to the number your images starts at
  ```python
  i = 1 # image number to start at
  ```
  7. If necessary, change ".jpg" in the "path" variable to another file extension (e.g. ".png" or ".jpeg")  
  ```python
  path = directory+str(i)+".jpg" # combines directory, image number, and file extension
  ```
  8. If necessary, change, add, or remove items in the "options" variable. Make sure all entries are separated by commas and are enclosed in "double quotes". Items listed here are the things you are going to identify on your images. Change the value in "clicked.set" to the default value you want to appear in the classification menu.  
  ```python
  options = ["duck", "cube", "ball", "team"]
  ```
  9. All done!
  
## Running the Program
  <img width="1142" alt="Screenshot of program with image view and buttons and drop down menu" src="https://user-images.githubusercontent.com/49379586/141716170-693d31e4-52aa-4fa4-9e5d-5a1b89416f2b.png">

  1. Run the program by going to the "Run" menu and clicking "Run Module". You can also press fn+f5 on your keyboard. A window should open up with one of your images a dropdown menu and a few buttons
  2. Check that the thing you want to classify is showing in the dropdown menu, if it is not, select it on the dropdown menu.
  3. Imagine a box around the thing you want to select
  4. Click on the image where of the corners of that box is
  5. Click on the image where the opposite corner of that box is. A colored rectangle should appear around the object and annotations should be added to the output file.
  6. Continue adding more rectangles around objects in the image, changing the selected classificaion in the dropdown menu as necessary. Different classifications have different rectangle colors.
  7. If you make a mistake, click the "Undo" button. If you want to clear the image of all annotations, click the "Clear" button
  8. Click the "Done" button to move to the next image. If there is nothing to annotate, just click done.
  9. The program will exit automatically when all images are annotated
  Note: You may close the program at any time. All changes are saved as they are made. Make sure to change the "i" variable, the variable that controls what image the program starts on, before launching the program again. If you do open the program again, there will be an extra step while processing the output file.
  
## Processing the Output File
  1. Open the output csv file in a program like Excel
  2. Edit the path of the images to the path where the images are going to be stored on the model making computer
  If you opened the program multiple times:
  1. Check for any entries that are not on their own line
  2. Move these entries to a new line. Entry order does not matter.
  Ensure the csv file is ready to go and that it adheres to [these standards](https://cloud.google.com/vision/automl/object-detection/docs/prepare)
  
## Troubleshooting
  Q: I cannot see the rectangle when selecting objects  
  A: Check IDLE and see if coordinates for "first" and "second" are being printed. If they are and you cannot see the rectangle, go to the code at the end of line 57 and change "width"
  
  
