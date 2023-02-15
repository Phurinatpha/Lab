from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np

checkImageWidth = 64
checkImageHeight = 64
checkImage = np.zeros((checkImageHeight, checkImageWidth, 3), dtype=np.ubyte)

height = 250

def loadImage(filename):
    img = Image.open(filename)
    img = img.convert("RGB")
    return img

def makeImage(image, resize=None):
    if resize is not None:
        image = image.resize(resize)
    width, height = image.size
    image_data = list(image.getdata())
    data = []
    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = image_data[i*width + j]
            row.append((r, g, b))
        data.append(row)
    return data, width, height

def init():
    
    # Load the image from file and resize it
    image = loadImage("/Lab/LabCG/img/or-cat.png")
    # image = loadImage("/Lab/LabCG/img/test-moon.png")

    resized_image = image.resize((400, int(image.size[1]*400/image.size[0])))
    
    # Set the initial window size
    glutInitWindowSize(resized_image.size[0], resized_image.size[1])

    # Create the window
    glutCreateWindow(b"display img and reshape")

    # Convert the image to a format that can be used by glDrawPixels
    image_data, width, height = makeImage(resized_image)

    # Create a numpy array from the image data
    image_array = np.array(image_data, dtype=np.uint8)

    # Store the image array as a global variable
    global myImage
    myImage = image_array

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Compute the position of the lower-left corner of the image
    x = (glutGet(GLUT_WINDOW_WIDTH) - scaledImage.shape[1]) // 2
    y = (glutGet(GLUT_WINDOW_HEIGHT) - scaledImage.shape[0]) // 2

    # Set the raster position to the lower-left corner of the image
    glRasterPos2i(x, y)

    # Draw the pixels
    glDrawPixels(scaledImage.shape[1], scaledImage.shape[0], GL_RGB, GL_UNSIGNED_BYTE, np.flipud(scaledImage))

    glFlush()
    
def reshape(w, h):
    global height
    glViewport(0, 0, w, h)
    height = h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, w, 0.0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Scale the image to fit the new window size
    width_ratio = float(w) / myImage.shape[1]
    height_ratio = float(h) / myImage.shape[0]
    min_ratio = min(width_ratio, height_ratio)
    scaled_width = int(myImage.shape[1] * min_ratio)
    scaled_height = int(myImage.shape[0] * min_ratio)
    global scaledImage
    scaledImage = np.array(Image.fromarray(myImage).resize((scaled_width, scaled_height)))


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(500, 100)
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
