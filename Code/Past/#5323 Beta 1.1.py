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
    RLEACCEL,
    K_s,
    K_w,
)

#variables
hz = 24
placeholder = "" #can be changed with no effect
menu_choice = ""
settings_choice = ""
sprite_timer = 100
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu1.png")), (1280, 720))
background_image0 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu0.png")), (1280, 720))
menu_in_use = 1



#Game
def menu(BASE_DIR):
    #ESSENTIAL CODE DO NOT TOUCH
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    global background_image1
    global background_image0
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()
    running = True
    #variables
    hz = 24
    placeholder = "" #can be changed with no effect
    menu_choice = ""
    settings_choice = ""
    sprite_timer = 100
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu1.png")), (1280, 720))
    background_image0 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu0.png")), (1280, 720))
    menu_in_use = 1

    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.RESIZABLE) 
    pygame.display.set_caption("Last Stand")
    
    class Menu(pygame.sprite.Sprite):
        def __init__(self):
            super(Menu, self).__init__()
            self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        def update(self, pressed_keys, menu_in_use, sprite_timer, background_image1, background_image0):

            if pressed_keys[K_UP] and menu_in_use > 1:
                menu_in_use -= 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Menu{menu_in_use}.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

            if pressed_keys[K_DOWN] and menu_in_use < 7:
                menu_in_use += 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Menu{menu_in_use}.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

            #Joystick Stuff
            if pygame.joystick.get_count() > 0:
                joystick = pygame.joystick.Joystick(0)
                joystick.init()
                up_y = joystick.get_axis(1)

                #Player Movement
                if up_y <= -0.1:
                    menu_in_use += 1
                    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Menu{menu_in_use}.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                
                if up_y >= 0.1:
                    menu_in_use += 1
                    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Menu{menu_in_use}.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
            return menu_in_use, sprite_timer, background_image1, background_image0

    Menu1 = Menu()

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

            pressed_keys = pygame.key.get_pressed()
            menu_in_use, sprite_timer, background_image1, background_image0 = Menu1.update(pressed_keys, menu_in_use, sprite_timer, background_image1, background_image0)
            print(menu_in_use)
        
        #Cirtical Screen Stuff
        screen.blit(Menu1.surf, Menu1.rect)        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

menu(BASE_DIR)




