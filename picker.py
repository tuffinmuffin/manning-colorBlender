import cv2 as cv
import sys
import numpy as np
import math

PICKER = "Color Picker"
CANVAS = "Canvas"
SIZE = (640, 640)

# Create a white canvas
def createCanvas(color, size = SIZE):
    canvasMat = np.empty(size + (3,), dtype=np.uint8)
    canvasMat[:][:] = color
    return canvasMat

# Display an image
def displayImage(image, name):
    cv.imshow(name, image)

# Load the color palette
def loadPalette(size = SIZE):
    palette = cv.imread("wheel1.jpg")
    return cv.resize(palette, size)

# Mouse callback function
def mouseCallbackFunction(event, x, y, flags, param):
    palette = param[0]
    canvas = param[1]
    if(not event == cv.EVENT_LBUTTONDOWN):
        return
    mixed = mixColors(findColor(palette, x, y), findColor(canvas, x, y))
    canvas[:][:] = mixed
    #redraw scene
    draw()

# Find the color for an image at the given location
def findColor(img,x,y):
    return img[x][y]

# Mix two colors
def mixColors(color1, color2):
    mix = color1*0.5 + color2*0.5
    return np.ceil(mix)

def draw():
    global palette, canvas
    displayImage(palette, PICKER)
    displayImage(canvas, CANVAS)

def main():
    global canvas, palette
    canvas = createCanvas((255,255,255))
    palette = loadPalette()
    draw()
    cv.setMouseCallback(PICKER, mouseCallbackFunction, (palette, canvas))

    while(True):
        draw()
        event = cv.waitKeyEx(0)
        if(event == 27):
            break





if __name__ == "__main__":
    main()