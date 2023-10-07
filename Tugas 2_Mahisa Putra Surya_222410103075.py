# Tugas 2
# Mahisa Putra Surya
# 222410103075

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

W, H = 500, 500

def draw():
    glColor3f(255.0, 255.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-200, -120)
    glVertex2f(-100, -120)
    glVertex2f(-120, -100)
    glVertex2f(-120, 220)     
    glVertex2f(-20, -120)     
    glVertex2f(20, -120) 
    glVertex2f(120, 220)
    glVertex2f(120, -100)
    glVertex2f(100, -120)
    glVertex2f(200, -120)
    glVertex2f(180, -100)
    glVertex2f(180, 260)
    glVertex2f(180, 260)
    glVertex2f(80, 260)
    glVertex2f(0, -40)
    glVertex2f(-80, 260)
    glVertex2f(-180, 260)
    glVertex2f(-180, -100)
    glEnd()

def iterate():
    glViewport(0, 0, W, H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(-W / 2, W, -H / 2, H, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(W, H)
glutInitWindowPosition(0, 0)
glutCreateWindow('Tugas 2_Mahisa Putra Surya_222410103075')
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()