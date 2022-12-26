from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-3.0, 5.0, -5.0, 5.0)

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.5, 0.5, 0.5)
    glLineWidth(3.0)

    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0) 
    glEnd()

    glColor3f(0.0, 0.0, 0.5) 
    glPointSize(5.0)

    for x in arange(-5.0, 5.0, 0.1): 
        y= x*x
        glBegin(GL_POINTS)
        glVertex2f(x, y) 
        glEnd()
        glFlush()

    sys.exit()

def main():

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow('Function Plotter')
    glutInitWindowPosition(50, 50) 
    glutInitWindowSize(400, 400)
    glutDisplayFunc(plotfunc)
    # glutKeyboardFunc(keyboard)

    init()

    glutMainLoop()

main()