#!/usr/bin/env python3

import objects_3d
import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

face = []
verticies = []
edge = []

def draw():

    obj_count = 7
    pyramids = [ objects_3d.Pyramid() for _ in range(obj_count)]

    glBegin(GL_LINES)

    for py in pyramids:

        #box.resize(f_hight= random.random() * 4)
        #print(box.info())

        for pol in py.polygons():
            py.info()
            print("pol:",pol)
            glVertex3fv(pol[0])
            glVertex3fv(pol[1])

    glEnd()

    
def move():
    glTranslatef(0.01, 0.01, 0.01)

def scale():
    glScalef(1.01, 1.01, 1.01)

def turn():
    glRotatef(1, 3, 1, 3)


def main():
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(145, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw()
#        gen_lines()
#        move()
        turn()
#        scale()
        pygame.display.flip()
        pygame.time.wait(10)



if __name__ == '__main__':
    main()
