import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import threading
import random



""" constants """
MOVING_SPEED = 0.1

""" globals """
score = 0

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

colors = (
    (10,1,1),
    (1,0,1),
    (1,1,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (1,1,0),
    (1,1,0),
    (0,0,1)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

keys_pressed = {
    "A":False,
    "W":False,
    "S":False,
    "D":False
}


def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def controls():
    while True:
        if keys_pressed["A"]:
            glTranslatef(-0.5, 0.0, 0.0)
            time.sleep(2)
        elif keys_pressed["D"]:
            glTranslatef(0.5, 0.0, 0.0)
            time.sleep(2)
        elif keys_pressed["W"]:
            glTranslatef(0.0, 0.5, 0.0)
            time.sleep(2)
        elif keys_pressed["S"]:
            glTranslatef(0.0, -0.5, 0.0)
            time.sleep(2)



def main():
    global score

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) 
    glTranslatef(random.randrange(-10,10), 0.0, -25) 
 #   glRotate(1, 1, 1000, 1) 

    object_passed = False

    

    while not object_passed:

        if keys_pressed["A"]:
            glTranslatef(-0.5, 0.0, 0.0)
            time.sleep(0.1)
        elif keys_pressed["D"]:
            glTranslatef(0.5, 0.0, 0.0)
            time.sleep(0.1)
        elif keys_pressed["W"]:
            glTranslatef(0.0, 0.5, 0.0)
            time.sleep(0.1)
        elif keys_pressed["S"]:
            glTranslatef(0.0, -0.5, 0.0)
            time.sleep(0.1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keys_pressed["A"] = True
                elif event.key == pygame.K_RIGHT:
                    keys_pressed["D"] = True
                elif event.key == pygame.K_UP:
                    keys_pressed["W"] = True
                elif event.key == pygame.K_DOWN:
                    keys_pressed["S"] = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys_pressed["A"] = False
                elif event.key == pygame.K_RIGHT:
                    keys_pressed["D"] = False
                elif event.key == pygame.K_UP:
                    keys_pressed["W"] = False
                elif event.key == pygame.K_DOWN:
                    keys_pressed["S"] = False

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslatef(0,0,1.0)
            #     elif event.button == 5:
            #         glTranslate(0,0,-1.0)        
               
    

        x = glGetDouble(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2] 

        if camera_z <= 0:
            score += 10
            main()

        if score <= 50:
            glTranslatef(0,0,MOVING_SPEED + ((score+1)/100))
        else:
            glTranslatef(0,0,MOVING_SPEED + 0.8)
       
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
