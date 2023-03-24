from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Globals for animation, ball position and direction of motion.
global x, y

# Initial position of the ball.
x = 0.34
y = 0.34

# Window dimensions.
width = height = 400

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 100, 0)
    # Set up projection matrix.
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def transform():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)

    # Define window coordinates.
    xw_min, xw_max, yw_min, yw_max = -0.5, 0.5, -0.5, 0.5

    # Define viewport coordinates.
    xv_min, xv_max, yv_min, yv_max = 0, width, 0, height

    # Compute viewport transformation parameters.
    sx = (xv_max - xv_min) / (xw_max - xw_min)
    sy = (yv_max - yv_min) / (yw_max - yw_min)
    tx = xv_min - sx * xw_min
    ty = yv_min - sy * yw_min

    # Set up viewport transformation matrix.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(xv_min, yv_min, xv_max-xv_min, yv_max-yv_min)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(tx, ty, 0.0)
    glScalef(sx, sy, 1.0)

    # Draw teapot.
    glutWireTeapot(0.5)

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow('Viewport')
    glutDisplayFunc(transform)
    init()
    glutMainLoop()

main()
