from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

# Globals for animation, ball position and direction of motion.
global x, y

# Initial position of the ball.
x = 0.34
y = 0.34

# Window dimenstions.
width = height = 600
axrng = 1.5

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 100, 0)
    # Dimensions of the screen (try increase axrng).
    gluOrtho2D(-axrng, axrng, -axrng, axrng)
    
def transform():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    
    yw_max = 500 # height
    xw_max = 500 # width
    yw_min = 0 # height
    xw_min = 0 # width
    
    yv_max = 400 # height
    xv_max = 400 # width
    yv_min = 0 # height
    xv_min = 0 # width
    
    sx = (xv_max - xv_min)/(xw_max - xw_min)
    sy = (yv_max - yv_min)/(yw_max - yw_min)
    
    tx = ((xw_max * xv_min) - (xw_min * xv_max))/(xw_max - xw_min)
    ty = ((yw_max * yv_min) - (yw_min * yv_max))/(yw_max - yw_min)
    
    win_view = [sx, 0, 0, 0, 
                0, sy, 0, 0, 
                tx, ty, 1, 0,
                0, 0, 0, 1]
    
    win_norm = [2/(xw_max - xw_min), 0, 0, 0, 
                0, 2/(yw_max - yw_min), 0, 0, 
                -(xw_max + xw_min)/(xw_max - xw_min), -(yw_max + yw_min)/(yw_max - yw_min), 1, 0,
                0, 0, 0, 1]

    norm_view = [(xv_max - xv_min)/2, 0, 0, 0, 
                0, (yv_max - yv_min)/2, 0, 0, 
                (xv_max + xv_min)/2, (yv_max + yv_min)/2, 1, 0,
                0, 0, 0, 1]
    win_normf = np.array(win_norm, dtype = float)
    norm_viewf = np.array(norm_view, dtype = float)
    
    # Transform the object.
    glPushMatrix()
    
    # glMultMatrixf(win_view)
    
    # glMultMatrixf(norm_viewf)
    # glMultMatrixf(win_normf)
    
   
    glMultMatrixf(win_normf)
    glMultMatrixf(norm_viewf)
    
    glutWireTeapot(0.5) # Size.
    # glutWireCube(0.5) # Size.
    
    glPopMatrix()
    
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