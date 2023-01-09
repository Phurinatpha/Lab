from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    #drawgrid
    glColor4f(1.0, 0.5, 0.0, 1.0)
    glBegin(GL_LINES)
    i = -5
    while(i <= 5):
        glVertex3f(i, 0, 5)
        glVertex3f(i, 0, -5)
        glVertex3f(5, 0, i)
        glVertex3f(-5, 0, i)
        i += 1
    glEnd()
    
    #Tetrahedron part
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(0, 2, 0)
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(0, 0, -1.4)
    glVertex3f(0, 2, 0)
    glVertex3f(-1, 0, 1)
    glEnd()

    glFlush()


def init():
    glClearColor(52.0/255.0,73.0/255.0,94.0/255.0,1.0)
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-2, 2, -1.5, 1.5, 1, 40)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -3)
    glRotatef(50, 1, 0, 0)
    glRotatef(70, 0, 1, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Tetrahedron")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()