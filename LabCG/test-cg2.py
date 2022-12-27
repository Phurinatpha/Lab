from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init(): 
    glClearColor(0.5, 0.0, 0.5, 1.0) #Dark magenta background color.
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def plotpeints(): 
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(10.0)
    glBegin(GL_POINTS) 
    glVertex2f(0.0, 0.0)
    glEnd()

    glColor3f(0.0, 1.0, 1.0) 
    glLineWidth(5.0)

    glBegin(GL_LINE_STRIP)
    glVertex2f(0.5, 0.0)
    glVertex2f(0.5, 0.5) 
    glVertex2f(0.0, 0.25)
    glVertex2f(0.5, 0.0)
    glEnd()

    glFlush()

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