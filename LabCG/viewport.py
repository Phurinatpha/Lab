from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def initGL():
    # Set "clearing" or background color
    glClearColor(0.0, 0.0, 0.0, 1.0) # Black and opaque

def display():
    glClear(GL_COLOR_BUFFER_BIT)   # Clear the color buffer with current clearing color

    # Define shapes enclosed within a pair of glBegin and glEnd
    glBegin(GL_QUADS)              # Each set of 4 vertices form a quad
    glColor3f(1.0, 0.0, 0.0) # Red
    glVertex2f(-0.8, 0.1)     # Define vertices in counter-clockwise (CCW) order
    glVertex2f(-0.2, 0.1)
    glVertex2f(-0.2, 0.7)
    glVertex2f(-0.8, 0.7)

    glColor3f(0.0, 1.0, 0.0) # Green
    glVertex2f(-0.7, -0.6)
    glVertex2f(-0.1, -0.6)
    glVertex2f(-0.1,  0.0)
    glVertex2f(-0.7,  0.0)

    glColor3f(0.2, 0.2, 0.2) # Dark Gray
    glVertex2f(-0.9, -0.7)
    glColor3f(1.0, 1.0, 1.0) # White
    glVertex2f(-0.5, -0.7)
    glColor3f(0.2, 0.2, 0.2) # Dark Gray
    glVertex2f(-0.5, -0.3)
    glColor3f(1.0, 1.0, 1.0) # White
    glVertex2f(-0.9, -0.3)
    glEnd()

    glBegin(GL_TRIANGLES)          # Each set of 3 vertices form a triangle
    glColor3f(0.0, 0.0, 1.0) # Blue
    glVertex2f(0.1, -0.6)
    glVertex2f(0.7, -0.6)
    glVertex2f(0.4, -0.1)

    glColor3f(1.0, 0.0, 0.0) # Red
    glVertex2f(0.3, -0.4)
    glColor3f(0.0, 1.0, 0.0) # Green
    glVertex2f(0.9, -0.4)
    glColor3f(0.0, 0.0, 1.0) # Blue
    glVertex2f(0.6, -0.9)
    glEnd()

    glBegin(GL_POLYGON)            # These vertices form a closed polygon
    glColor3f(1.0, 1.0, 0.0) # Yellow
    glVertex2f(0.4, 0.2)
    glVertex2f(0.6, 0.2)
    glVertex2f(0.7, 0.4)
    glVertex2f(0.6, 0.6)
    glVertex2f(0.4, 0.6)
    glVertex2f(0.3, 0.4)
    glEnd()

    # glBegin(GL_POLYGON)                   
    # radius = 0.2
    # ori_x = 0.0                        
    # ori_y = 0.0
    # for i in range(300):
    #     angle = 2 * math.pi * i / 300
    #     x = math.cos(angle) * radius
    #     y = math.sin(angle) * radius
    #     glVertex2d(ori_x + x, ori_y + y)
    
    # glEnd()

    # glBegin(GL_POLYGON)                   
    # radius = 0.325
    # ori_x = 0.0                       
    # ori_y = -0.475
    # for i in range(300):
    #     angle = 2 * math.pi * i / 300
    #     x = math.cos(angle) * radius
    #     y = math.sin(angle) * radius
    #     glVertex2d(ori_x + x, ori_y + y)
    
    # glEnd()

    # glBegin(GL_POLYGON)
                 
    # radius = 0.01
    # ori_x = 0.1                        
    # ori_y = 0.1
    # for i in range(300):
    #     angle = 2 * math.pi * i / 300
    #     x = math.cos(angle) * radius
    #     y = math.sin(angle) * radius
    #     glVertex2d(ori_x + x, ori_y + y)
    
    # glEnd()


    glFlush() 

def reshape(width, height):
    if height == 0:
        height = 1
    aspect = float(width) / float(height)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width >= height:
        gluOrtho2D(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0)
    else:
        gluOrtho2D(-1.0, 1.0, -1.0 / aspect, 1.0 / aspect)

def main():

    glutInit()
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Viewport Transform")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    initGL()
    glutMainLoop()


main()

