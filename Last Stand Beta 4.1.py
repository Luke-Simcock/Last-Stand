#5323 Alpha 2.2.1

#Importations
import os
import pygame 
import random
import sys
import time
import threading
from fastapi import background
from ctypes import windll
from tkinter import *
from pygame.locals import (
    RLEACCEL,
    K_DOWN,
    K_RETURN,
    K_UP,
    K_q,
    K_w,
    K_e,
    K_r,
    K_t,
    K_y,
    K_i,
    K_o,
    K_p,
    K_a,
    K_s,
    K_d,
    K_f,
    K_g,
    K_h,
    K_j,
    K_k,
    K_l,
    K_z,
    K_x,
    K_c,
    K_v,
    K_b,
    K_n,
    K_m,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_0,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#variables
hz = 24
placeholder = "" #can be changed with no effect
stop_music = False
menu_choice = ""
settings_choice = ""
sprite_timer = 100
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
storage_file = os.path.join(BASE_DIR, "TextFolders", "Storage.txt")
background_image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Background1.png")), (1280, 720))
background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Menu1.png")), (1280, 720))
menu_in_use = 1


#Menu
def menu(BASE_DIR):
    #ESSENTIAL CODE DO NOT TOUCH
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    global background_image1
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

        def update(self, pressed_keys, menu_in_use, sprite_timer, background_image1, BASE_DIR):

            if pressed_keys[K_UP] and menu_in_use > 1:
                menu_in_use -= 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Menu{menu_in_use}.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

            if pressed_keys[K_DOWN] and menu_in_use < 7:
                menu_in_use += 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Menu{menu_in_use}.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
            
            #========================  Redirect to next function  =====================#
            if pressed_keys[K_RETURN] and menu_in_use == 1: #game
                start_confirm(BASE_DIR)
            if pressed_keys[K_RETURN] and menu_in_use == 2: #settings
                pass
            if pressed_keys[K_RETURN] and menu_in_use == 3: #tutorial/controls
                pass
            if pressed_keys[K_RETURN] and menu_in_use == 4: #leaderboard
                pass
            if pressed_keys[K_RETURN] and menu_in_use == 5: #account (sign in)
                accounts(BASE_DIR)
            if pressed_keys[K_RETURN] and menu_in_use == 6: #credits
                pass
            if pressed_keys[K_RETURN] and menu_in_use == 7: #quit game
                pygame.quit()
                sys.exit()
            return menu_in_use, sprite_timer, background_image1, 

    Menu1 = Menu()

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

            pressed_keys = pygame.key.get_pressed()
            menu_in_use, sprite_timer, background_image1,  = Menu1.update(pressed_keys, menu_in_use, sprite_timer, background_image1, BASE_DIR)
             
        
        #Cirtical Screen Stuff
        screen.blit(Menu1.surf, Menu1.rect)        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

#start confirmation
def start_confirm(BASE_DIR):
    #ESSENTIAL CODE DO NOT TOUCH
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    global background_image1
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
    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Start_confirm-2.png.png")), (1280, 720))
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

        def update(self, pressed_keys, menu_in_use, sprite_timer, background_image1, ):

            if pressed_keys[K_UP]:
                menu_in_use = 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Start_confirm-2.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

            if pressed_keys[K_DOWN]:
                menu_in_use = 2
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Start_confirm-3.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
            
            #========================  Redirect to next function  =====================#
            if pressed_keys[K_RETURN] and menu_in_use == 1: #game
                game()
            if pressed_keys[K_RETURN] and menu_in_use == 2: #menu
                menu(BASE_DIR)
            return menu_in_use, sprite_timer, background_image1, 

    Menu1 = Menu()

    time.sleep(0.5)

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

            pressed_keys = pygame.key.get_pressed()
            menu_in_use, sprite_timer, background_image1,  = Menu1.update(pressed_keys, menu_in_use, sprite_timer, background_image1, )
             
        
        #Cirtical Screen Stuff
        screen.blit(Menu1.surf, Menu1.rect)        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

#accounts
def accounts(BASE_DIR):
    #ESSENTIAL CODE DO NOT TOUCH
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    global background_image1
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
    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Accounts-2.png.png")), (1280, 720))
    menu_in_use = 1
    details_sent = False

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

    Menu1 = Menu()

    textfont = pygame.font.SysFont("monospace", 50) 
    username = ""
    username_entered = False
    password = ""
    password_entered = False


    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

            pressed_keys = pygame.key.get_pressed()
             
        
        if username_entered == False:
            
            menu_in_use = 1
            background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Accounts-1.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
            Menu1.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_RETURN:
                    username_entered = True
                    menu_in_use = 2
                    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Accounts-2.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                    Menu1.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                else:
                    username += event.unicode
                    print(username)

        elif password_entered == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                elif event.key == pygame.K_RETURN:
                    password_entered = True
                    menu_in_use = 3
                    background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Accounts-3.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                    Menu1.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                else:
                    password += event.unicode
        
        else:
            

            if pressed_keys[K_UP] and menu_in_use > 3:
                menu_in_use -= 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Accounts-{menu_in_use}.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                Menu1.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

            if pressed_keys[K_DOWN] and menu_in_use < 5:
                menu_in_use += 1
                background_image1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", f"Accounts-{menu_in_use}.png.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                Menu1.surf = pygame.transform.scale(background_image1.convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
            
            #========================  Redirect to next function  =====================#
            if pressed_keys[K_RETURN] and menu_in_use == 3: #sign up
                start_confirm(BASE_DIR)
            if pressed_keys[K_RETURN] and menu_in_use == 4: #sign in
                pass
            if pressed_keys[K_RETURN] and menu_in_use == 5: #menu
                menu(BASE_DIR)



        print (menu_in_use)

        username_printed = textfont.render(f" {username}", 1, (255,255,255))  
        password_printed = textfont.render(f" {password}", 1, (255,255,255))  

        #Cirtical Screen Stuff
        screen.blit(Menu1.surf, Menu1.rect) 
        screen.blit(username_printed, (60, 175))
        screen.blit(password_printed, (60, 225))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

#Accounts
def get_storage_data():
    with open(storage_file, "r") as f:
        lines = f.readlines()

    name1, password1, score1 = lines[0].strip().split("|")
    name2, password2, score2 = lines[1].strip().split("|")
    name3, password3, score3 = lines[2].strip().split("|")
    name4, password4, score4 = lines[3].strip().split("|")
    name5, password5, score5 = lines[4].strip().split("|")

    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    score4 = int(score4)
    score5 = int(score5)

    print(f"Name: {name1}, Password: {password1}, Score: {score1}")
    print(f"Name: {name2}, Password: {password2}, Score: {score2}")
    print(f"Name: {name3}, Password: {password3}, Score: {score3}")
    print(f"Name: {name4}, Password: {password4}, Score: {score4}")
    print(f"Name: {name5}, Password: {password5}, Score: {score5}")

    scores = [score1, score2, score3, score4, score5]
    names = [name1, name2, name3, name4, name5]
    passwords = [password1, password2, password3, password4, password5]

    scores_sorted = sorted(scores, reverse=True)
    print (scores_sorted)
    lowest_score = scores_sorted[4]


    names_current = "bil"
    passw_current = "ung65#"
    scores_current = "5"

    account_current = f"{names_current}{passw_current}{scores_current}"
    print(account_current)

#Game
def game():
    #Game Settings
    player_speed =  16
    enemy_speed =   10
    bullet_speed =  6
    missile_speed = 20
    bomb_speed =    2

    #Setting Up Window and Sprites values
    WHITE = (255, 255, 255)
    sprite_gap_to_border = 75
    sprite_gap_to_right = 336
    sprite_gap_to_left = 323
    player_size_w = 90
    player_size_h = 144
    enemy_size_w = 72
    enemy_size_h = 56
    bullet_size_w = 20
    bullet_size_h = 53
    missile_size_w = 25
    missile_size_h = 110 
    bomb_size_w = 27
    bomb_size_h = 66

    player_health = 15 +80
    enemy1_health = 1000
    player_bullet_damage = 10
    player_missile_damage = 15
    player_bomb_damage = 35
    enemy1_bullet_damage = 25
    enemy1_missile_damage = 35
    enemy1_bomb_damage = 55

    #Globilisation
    global enemy_time
    global LorR_Enemy
    global LorR_Calc
    global sprite_timer
    global bullet1_shot
    global bullet2_shot
    global missile_shot
    global bomb_shot
    global bullet1
    global bullet2
    global enemy_bullet1_shot
    global enemy_bullet2_shot
    global enemy_missile_shot
    global enemy_bomb_shot
    global enemy_bullet1
    global enemy_bullet2


    enemy_time = random.randint(45, 50) 
    LorR_Enemy = random.choice([1, 100])
    LorR_Calc = random.randint(0, 100)
    sprite_timer = 100

    #ESSENTIAL CODE DO NOT TOUCH
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    bullet1_shot = False
    bullet2_shot = False 
    missile_shot = False
    bomb_shot = False
    enemy_bullet1_shot = False
    enemy_bullet2_shot = False 
    enemy_missile_shot = False
    enemy_bomb_shot = False
    explode_true = False
    deadP = True


    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.RESIZABLE)
    textfont = pygame.font.SysFont("monospace", 50) 
    pygame.display.set_caption("Last Stand")

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Frame1.png")).convert(),
                (player_size_w, player_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - player_size_h/2 - sprite_gap_to_border)

        # Move the sprite based on user keypresses
        def update(self, pressed_keys):

            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Frame1.png")).convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            
            elif sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Frame2.png")).convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            
            elif sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Frame3.png")).convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            
            elif sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Frame4.png")).convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)

            elif sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Frame5.png")).convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)

            if pressed_keys[K_w]:
                self.rect.move_ip(0, -player_speed)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, player_speed)
            if pressed_keys[K_a]:
                self.rect.move_ip(-player_speed, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(player_speed, 0)
            
            # Keep player on the screen
            if self.rect.left < sprite_gap_to_left:
                self.rect.left = sprite_gap_to_left
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= SCREEN_HEIGHT - player_size_h*1.5 - sprite_gap_to_border*2:
                self.rect.top = SCREEN_HEIGHT - player_size_h*1.5 - sprite_gap_to_border*2
            if self.rect.bottom >= SCREEN_HEIGHT-5:
                self.rect.bottom = SCREEN_HEIGHT-5

    class Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bullet", "Frame1.png")).convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)   

        def update(self):
            
            global sprite_timer, bullet1_shot, bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bullet", "Frame1.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            elif sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bullet", "Frame2.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            elif sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bullet", "Frame3.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            elif sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bullet", "Frame4.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            elif sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bullet", "Frame5.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if bullet1_shot == True:
                bullet1.rect.move_ip(0, -bullet_speed)
            if bullet1_shot == False:
                bullet1.rect.x = (player.rect.x+33)
                bullet1.rect.y = (player.rect.y)
                bullet1.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                bullet1.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if bullet1.rect.bottom <= 0:
                bullet1_shot = False

            if bullet2_shot == True:
                bullet2.rect.move_ip(0, -bullet_speed)
            if bullet2_shot == False:
                bullet2.rect.x = (player.rect.x+33)
                bullet2.rect.y = (player.rect.y)
                bullet2.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                bullet2.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if bullet2.rect.bottom <= 0:
                bullet2_shot = False
    class Missile(pygame.sprite.Sprite):

        def __init__(self):
            super(Missile, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Missiles", "Frame1.png")).convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + missile_size_h/2)   

        def update(self):
            
            global sprite_timer, missile_shot

            if missile_shot == True:
                missile1.rect.move_ip(0, -missile_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Missiles", "Frame1.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Missiles", "Frame2.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Missiles", "Frame3.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Missiles", "Frame4.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Missiles", "Frame5.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if missile_shot == False:
                missile1.rect.x = (player.rect.x + 30)
                missile1.rect.y = (player.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if missile1.rect.bottom <= 0:
                missile_shot = False
    class Bomb(pygame.sprite.Sprite):

        def __init__(self):
            super(Bomb, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bombs", "Frame1.png")).convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, bomb_shot

            if bomb_shot == True:
                bomb1.rect.move_ip(0, -bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bombs", "Frame1.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bombs", "Frame1.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bombs", "Frame3.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bombs", "Frame4.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "Bombs", "Frame5.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if bomb_shot == False:
                bomb1.rect.x = (player.rect.x + 32)
                bomb1.rect.top = (player.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if bomb1.rect.bottom <= 0:
                bomb_shot = False

    class Enemy(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Level 1", "1", "Frame1.png")).convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h/2 + sprite_gap_to_border)

        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Level 1", "1", "Frame1.png")).convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            elif sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Level 1", "1", "Frame2.png")).convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            elif sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Level 1", "1", "Frame3.png")).convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            elif sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Level 1", "1", "Frame4.png")).convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)

            

            #Enemy Movement
            if enemy_time > 0:
                enemy_time -= 1

                #timer runs out
                if LorR_Enemy >= LorR_Calc:  
                    self.rect.move_ip(-enemy_speed, 0)   #left
                elif LorR_Enemy < LorR_Calc: 
                    self.rect.move_ip(enemy_speed, 0)   #right

            else:
                #Reset
                enemy_time = random.randint(25, 30)
                LorR_Enemy = (enemy1.rect.x - 241.5) / 1437 * 100
                
                #1920 - 483 = 1437

                LorR_Calc = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < sprite_gap_to_left:
                self.rect.left = sprite_gap_to_left
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class Enemy_Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy1.rect.x+25)
            self.rect.y = (enemy1.rect.y)

        def update(self):
            
            global sprite_timer, enemy_bullet1_shot, enemy_bullet2_shot
            
            if enemy_bullet1.rect.top >= SCREEN_HEIGHT:
                enemy_bullet1_shot = False
                enemy_bullet1.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                enemy_bullet1.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy_bullet2.rect.top >= SCREEN_HEIGHT:
                enemy_bullet2_shot = False
                enemy_bullet2.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                enemy_bullet2.surf.set_colorkey((0, 255, 255), RLEACCEL)

            if enemy_bullet1_shot == True:
                enemy_bullet1.rect.move_ip(0, +bullet_speed)
                if sprite_timer == 100:
                    enemy_bullet1.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame1.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet1.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 80:
                    enemy_bullet1.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame2.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet1.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 60:
                    enemy_bullet1.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame3.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet1.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 40:
                    enemy_bullet1.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame4.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet1.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 20:
                    enemy_bullet1.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame5.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet1.surf.set_colorkey((255, 255, 255), RLEACCEL)
            if enemy_bullet2_shot == True:
                enemy_bullet2.rect.move_ip(0, +bullet_speed)
                if sprite_timer == 100:
                    enemy_bullet2.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame1.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet2.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 80:
                    enemy_bullet2.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame2.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet2.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 60:
                    enemy_bullet2.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame3.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet2.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 40:
                    enemy_bullet2.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame4.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet2.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 20:
                    enemy_bullet2.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bullet", "Frame5.png")).convert(),
                        (bullet_size_w, bullet_size_h))
                    enemy_bullet2.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_bullet1_shot == False:
                enemy_bullet1.rect.x = (enemy1.rect.x+25)
                enemy_bullet1.rect.y = (enemy1.rect.y)   
                enemy_bullet1.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                enemy_bullet1.surf.set_colorkey((0, 255, 255), RLEACCEL)      
            if enemy_bullet2_shot == False:
                enemy_bullet2.rect.x = (enemy1.rect.x+25)
                enemy_bullet2.rect.y = (enemy1.rect.y)  
                enemy_bullet2.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (bullet_size_w, bullet_size_h))
                enemy_bullet2.surf.set_colorkey((0, 255, 255), RLEACCEL)           
    class Enemy_Missile(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Missile, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy1.rect.x + 24)
            self.rect.bottom = (enemy1.rect.top)     

        def update(self):
            
            global sprite_timer, enemy_missile_shot

            if enemy_missile_shot == True:
                enemy_missile1.rect.move_ip(0, +missile_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Missiles", "Frame1.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Missiles", "Frame2.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Missiles", "Frame3.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Missiles", "Frame4.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Missiles", "Frame5.png")).convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_missile_shot == False:
                enemy_missile1.rect.x = (enemy1.rect.x + 24)
                enemy_missile1.rect.bottom = (enemy1.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
                
            if enemy_missile1.rect.top >= SCREEN_HEIGHT:
                enemy_missile_shot = False
    class Enemy_Bomb(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bomb, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy1.rect.x + 24)
            self.rect.top = (enemy1.rect.bottom)

        def update(self):
            
            global sprite_timer, enemy_bomb_shot

            if enemy_bomb_shot == True:
                enemy_bomb1.rect.move_ip(0, +bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bombs", "Frame1.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bombs", "Frame2.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bombs", "Frame3.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bombs", "Frame4.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                elif sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons", "Bombs", "Frame5.png")).convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_bomb_shot == False:
                enemy_bomb1.rect.x = (enemy1.rect.x + 24)
                enemy_bomb1.rect.top = (enemy1.rect.bottom)

                self.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Enemies", "Weapons","SetAs'00FFFF'.png")).convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy_bomb1.rect.top >= SCREEN_HEIGHT:
                enemy_bomb_shot = False

    class Explode(pygame.sprite.Sprite):

        def __init__(self):
            super(Explode, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH, SCREEN_HEIGHT)   

        def update(self):
            
            global sprite_timer, explode_true

            explode_sleep = 0.05

            bullet1.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            bullet1.surf.set_colorkey((0, 255, 255), RLEACCEL)
            bullet2.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            bullet2.surf.set_colorkey((0, 255, 255), RLEACCEL)
            missile1.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            missile1.surf.set_colorkey((0, 255, 255), RLEACCEL)
            bomb1.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            bomb1.surf.set_colorkey((0, 255, 255), RLEACCEL)

            enemy_bullet1.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            enemy_bullet1.surf.set_colorkey((0, 255, 255), RLEACCEL)
            enemy_bullet2.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            enemy_bullet2.surf.set_colorkey((0, 255, 255), RLEACCEL)
            enemy_missile1.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            enemy_missile1.surf.set_colorkey((0, 255, 255), RLEACCEL)
            enemy_bomb1.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (150, 150))
            enemy_bomb1.surf.set_colorkey((0, 255, 255), RLEACCEL)




            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-1.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-2.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-3.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-4.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-5.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-6.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-7.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-8.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-9.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-10.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-11.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-12.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-13.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-14.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            if deadP == True:
                player.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (150, 150))
                player.surf.set_colorkey((0, 255, 255), RLEACCEL)
            elif deadP == False:
                enemy1.surf = pygame.transform.scale(
                    pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                    (150, 150))
                enemy1.surf.set_colorkey((0, 255, 255), RLEACCEL)

            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-15.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-16.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-17.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-18.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-19.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-20.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-21.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-22.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-23.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Explosion", "Explosion-24.png.png")).convert(),
                (150, 150))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
    class Game_over(pygame.sprite.Sprite):

        def __init__(self):
            super(Game_over, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Player", "Weapons", "SetAs'00FFFF'.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (640, 360)   

        def update(self):
            
            print("testing")

            explode_sleep = 0.05
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over--1.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(1.2)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-0.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(0.14)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over--1.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(0.7)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-0.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(1.2)
            

            print("testing2")

            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-1.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-2.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-3.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-4.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-5.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-6.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-7.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-8.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-9.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-10.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-11.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-12.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-13.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-14.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-15.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-16.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-17.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-18.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-19.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-20.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            time.sleep(explode_sleep)
            self.surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Game over", "game_over-21.png.png")).convert(),
                (1280, 720))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()

            print("testing3")
            pygame.quit()
            sys.exit()    

    explode1 = Explode()
    game_over = Game_over()

    # Instantiate sprites
    player = Player()

    bullet1 = Bullet()
    bullet2 = Bullet()
    missile1 = Missile()
    bomb1 = Bomb()

    enemy1 = Enemy()

    enemy_bullet1 = Enemy_Bullet()
    enemy_bullet2 = Enemy_Bullet()
    enemy_missile1 = Enemy_Missile()
    enemy_bomb1 = Enemy_Bomb()


    #Groups
    players = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    missiles = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    enemy_missiles = pygame.sprite.Group()
    enemy_bombs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    players.add(player
                )
    enemies.add(enemy1,
                )
    bullets.add(bullet1,
                bullet2
                )
    missiles.add(missile1
                 )
    bombs.add(bomb1
              )
    enemy_bullets.add(enemy_bullet1,
                enemy_bullet2
                )
    enemy_missiles.add(enemy_missile1
                 )
    enemy_bombs.add(enemy_bomb1
              )
    all_sprites.add(bullet1,
                    bullet2,
                    missile1,
                    bomb1, 
                    enemy_bullet1,
                    enemy_bullet2,
                    enemy_missile1,
                    enemy_bomb1,
                    player, 
                    enemy1,
                    explode1,
                    game_over
                    )
    
    bullet_delay_time = 0
    bullet_delay_base = 20
    missile_delay_time = 0
    missile_delay_base = 75
    bomb_delay_time = 0
    bomb_delay_base = 75

    enemy_bullet_delay_time = 0
    enemy_bullet_delay_base = 20
    enemy_missile_delay_time = 0
    enemy_missile_delay_base = 75
    enemy_bomb_delay_time = 0
    enemy_bomb_delay_base = 75

    def bullets_updating():
        bullet1.update()
        bullet2.update()

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        Thread1 = threading.Thread(player.update(pressed_keys))
        Thread2 = threading.Thread(enemy1.update())
        Thread3 = threading.Thread(target = bullets_updating)
        Thread5 = threading.Thread(missile1.update())
        Thread6 = threading.Thread(bomb1.update())
        Thread7 = threading.Thread(enemy_bullet1.update())
        Thread8 = threading.Thread(enemy_bullet2.update())
        Thread9 = threading.Thread(enemy_missile1.update())
        Thread10 = threading.Thread(enemy_bomb1.update())

        Thread1.start()
        Thread2.start()
        Thread3.start()
        Thread5.start()
        Thread6.start()
        Thread7.start()
        Thread8.start()
        Thread9.start()
        Thread10.start()

        
        if sprite_timer == 0:
            sprite_timer = 100 
        else:
            sprite_timer -= 5

        #Kills player bullets
        if pygame.sprite.spritecollideany(bullet1, enemies):
            bullet1_shot = False
            enemy1_health -= player_bullet_damage
        if pygame.sprite.spritecollideany(bullet2, enemies):
            bullet2_shot = False
            enemy1_health -= player_bullet_damage
        if pygame.sprite.spritecollideany(missile1, enemies):
            missile_shot = False
            enemy1_health -= player_missile_damage
        if pygame.sprite.spritecollideany(bomb1, enemies):
            bomb_shot = False
            enemy1_health -= player_bomb_damage
        #Kills enemy bullets
        if pygame.sprite.spritecollideany(enemy_bullet1, players):
            enemy_bullet1_shot = False
            player_health -= enemy1_bullet_damage
        if pygame.sprite.spritecollideany(enemy_bullet2, players):
            enemy_bullet2_shot = False
            player_health -= enemy1_bullet_damage
        if pygame.sprite.spritecollideany(enemy_missile1, players):
            enemy_missile_shot = False
            player_health -= enemy1_missile_damage
        if pygame.sprite.spritecollideany(enemy_bomb1, players):
            enemy_bomb_shot = False
            player_health -= enemy1_bomb_damage
    
        #Kills player
        if player_health <= 0:
            if pygame.sprite.spritecollideany(player, enemy_bullets):
                player.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                explode1.rect.center = player.rect.center
                deadP = True
                explode1.update()
                time.sleep(1.5)
                game_over.update()
                running = False
            if pygame.sprite.spritecollideany(player, enemy_missiles):
                player.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                explode1.rect.center = player.rect.center
                deadP = True
                explode1.update()
                time.sleep(1.5)
                game_over.update()
                running = False
            if pygame.sprite.spritecollideany(player, enemy_bombs):
                player.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                explode1.rect.center = player.rect.center
                deadP = True
                explode1.update()
                time.sleep(1.5)
                game_over.update()
                running = False
        #kills enemy
        if enemy1_health <= 0:
            if pygame.sprite.spritecollideany(enemy1, bullets):
                enemy1.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                explode1.rect.center = enemy1.rect.center
                deadP = False
                explode1.update()
                time.sleep(1.5)
                game_over.update()
                running = False
            if pygame.sprite.spritecollideany(enemy1, missiles):
                enemy1.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                explode1.rect.center = enemy1.rect.center
                deadP = False
                explode1.update()
                time.sleep(1.5)
                game_over.update()
                running = False
            if pygame.sprite.spritecollideany(enemy1, bombs):
                enemy1.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                explode1.rect.center = enemy1.rect.center
                deadP = False
                explode1.update()
                time.sleep(1.5)
                game_over.update()
                running = False

        enemy_bullet_chance = random.randint(1,50)
        enemy_missile_chance = random.randint(1,50)
        enemy_bomb_chance = random.randint(1,50)

        if enemy_bullet_chance == 5:
            if enemy_bullet_delay_time <= 0:
                if enemy_bullet1_shot == False:
                    enemy_bullet1_shot = True
                    enemy_bullet_delay_time = enemy_bullet_delay_base
                elif enemy_bullet1_shot and enemy_bullet2_shot == False:
                    enemy_bullet2_shot = True
                    enemy_bullet_delay_time = enemy_bullet_delay_base

        if enemy_missile_chance == 5:
            if enemy_missile_delay_time <= 0:
                if enemy_missile_shot == False:
                    enemy_missile_shot = True
                    enemy_missile_delay_time = enemy_missile_delay_base

        if enemy_bomb_chance == 5:
            if enemy_bomb_delay_time <= 0:
                if enemy_bomb_shot == False:
                    enemy_bomb_shot = True
                    enemy_bomb_delay_time = enemy_bomb_delay_base
        

        enemy_bullet_delay_time -= 2
        enemy_missile_delay_time -= 2
        enemy_bomb_delay_time -= 2

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            if bullet_delay_time <= 0:
                if bullet1_shot == False:
                    bullet1_shot = True
                    bullet_delay_time = bullet_delay_base
                elif bullet1_shot and bullet2_shot == False:
                    bullet2_shot = True
                    bullet_delay_time = bullet_delay_base
        if pressed_keys[K_m]:
            if missile_delay_time <= 0:
                if missile_shot == False:
                    missile_shot = True
                    missile_delay_time = missile_delay_base
        if pressed_keys[K_b]:
            if bomb_delay_time <= 0:
                if bomb_shot == False:
                    bomb_shot = True
                    bomb_delay_time = bomb_delay_base
        
        bullet_delay_time -= 2
        missile_delay_time -= 2
        bomb_delay_time -= 2

        Health_Player = textfont.render(f" {player_health}", 1, (255,255,255))
        Health_Enemy = textfont.render(f" {enemy1_health}", 1, (255,255,255))

        Thread1.join()
        Thread2.join()
        Thread3.join()
        Thread5.join()
        Thread6.join()
        Thread7.join()
        Thread8.join()
        Thread9.join()
        Thread10.join()

        #Cirtical Screen Stuff
        screen.blit(background_image, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        screen.blit(Health_Player, (60, 175))
        screen.blit(Health_Enemy, (60, 500))
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()

get_storage_data()
menu(BASE_DIR)
game()