from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

global x, y 

# Initial position of the ball.
x = 0.34
y = 0.34

# Window dimensions.
width = height = 500
axrng = 1.5

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 100, 0)

    # Dimensions of the screen (try increase axrng).
    gluOrtho2D(-axrng, axrng, -axrng, axrng)

def transform():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)

    reflect_x = [1,0,0,0,0,-1,0,0,0,0,1,0,0,0,0,1]
    reflect_y = [-1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]
    reflect_xy = [-1,0,0,0,0,-1,0,0,0,0,1,0,0,0,0,1]
    reflectf1 = np.array(reflect_xy, dtype=float)
    reflectf2 = np.array(reflect_xy, dtype=float)

    # transform the object.
    glPushMatrix()

    glRotatef(-45., 0., 0., 1.)

    glutWireTeapot(0.5)

    glPopMatrix()

    # The 2nd object.
    glColor3ub(0, 100, 100)
    glPushMatrix()

    glTranslatef(-.5, -.5, 0.)
    glRotatef(-45., 0., 0., 1.)
    glRotatef(180., 0., 1., 0.)
    glMultMatrixf(reflectf2)

    glutWireTeapot(0.5)

    glPopMatrix()

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Transformation: Reflection')
    glutDisplayFunc(transform)

    init()
    glutMainLoop() 

main()