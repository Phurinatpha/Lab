from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)
    # glutSolidTeapot(0.5)
    # glutWireSquere(0.5,10,10)
    # glutWireCube(1.0)
    # glutWireTetrahedron()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutCreateWindow("Wire Teapot by PyOpenGL")
glutDisplayFunc(draw)
glutMainLoop()