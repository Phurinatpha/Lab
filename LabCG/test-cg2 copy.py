from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


def init(): 
    glClearColor(0.5, 0.0, 0.5, 1.0) #Dark magenta background color.
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def plotpeints(): 
    glBegin(GL_POLYGON)                   
    radius = 0.2
    ori_x = 0.0                        
    ori_y = 0.0
    for i in range(300):
        angle = 2 * math.pi * i / 300
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        glVertex2d(ori_x + x, ori_y + y)
    
    glEnd()

def main():
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
    glutInitWindowSize(480, 480)

    #glutInitWindowPosition(50, 501)
    glutCreateWindow("Plot 20 Points")
    glutDisplayFunc(plotpeints)

    init() 
    glutMainLoop()

main()