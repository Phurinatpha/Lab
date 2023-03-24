from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np

global x, y

x = 0.34
y = 0.34

# Window dimenstions.
width = 600
height = 500
axrng = 1.0

def load_texture(texture_file):
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    img = Image.open(texture_file)
    img_data = np.array(list(img.getdata()), np.uint8)
    img_data = np.flipud(img_data)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texture_id

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-axrng, axrng, -axrng, axrng)

def transform():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    
    yw_max = 400 # height
    xw_max = 550 # width
    yw_min = 0 # height
    xw_min = 0 # width
    
    yv_max = 350 # height
    xv_max = 400 # width
    yv_min = 0 # height
    xv_min = 0 # width
    
    sx = (xv_max - xv_min)/(xw_max - xw_min)
    sy = (yv_max - yv_min)/(yw_max - yw_min)
    
    tx = ((xw_max * xv_min) - (xw_min * xv_max))/(xw_max - xw_min)
    ty = ((yw_max * yv_min) - (yw_min * yv_max))/(yw_max - yw_min)

    win_view = np.array([sx, 0, 0, 0,
                        0, sy, 0, 0,
                        0, 0, 1, 0,
                        tx, ty, 0, 1]).reshape((4, 4))


    win_norm = np.array([2/(xw_max - xw_min), 0, 0, 0,
                         0, 2/(yw_max - yw_min), 0, 0,
                         0, 0, 1, 0,
                         -(xw_max + xw_min)/(xw_max - xw_min), -(yw_max + yw_min)/(yw_max - yw_min), 0, 1]).reshape((4, 4))

    norm_view = np.array([(xv_max - xv_min)/2, 0, 0, 0,
                          0, (yv_max - yv_min)/2, 0, 0,
                          0, 0, 0.5, 0,
                          0.5, 0.5, 0.5, 1]).reshape((4, 4))
    
    # Transform the object.
    # win_viewf = np.array(win_view, dtype=float)
    # win_normf = np.array(win_norm, dtype=float)
    norm_viewf = np.array(norm_view, dtype=float)

    full_transform = np.matmul(win_view, np.matmul(win_norm, norm_view)) 
    
    texture_id = load_texture("/Lab/LabCG/img/or-cat.png")

    # Apply the transformation to the object.
    glPushMatrix()
    glMultMatrixf(win_view) # window view
    glTranslatef( -.9,0,0.)
    # Enable texturing.
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glTexCoord2f(1.0, 1.0)
    glVertex2f(-0.5, 0.5)
    glTexCoord2f(0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Finish the frame.
    glPopMatrix()

    # Apply the transformation to the object.
    glPushMatrix()
    glMultMatrixf(win_norm) # window view
    glScalef(80,80,80)
    glTranslatef( 2.5,1.8,0.)
    # Enable texturing.
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glTexCoord2f(1.0, 1.0)
    glVertex2f(-0.5, 0.5)
    glTexCoord2f(0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Finish the frame.
    glPopMatrix()


    # New object.
    glPushMatrix()
    glMultMatrixf(norm_viewf) #viewport
    glScalef(100,100,100)
    glTranslatef( 4.,1.8,0.)
    # Enable texturing.
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glTexCoord2f(1.0, 1.0)
    glVertex2f(-0.5, 0.5)
    glTexCoord2f(0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Finish the frame.
    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(450, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow('Window to Viewport')
    glutDisplayFunc(transform)
    init()
    glutMainLoop()

main()