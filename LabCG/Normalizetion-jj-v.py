from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np
from PIL import Image

global x, y

x = 0.34
y = 0.34

width = height = 500

axrng = 1

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
    image = loadImage("/Lab/LabCG/img/or-cat.png")
    
    # Convert the image to a format that can be used by glDrawPixels
    image_data, img_width, img_height = makeImage(image)

    # Create a numpy array from the image data
    image_array = np.array(image_data, dtype=np.uint8)
    
    # Store the image array as a global variable
    global myImage
    myImage = image_array
    
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 100, 0)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-axrng, axrng, -axrng, axrng)
    


def tranform():
    global x, y
    
    glClear(GL_COLOR_BUFFER_BIT)
    wx_mx = 200
    wy_mx = 200
    wx_mn = 100
    wy_mn = 100
    Mws = [2/(wx_mx-wx_mn), -(wx_mx + wx_mn)/(wx_mn-wx_mx),2/(wy_mx-wy_mn),-(wy_mx + wy_mn)/(wy_mx-wy_mn)]
    
    vx_mx = width
    vy_mx = height
    vx_mn = 0
    vy_mn = 0
    Mv = [(vx_mx-vx_mn)/2, (vx_mx + vx_mn)/2,(vy_mx-vy_mn)/2,(vy_mx + vy_mn)/2]

    Nor_s = [
        Mws[0], 0, Mws[1], 0, 
        0, Mws[2], Mws[3], 0, 
        0, 0, 1, 0,
        0, 0, 0, 1]
    sher_y = [
        Mv[0], 0, Mv[1], 0, 
        0, Mv[2], Mv[3], 0, 
        0, 0, 1, 0,
        0, 0, 0, 1]
    sherf1 = np.array(Nor_s, dtype=float)
    sherf2 = np.array(sher_y, dtype=float)
    
    
    # glPushMatrix()
    # glTranslatef(.0, .0, .0)
    # glMultMatrixf(sherf1)
    # glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, myImage)

    # glPopMatrix()

    glPushMatrix()
    glMultMatrixf(sherf2)
    glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, myImage)
    
    glPopMatrix()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow('Tranformation: Reflection')
    glutDisplayFunc(tranform)

    init()
    glutMainLoop()


main()
