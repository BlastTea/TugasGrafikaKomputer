# Tugas 3
# Mahisa Putra Surya
# 222410103075

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

W, H = 500, 500

def draw_circle(start_angle_degrees, angle_degrees, radius, num_segment, x_center, y_center):
    start_angle = math.radians(start_angle_degrees)
    angle = math.radians(angle_degrees)

    glBegin(GL_POLYGON)

    if ((angle_degrees - start_angle_degrees).__abs__() != 360):
        glVertex2f(x_center, y_center)

    for i in range(num_segment):
        theta = start_angle + (angle * i / num_segment)
        x = x_center + radius * math.cos(theta)
        y = y_center + radius * math.sin(theta)
        glVertex2f(x, y)

    glVertex2f(x_center, y_center)

    glEnd()

def draw():
    # Background
    glColor3f(200 / 255, 19 / 255, 92 / 255)
    draw_circle(0, 360, 100.0, 100, 0, 0)

    # Face outline
    glColor3f(1.0, 1.0, 1.0)
    draw_circle(90, 275, 80.0, 100, 0, 0)
    glColor3f(200 / 255, 19 / 255, 92 / 255)
    draw_circle(90, 275, 70.0, 100, 0, 0)

    glColor3f(1.0, 1.0, 1.0)
    # The eye
    draw_circle(0, 360, 10.0, 100, -30, 30)

    # Horizontal line on G
    glBegin(GL_POLYGON)
    glVertex2f(80, 5)
    glVertex2f(20, 5)
    glVertex2f(20, -5)
    glVertex2f(80, -5)
    glEnd()

    # Vertical line on L
    glBegin(GL_POLYGON)
    glVertex2f(-5, -40)
    glVertex2f(5, -40)
    glVertex2f(5, 40)
    glVertex2f(-5, 40)
    glEnd()

    # Horizontal line on L
    glBegin(GL_POLYGON)
    glVertex2f(-5, -30)
    glVertex2f(20, -30)
    glVertex2f(20, -40)
    glVertex2f(-5, -40)
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
glutCreateWindow('Tugas 3_Mahisa Putra Surya_222410103075')
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
