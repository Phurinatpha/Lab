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

    sh_x = .4
    sh_y = -.5
    shear_x = [1,0,0,0,sh_x,1,0,0,0,0,1,0,0,0,0,1]
    shear_y = [1,sh_y,0,0,0,1,0,0,0,0,1,0,0,0,0,1]
    shear_xy = [1,-sh_y,0,0,-sh_x,1,0,0,0,0,1,0,0,0,0,1]
    shearf1 = np.array(shear_x, dtype=float)
    shearf2 = np.array(shear_y, dtype=float)
    shearf3 = np.array(shear_xy, dtype=float)
    

    # transform the object.
    glPushMatrix()

    glMultMatrixf(shearf1)

    glutWireTeapot(0.5)

    glPopMatrix()

    # The 2nd object.
    glColor3ub(0, 100, 100)
    glPushMatrix()

    glTranslatef(0., .8, 0.)
    glMultMatrixf(shearf2)

    glutWireTeapot(0.5)

    glPopMatrix()

    # The 2nd object.
    glColor3ub(100, 0, 100)
    glPushMatrix()

    glTranslatef(0., -.8, 0.)
    glMultMatrixf(shearf3)

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