# Tugas 4
# Mahisa Putra Surya
# 222410103075

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w, h, x, y, a, sc, r, s = 500, 500, 0, 0, 0, 0, 100.0, 0.2
dx, dy, da, dsc = s, s, s, s


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
    global w, h, x, y, a, sc, r, dx, dy, da, dsc
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(-w, w, -h, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # collision detection :)
    if x + r >= w:
        # jika bertabrakan dengan viewport kanan, maka bergerak ke kiri
        dx = -s
    elif x - r <= -w:
        # jika bertabrakan dengan viewport kiri, maka bergerak ke kanan
        dx = s

    if y + r >= h:
        # jika bertabrakan dengan viewport atas, maka bergerak ke bawah
        dy = -s
        if dx == -s:
            # jika bergerak ke arah kiri, maka rotasi harus ke arah kiri (berlawanan dengan arah jarum jam)
            da = s
        elif dx == s:
            # selain itu, jika bergerak ke arah kanan, maka rotasi harus ke arah kanan (searah dengan jarum jam)
            da = -s
    elif y - r <= -h:
        # jika bertabrakan degan viewport bawah, maka bergerak ke atas
        dy = s
        if dx == -s:
            # jika bergerak ke arah kiri, maka rotasi harus ke arah kiri (berlawanan dengan arah jarum jam)
            da = s
        elif dx == s:
            # selain itu, jika bergerak ke arah kanan, maka rotasi harus ke arah kanan (searah dengan jarum jam)
            da = -s

    if dsc == s and sc >= 1.0:
        # jika ukuran logo lebih besar atau sama dengan 2x lipat dari ukuran aslinya, maka kecilkan
        dsc = -s
    elif dsc == -s and sc <= 0.0:
        # jika ukuran logo lebih kecil atau sama dengan 1x lipat dari ukuran aslinya, maka besarkan
        dsc = s

    x += dx
    y += dy

    a += da

    sc += dsc * 0.001 # 0.1%
    r = 100.0 * (1.0 + sc)

    glTranslatef(x, y, 0.0)

    glRotatef(a, 0, 0, 1)

    glScalef(1.0 + sc, 1.0 + sc, 0)

    if 360 >= a <= -360:
        # jika rotasi sudah 360°, atur a menjadi 0°
        a = 0


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw()
    glutSwapBuffers()


def reshape(w_new, h_new):
    global w, h
    w, h = w_new, h_new


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow('Tugas 4_Mahisa Putra Surya_222410103075')
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutReshapeFunc(reshape)
glutMainLoop()
