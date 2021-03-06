#!/usr/bin/env python3

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import * 


face = []
verticies = []
edge = []

def face_to_edge():
    for f in face:
        if 37 in f:
            continue
        edge.append([f[0],f[1]])
        edge.append([f[0],f[2]])
        edge.append([f[1],f[2]])


def readfile():
    with open("test.obj") as fd:
        for line in fd:
            value = line.split()

            if len(value) == 4:
                if value[0] == "f":
                    face.append( [int(value[1]), int(value[2]), int(value[3])])
            
                if value[0] == "v":
                    verticies.append( [float(value[1]), float(value[2]), float(value[3])] )

    face_to_edge()


#def grow():
#    for i in range(len(verticies)):
#        verticies[i] *= 2



def Cube():
    glBegin(GL_LINES)
    for e in edge:
        for vertex in e:
#            print(vertex)
            glVertex3fv(verticies[vertex])
#    grow()
    glEnd()



def main():

    readfile()

    print("---")
    for v in verticies:
        print(v)
    print("-")
    for e in edge:
        print(e)
    print("-")
    for f in face:
        print(f)
    print("---")



    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()

