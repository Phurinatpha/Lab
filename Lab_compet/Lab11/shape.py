from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def midshape(rx, ry, xc, yc):
    x = 0
    y = ry
    
    d1 = ((rx * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    
    while(dx < dy):
        points.extend([(x+xc, y+yc), (-x+xc, y+yc), (x+xc, -y+yc), (-x+xc, -y+yc)])
        
        if(d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
            
    d2 = ((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry)
    
    while(y >= 0):
        points.extend([(x+xc, y+yc), (-x+xc, y+yc), (x+xc, -y+yc), (-x+xc, -y+yc)])
        
        if(d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) # Background color: R, G, B, Alpha.
    gluOrtho2D(-30.0, 30.0, -30.0, 30.0) # L, R, T, B.


if __name__ == '__main__':
    points = []
    midshape(15, 25, 0, 0)
    print(len(points), points)
    print('x = ', points[0][0], '; y = ', points[0][1]) # The 1st point.

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    # glutInitWindowSize(500, 500)
    # glutInitWindowPosition(50, 50)
    glutCreateWindow('Plot 2D Points')
    glutDisplayFunc(plotpoints)
    
    init()
    glutMainLoop()