#5323 Beta 1.1

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
hz = 24
placeholder = "" #can be changed with no effect
menu_choice = ""
settings_choice = ""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

#Game
def menu():
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
    background_image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu1.png")), (1280, 720))
    background_timer = 1
    background_count = 1

    #Joystick Stuff
    def menu_navigation(movement_up, background_count):
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
                    
            # Axis 0: Left/Right movement
            up_y = joystick.get_axis(1)

            if up_y >= 0.1: 
                movement_up = True
            if up_y <= -0.1:
                movement_up = False        
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                 pass
            


        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
                movement_up = True
                if movement_up == True and background_count >= 2:
                    background_count -= 1
                    
                if movement_up == False and background_count <= 6:
                    background_count += 1
                pass
        


        if pressed_keys[K_DOWN]:
                movement_up = False
                if movement_up == True and background_count >= 2:
                    background_count -= 1
            
                if movement_up == False and background_count <= 6:
                    background_count += 1
                pass
        



        if pressed_keys[K_RETURN]:
                pass
        return movement_up, background_count
        






    def which_Background(background_timer, background_image, background_count):
        if background_timer == 1:
            background_image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu0.png")), (1280, 720))
        if background_count == 1:
            background_image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu1.png")), (1280, 720))
        background_timer *= -1
        return background_image

        
            



    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                menu_navigation()

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        
        menu_navigation(movement_up, background_count)
        which_Background(background_timer, background_image, background_count)

        #Cirtical Screen Stuff
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()

menu()