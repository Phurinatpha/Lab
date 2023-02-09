from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

# globals for animation
global anim, x, y ,dx, dy, deg, s

# Initial position of the ball.
x = -0.67
y = 0.34
deg = 0 #Degrees.

s = 0
scale = []
for f in np.arange(0.5, 3.0, 0.01):
    scale.append(f)
for f in np.arange(3.0, 0.6, -0.01):
    scale.append(f)

# Direction 'sign' of the ball's motion
dx = dy = 1

# Window dimensions.
width = height = 500
axrng = 1.0

# No animation to start.
anim = 0 
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 100, 0)

    # Dimensions of the screen (try increase axrng).
    gluOrtho2D(-axrng, axrng, -axrng, axrng)

def idle():
    if anim == 1:
        glutPostRedisplay()

def bounce():
    global x, y, dx, dy, deg, s
    glClear(GL_COLOR_BUFFER_BIT)

    # Change x, y, & deg.
    x += 0.001 * dx
    y += 0.001 * dy
    deg += 1

    s = (s+1) % len(scale)

    # Move the ball location based on x & y.
    glPushMatrix()

    glTranslate(x, y, 0)
    glRotated(deg, 1, 0, 0) #angle, x, y, z.
    glScalef(scale[s], scale[s], scale[s])

    glutWireSphere(0.1, 20, 20) #radiusm, slice, stacks.
    # glutSolidSphere(0.1, 50, 50)
    glPopMatrix()

    # Collision detection
    if x >= axrng - 0.1 or x <= -axrng + 0.1:
        dx = -1 * dx
    if y >= axrng - 0.1 or y <= -axrng + 0.1:
        dy = -1 * dy

    # glFlush()
    glutSwapBuffers()

def keyboard(key, x, y):
    # Animate by pressing 'a' and stop by 's'.
    global anim

    if key == b'a':
        anim = 1 
    if key == b's':
        anim = 0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Bounce')
    glutDisplayFunc(bounce)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboard)

    init()
    glutMainLoop() 

main()