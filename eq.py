#!/usr/bin/env python3

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

import objects_3d

face = []
verticies = []
edge = []



def draw_eq():

    mx = 8
    my = 2
    mz = 2

    box_count = 7


    glBegin(GL_LINES)


    eq = [ objects_3d.Box() for _ in range(box_count)]
    for box in eq:
        box.resize(f_hight= random.random() * 4)
        #print(box.info())
        for line in box.lines:
            glVertex3fv(line[0])
            glVertex3fv(line[1])

    glEnd()

    

#    mx = 8
#    my = 2
#    mz = 2
#
#    eq = [ [x,y,z] for x in range(mx) for y in range(my) for z in range(mz) ]
#    print("\neq:::",eq)
#
#    glBegin(GL_LINES)
#    for x in range(len(eq)):
#        glVertex3fv(eq[x])
#        glVertex3fv(eq[(x+4) % len(eq)])
#
#    for x in zip(*(iter(eq),) * mx):
#        print("trick", x)
#        for y in zip(*(iter(x),) * my * mz):
#            print("  trick", y)
#            for c in range(len(y)):
#                glVertex3fv(y[c])
#                glVertex3fv(y[(c + 1) % len(y)])
#


#    for x in range(len(eq)):
#        glVertex3fv(eq[x])
#        glVertex3fv(eq[(x+2) % len(eq)])



#    glEnd()

#    mx = 8
#    my = 2
#    mz = 2
#
#    eq = [ [[[x,y,z] for z in range(mz)  ] for y in range(my) ] for x in range(mx) ]
#
#    #eq_test = [x,  ]
#    print(eq)
#
#
#    glBegin(GL_LINES)
#    for x in eq:
#        for y in x:
#            glVertex3fv(y[0])
#            glVertex3fv(y[1])
#
#    for x in eq:
#        for y in range(my):
#            
#            glVertex3fv(x[0][y])
#            glVertex3fv(x[1][y])
#
#
#    glEnd()
#        



#    eqf = [[x,y,0] for x in range(mx) for y in range(my)]
#    eqb = [[x,y,1] for x in range(mx) for y in range(my)]
#
#    print(eqf, eqb)
#
#    glBegin(GL_LINES)
#    for c in range(len(eqf)):
#        glVertex3fv(eqf[c])
#        glVertex3fv(eqb[c])
#    glEnd()
#   



#    eq = [[x,z,y] for z in range(mz) for y in range(my) for x in range(mx) ]
#    glBegin(GL_LINES)
#    for x in range(mx):
#        glVertex3fv(eq[x])
#        glVertex3fv(eq[x+mx])
#
#    for c in range(len(eq)):
#        glVertex3fv(eq[c])
#        if c + 1 == len(eq):
#            c = 1
#        glVertex3fv(eq[c+1])
#
#
#
#    #for e in range(len(eq)):
#    #   for q in range(len(eq)):
#
#
#     #       glVertex3fv(eq[e])
#     #       glVertex3fv(eq[q])
#    glEnd()


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
        draw_eq()
        #gen_lines()
#        move()
#        turn()
#        scale()
        pygame.display.flip()
        pygame.time.wait(10)




if __name__ == '__main__':
    main()
