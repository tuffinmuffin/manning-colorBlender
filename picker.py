import cv2 as cv
import sys
import numpy as np


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

### Your code here

def main():
    canvas = createCanvas((255,255,255))
    palette = loadPalette()
    print(canvas[1][1])
    print(palette[1][1])
    displayImage(palette, PICKER)
    displayImage(canvas, CANVAS)
    cv.waitKey(0)




if __name__ == "__main__":
    main()