#5323 Beta Menu 0.1

#Importations
import os
from fastapi import background
import pygame 
import sys
from tkinter import *
from pygame.locals import (
    K_DOWN,
    K_UP,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

#variables
placeholder = "" #can be changed with no effect
menu_choice = ""
settings_choice = ""

#Game
def menu():
    #Variables
    sprite_timer = 100

    #ESSENTIAL CODE DO NOT TOUCH
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()
    running = True

    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.RESIZABLE) 
    pygame.display.set_caption("Last Stand")

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    movement_up = True
    background_timer = 1
    background_count = 1

    #Joystick Stuff
    def menu_navigation():
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
                    
            # Axis 0: Left/Right movement
            up_y = joystick.get_axis(1)

            if up_y >= 0.1: 
                movement_up = True
                new_background(movement_up, background_count)
            if up_y <= -0.1:
                movement_up = False        
                new_background(movement_up, background_count)
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                 pass
            
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
                movement_up = True
                new_background(movement_up, background_count)
                pass
        if pressed_keys[K_DOWN]:
                movement_up = False
                new_background()
                pass
        if pressed_keys[K_RETURN]:
                pass
        

    def which_Background(background_timer, background_image, background_count):
        if background_timer == 1:
             print ("Background is 0")
        elif background_count == 1:
             print ("Background is 1")
        elif background_count == 2:
             print ("Background is 2")
        elif background_count == 3:
             print ("Background is 3")
        elif background_count == 4:
             print ("Background is 4")
        elif background_count == 5:
             print ("Background is 5")
        elif background_count == 6:
             print ("Background is 6")
        elif background_count == 7:
             print ("Background is 7")
        background_timer *= -1
        return background_image

    def new_background(movement_up, background_count):
        if movement_up == True and background_count >= 2:
            background_count -= 1
            
        if movement_up == False and background_count <= 6:
            background_count += 1
            return background_count
            



    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                menu_navigation()

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        
        menu_navigation()
        which_Background(background_timer, background_count)

        #Cirtical Screen Stuff
        pygame.display.flip()

    pygame.quit()
    sys.exit()

menu()