#5323 pre game code

#Importations
import os
import pygame 
import random
import sys
import time
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_SPACE,
    K_m,
    K_b,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#variables
hz = 60
placeholder = "" #can be changed with no effect
stop_music = False
menu_choice = ""
settings_choice = ""

#Title
def start_title():
    print("===============================================================================")
    time.sleep(0.5)
    print("           :::::::::::::    :::::::::::     ::::::::        ::::::::::: ")
    time.sleep(0.5)
    print("          :+:       :+:   :+:       :+:   :+:       :+:   :+:      :+: ")
    time.sleep(0.5)
    print("         +:+                       +:+          +:+               +:+  ")
    time.sleep(0.5)
    print("        +#++:++:++#+        +#++:++:         +#+           +#++:++:    ")
    time.sleep(0.5)
    print("                 +#+              +#+     +#+                    +#+    ")
    time.sleep(0.5)
    print("      #+#       #+#   #+#       #+#    #+#           #+#       #+#     ")
    time.sleep(0.5)
    print("      ###########     ###########    #############   ###########       ")      
    time.sleep(0.5)
    print("===============================================================================")
    time.sleep(1.5)

#Game
def game():
    #Game Settings
    
    #speed normilisation
    if hz == 30:
        player_speed =  28
        enemy_speed =   20
        bullet_speed =  40
        missile_speed = 16
        bomb_speed =    4
        
    if hz == 60:
        player_speed =  14
        enemy_speed =   10
        bullet_speed =  20
        missile_speed = 8
        bomb_speed =    2
    
    if hz == 90:
        player_speed =  10.5
        enemy_speed =   7.5
        bullet_speed =  15
        missile_speed = 6
        bomb_speed =    1.5
    
    if hz == 120:
        player_speed =  7
        enemy_speed =   5
        bullet_speed =  10
        missile_speed = 4
        bomb_speed =    1

    #speed normilisation
    player_speed =  14
    enemy_speed =   10
    bullet_speed =  5
    missile_speed = 35
    bomb_speed =    2

    #Enemy Intilisation

    #Setting Up Window and Sprites values
    SCREEN_WIDTH = 1543
    SCREEN_HEIGHT = 864
    WHITE = (255, 255, 255)
    sprite_gap_to_border = 30
    player_size_w = 70
    player_size_h = 70
    enemy_size_w = 130
    enemy_size_h = 85
    bullet_size_w = 24
    bullet_size_h = 63
    missile_size_w = 30
    missile_size_h = 132
    bomb_size_w = 54
    bomb_size_h = 132

    #Globilisation
    global enemy_time
    global LorR_Enemy
    global LorR_Calc
    global sprite_timer
    global bullet1_shot
    global bullet2_shot
    global bullet3_shot
    global missile_shot
    global bomb_shot
    global e1bullet1_shot
    global e1bullet2_shot
    global e1bullet3_shot
    global e1missile_shot
    global e1bomb_shot

    enemy_time = random.randint(45, 50) 
    LorR_Enemy = random.choice([1, 100])
    LorR_Calc = random.randint(0, 100)
    sprite_timer = 100

    #ESSENTIAL CODE DO NOT TOUCH
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()
    running = True
    bullet1_shot = False
    bullet2_shot = False
    bullet3_shot = False 
    missile_shot = False
    bomb_shot = False
    e1bullet1_shot = False
    e1bullet2_shot = False
    e1bullet3_shot = False 
    e1missile_shot = False
    e1bomb_shot = False

    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN) 
    pygame.display.set_caption("5323")

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            # Create the surface and assign it to the instance variable 'surf'
            self.surf = pygame.Surface((player_size_w, player_size_h))
            self.surf.fill((WHITE))  # This line was also misplaced - should be inside __init__
            # Now get the rect from the properly assigned surf
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - player_size_h/2 - sprite_gap_to_border)

        # Move the sprite based on user keypresses
        def update(self, pressed_keys):
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -player_speed)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, player_speed)
            if pressed_keys[K_a]:
                self.rect.move_ip(-player_speed, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(player_speed, 0)
            
            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= SCREEN_HEIGHT - player_size_h*3 - sprite_gap_to_border*2:
                self.rect.top = SCREEN_HEIGHT - player_size_h*3 - sprite_gap_to_border*2
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            #Joystick Stuff
            if pygame.joystick.get_count() > 0:
                joystick = pygame.joystick.Joystick(0)
                joystick.init()
                
                # Axis 0: Left/Right movement
                left_x = joystick.get_axis(0)
                # Axis 0: Left/Right movement
                up_y = joystick.get_axis(1)

                #Player Movement
                if left_x <= -0.1: 
                    self.rect.move_ip(-player_speed, 0) #Left 
                if left_x >= 0.1:
                    self.rect.move_ip(player_speed, 0) #Right
                if up_y >= 0.1: 
                    self.rect.move_ip(0, player_speed) #Up
                if up_y <= -0.1:
                    self.rect.move_ip(0, -player_speed) #Down



        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h/2 + sprite_gap_to_border)

        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)

            

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
                enemy_time = random.randint(45, 50)
                LorR_Enemy = enemy1.rect.x / 1543 * 100
                LorR_Calc = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bullet/Frame1.png").convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)   

        def update(self):
            
            global sprite_timer, bullet1_shot, bullet2_shot, bullet3_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bullet/Frame5.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if bullet1_shot == True:
                bullet1.rect.move_ip(0, -bullet_speed)
            if bullet1_shot == False:
                bullet1.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)
            if bullet1.rect.top <= 0:
                bullet1_shot = False

            if bullet2_shot == True:
                bullet2.rect.move_ip(0, -bullet_speed)
            if bullet2_shot == False:
                bullet2.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)
            if bullet2.rect.top <= 0:
                bullet2_shot = False

            if bullet3_shot == True:
                bullet3.rect.move_ip(0, -bullet_speed)
            if bullet3_shot == False:
                bullet3.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)
            if bullet3.rect.top <= 0:
                bullet3_shot = False

    class Missile(pygame.sprite.Sprite):

        def __init__(self):
            super(Missile, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Missiles/Frame1.png").convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + missile_size_h/2)   

        def update(self):
            
            global sprite_timer, missile_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Missiles/Frame1.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Missiles/Frame2.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Missiles/Frame3.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Missiles/Frame4.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Missiles/Frame5.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if missile_shot == True:
                missile1.rect.move_ip(0, -missile_speed)
            if missile_shot == False:
                missile1.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + missile_size_h/2)
            if missile1.rect.top <= 0:
                missile_shot = False

    class Bomb(pygame.sprite.Sprite):

        def __init__(self):
            super(Bomb, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bombs/Frame1.png").convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((45, 54, 76), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, bomb_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bombs/Frame1.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/PlayerWeapons/Bombs/Frame2.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bombs/Frame3.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bombs/Frame4.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Player/Weapons/Bombs/Frame5.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if bomb_shot == True:
                bomb1.rect.move_ip(0, -bomb_speed)
            if bomb_shot == False:
                bomb1.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bomb_size_h/2)
            if bomb1.rect.top <= 0:
                bomb_shot = False


    class Enemy(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h/2 + sprite_gap_to_border)

        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 255, 0), RLEACCEL)

            

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
                enemy_time = random.randint(45, 50)
                LorR_Enemy = enemy1.rect.x / 1543 * 100
                LorR_Calc = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class e1Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(e1Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)   

        def update(self):
            
            global sprite_timer, e1bullet1_shot, e1bullet2_shot, e1bullet3_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bullet/Frame5.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if e1bullet1_shot == True:
                e1bullet1.rect.move_ip(0, +bullet_speed)
            if e1bullet1_shot == False:
                e1bullet1.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)
            if e1bullet1.rect.top <= 0:
                e1bullet1_shot = False

            if e1bullet2_shot == True:
                e1bullet2.rect.move_ip(0, +bullet_speed)
            if e1bullet2_shot == False:
                e1bullet2.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)
            if e1bullet2.rect.top <= 0:
                e1bullet2_shot = False

            if e1bullet3_shot == True:
                e1bullet3.rect.move_ip(0, +bullet_speed)
            if e1bullet3_shot == False:
                e1bullet3.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)
            if e1bullet3.rect.top <= 0:
                e1bullet3_shot = False

    class e1Missile(pygame.sprite.Sprite):

        def __init__(self):
            super(e1Missile, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + missile_size_h/2)   

        def update(self):
            
            global sprite_timer, e1missile_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Missiles/Frame2.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Missiles/Frame3.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Missiles/Frame4.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Missiles/Frame5.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if e1missile_shot == True:
                e1missile1.rect.move_ip(0, +missile_speed)
            if e1missile_shot == False:
                e1missile1.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + missile_size_h/2)
            if e1missile1.rect.top <= 0:
                e1missile_shot = False

    class e1Bomb(pygame.sprite.Sprite):

        def __init__(self):
            super(e1Bomb, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((45, 54, 76), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, bomb_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                    (bomb_size_w, bomb_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if e1bomb_shot == True:
                e1bomb1.rect.move_ip(0, +bomb_speed)
            if e1bomb_shot == False:
                e1bomb1.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bomb_size_h/2)
            if e1bomb1.rect.top <= 0:
                e1bomb_shot = False

    # Instantiate sprites
    player = Player()

    enemy1 = Enemy()

    bullet1 = Bullet()
    bullet2 = Bullet()
    bullet3 = Bullet()

    missile1 = Missile()

    bomb1 = Bomb()

    e1bullet1 = e1Bullet()
    e1bullet2 = e1Bullet()
    e1bullet3 = e1Bullet()

    e1missile1 = e1Missile()

    e1bomb1 = e1Bomb()

    #Groups
    players = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    missiles = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    e1bullets = pygame.sprite.Group()
    e1missiles = pygame.sprite.Group()
    e1bombs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    players.add(player
                )
    enemies.add(enemy1,
                )
    bullets.add(bullet1,
                bullet2,
                bullet3
                )
    missiles.add(missile1
                 )
    bombs.add(bomb1
              )
    e1bullets.add(e1bullet1,
                e1bullet2,
                e1bullet3
                )
    e1missiles.add(e1missile1
                 )
    e1bombs.add(e1bomb1
                )
    all_sprites.add(player, 
                    enemy1,
                    bullet1,
                    bullet2,
                    bullet3,
                    missile1,
                    bomb1 
                    )
    
    bullet_delay_time = 0
    bullet_delay_base = 20

    missile_delay_time = 0
    missile_delay_base = 75

    bomb_delay_time = 0
    bomb_delay_base = 75

    e1bullet_delay_time = 0
    e1bullet_delay_base = 20

    e1missile_delay_time = 0
    e1missile_delay_base = 75

    e1bomb_delay_time = 0
    e1bomb_delay_base = 75

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemy1.update()
        bullet1.update()
        bullet2.update()
        bullet3.update()
        missile1.update()
        bomb1.update()
        
        if sprite_timer == 0:
            sprite_timer = 100 
        else:
            sprite_timer -= 5

        if pygame.sprite.spritecollideany(bullet1, enemies):
            bullet1_shot = False
        if pygame.sprite.spritecollideany(bullet2, enemies):
            bullet2_shot = False
        if pygame.sprite.spritecollideany(bullet3, enemies):
            bullet3_shot = False
        if pygame.sprite.spritecollideany(missile1, enemies):
            missile_shot = False
        if pygame.sprite.spritecollideany(bomb1, enemies):
            bomb_shot = False

        if pygame.sprite.spritecollideany(e1bullet1, players):
            e1bullet1_shot = False
        if pygame.sprite.spritecollideany(e1bullet2, players):
            e1bullet2_shot = False
        if pygame.sprite.spritecollideany(e1bullet3, players):
            e1bullet3_shot = False
        if pygame.sprite.spritecollideany(e1missile1, players):
            e1missile_shot = False
        if pygame.sprite.spritecollideany(e1bomb1, players):
            e1bomb_shot = False
        

        if pygame.sprite.spritecollideany(enemy1, bullets):
            enemy1.kill()
            screen.fill("black")
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        
        if pygame.sprite.spritecollideany(enemy1, missiles):
            enemy1.kill()
            screen.fill("black")
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False

        if pygame.sprite.spritecollideany(enemy1, bombs):
            enemy1.kill()
            screen.fill("black")
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False

        if pygame.sprite.spritecollideany(player, e1bullets):
            player.kill()
            screen.fill("black")
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        
        if pygame.sprite.spritecollideany(player, e1missiles):
            player.kill()
            screen.fill("black")
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False

        if pygame.sprite.spritecollideany(player, e1bombs):
            player.kill()
            screen.fill("black")
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE] or event.type == pygame.JOYBUTTONDOWN and event.button == 5:
            if bullet_delay_time <= 0:
                if bullet1_shot == False:
                    bullet1_shot = True
                    bullet_delay_time = bullet_delay_base
                elif bullet1_shot and bullet2_shot == False:
                    bullet2_shot = True
                    bullet_delay_time = bullet_delay_base
                elif bullet1_shot and bullet2_shot and bullet3_shot == False:
                    bullet3_shot = True
                    bullet_delay_time = bullet_delay_base

        if pressed_keys[K_m] or event.type == pygame.JOYBUTTONDOWN and event.button == 2:
            if missile_delay_time <= 0:
                if missile_shot == False:
                    missile_shot = True
                    missile_delay_time = missile_delay_base

        if pressed_keys[K_b] or event.type == pygame.JOYBUTTONDOWN and event.button == 1:
            if bomb_delay_time <= 0:
                if bomb_shot == False:
                    bomb_shot = True
                    bomb_delay_time = bomb_delay_base
        
        bullet_delay_time -= 1
        missile_delay_time -= 1
        bomb_delay_time -= 1

        e1bul = random.randint(1,10)
        e1mis = random.randint(1,10)
        e1bom = random.randint(1,10)
        if e1bul == 5:
            if e1bullet_delay_time <= 0:
                if e1bullet1_shot == False:
                    e1bullet1_shot = True
                    e1bullet_delay_time = bullet_delay_base
                elif e1bullet1_shot and bullet2_shot == False:
                    e1bullet2_shot = True
                    e1bullet_delay_time = bullet_delay_base
                elif e1bullet1_shot and bullet2_shot and bullet3_shot == False:
                    e1bullet3_shot = True
                    e1bullet_delay_time = e1bullet_delay_base

        if e1mis == 5:
            if e1missile_delay_time <= 0:
                if e1missile_shot == False:
                    e1missile_shot = True
                    e1missile_delay_time = e1missile_delay_base

        if e1bom == 5:
            if e1bomb_delay_time <= 0:
                if e1missile_shot == False:
                    e1bomb_shot = True
                    e1bomb_delay_time = e1bomb_delay_base

        e1bullet_delay_time -= 1
        e1missile_delay_time -= 1
        e1bomb_delay_time -= 1

        #Cirtical Screen Stuff
        screen.fill("black")
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()


#Menu
def menu():
    global placeholder
    global stop_music
    global menu_choice
    global settings_choice

    print("")
    print("===================================== Menu ====================================")
    time.sleep(0.5)
    print("Press 1 to Start")
    time.sleep(0.5)
    print("Press 2 to open settings")
    time.sleep(0.5)
    print("Press 3 to open tutorial")
    time.sleep(0.5)
    print("Press 4 to open leaderboard")
    time.sleep(0.5)
    print("Press 5 to open accounts")
    time.sleep(0.5)
    print("Press 6 to open credits")
    time.sleep(0.5)
    print("Press Esc to quit")
    time.sleep(0.5)
    menu_choice = input("Enter choice: ")
    print("===============================================================================")
    print("")
    
    #The Game
    if menu_choice == "1":
        
        print("===============================================================================")
        print("===============================================================================")
        print("enter 'SKIP' to skip the cutscene")
        print("enter anything else to continue")
        placeholder = input("")
        if placeholder != "SKIP":
            time.sleep(0.5)
            print("[You]")
            print("*Where am i?*")
            placeholder = input("")
            time.sleep(0.5)
            print("[You]")
            print("*Who am i?*")
            placeholder = input("")
            time.sleep(0.5)
            print("[Man]")
            print("You are a civilain in the Terran Galactic Empire.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("I am General Nishikado of the Unified Armed Forces of the Sagittarius Arm.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("There has been a brutal war against our people.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("Casualties across the empire are at 34%")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("Casualties across the most effected regions are at 89%")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("The enemy has captured the Perseus Arm of the milky way.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("This leaves only the Sagittarius Arm region to defend us.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("If we fail to hold this point then the Orion Arm will fall and with it, our empire.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("You have been conscripted into the General Defencive Force of the Sagittarius Arm")
            placeholder = input("")
            time.sleep(0.5)        
            print("[General Nishikado]")
            print("This regiment is a level 2 importance meaning only the force more valuable is the Final Defencive Force of the Orion Arm.")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("Your only objective is to inflict as much harm to the enemy forces as possible")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("We have ranked all enemy forces at levels 1-10")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("You Appear to be a level 4.5, with a class selected you can go up to a level 5")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("You can reach up to a level 6.5 with armour")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("You better come back a hero or not at all")
            placeholder = input("")
            time.sleep(0.5)
            print("[General Nishikado]")
            print("Good luck soldier")
            placeholder = input("")
        print("")
        game()


    #Settings
    if menu_choice == "2":
        print("")
        print("=================================== Settings ==================================")
        time.sleep(0.5)
        print("Press 1 to open game Hz")
        time.sleep(0.5)
        print("Press 2 to open audio")
        time.sleep(0.5)
        print("Press 3 to open music")
        time.sleep(0.5)
        print("Press 4 to open difficulty")
        time.sleep(0.5)
        print("Press 5 to open menu")
        time.sleep(0.5)
        print("Press Esc to quit")
        time.sleep(0.5)
        settings_choice = input("Enter choice: ")
        print("===============================================================================")
        print("")

        #Hz
        if settings_choice == "1":
            hz_loop = True
            while hz_loop == True:
                print("-------------------------------------- Hz -------------------------------------")
                print("Lower will put less strain on your computer but may make the game less smooth")
                time.sleep(1)
                print("Higher will make the game more smooth but may put less strain on your computer")
                time.sleep(1)
                print("This will also effct how many ")
                time.sleep(1)
                print("It is recommended to match your in game Hz to your monitors Hz")
                time.sleep(1)
                print("Hz must be 30, 60, 90 or 120")
                time.sleep(1)
                print("Default is 60")
                time.sleep(1)
                hz = int(input("Enter Hz: "))
                if hz is 30 or 60 or 90 or 120:
                    hz_loop = False
                else:
                    hz_loop = True
                print("===============================================================================")
                time.sleep(2)
                menu()

        #Audio
        if settings_choice == "2":
            print("------------------------------------- Audio  -----------------------------------")
            print("This Audio took too long to make so deal with it")
            time.sleep(1)
            placeholder = input("")
            print("===============================================================================")
            print("")
            menu()

        #Music settings
        if settings_choice == "3":
            print("------------------------------------ Music  -----------------------------------")
            print("Press 1 to turn on music")
            time.sleep(1)
            print("Press 2 to turn off music")
            time.sleep(1)
            print("Press Esc to quit")
            time.sleep(1)
            music_choice = int(input("Enter choice: "))
            print("===============================================================================")
            if music_choice == 1:
                stop_music = False
                music()
                menu()
            if music_choice == 2:
                stop_music = True
                menu()

        #Difficulty
        if settings_choice == "4":
            print("---------------------------------- Difficulty ---------------------------------")
            print("Difficulty settings coming soon!")
            time.sleep(1)
            placeholder = input("")
            menu()

        #Menu
        if settings_choice == "5":
            menu()

        #Tutorial
    
    #Tutorial
    if menu_choice == "3":
        print("")
        print("=================================== Tutorial ==================================")
        time.sleep(0.5)
        print("5323 is a single player space shooter game where the goal is to get 5323 points.")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("You move left using the        A key")
        print("You move right using the       D key")
        print("You shoot bullets using the    Space bar")
        print("You shoot missiles using the   M key")
        print("You shoot bombs using the      B key")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Player types and stats:")
        print("colour          bullet         missile         bomb        health       level")
        print("Base            1x bullet      1x missile      1x bomb     15 health    level 4.5")
        print("Rifle           1.3x bullet    1x missile      1x bomb     15 health    level 5")
        print("ICBM            1x bullet      1.2x missile    1x bomb     15 health    level 5")
        print("Bomber          1x bullet      1x missile      1.25x bomb  15 health    level 5")
        print("Tank            1x bullet      1x missile      1x bomb     25 health    level 5")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Armour          1.5x bullet    1.4x missile    1.2x bomb   +80 health   level 6.5")
        print("coin            1, 2, 5, 10, 25, 50, 100, 200, 1000")
        print("dice            [2-5 nothing] [1 player to 1hp] [6 removes 50% of all enemies total hp] ")
        print("hammer          puts health back to 100%")
        print("sands of time   gives player an extra life")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Enemy types and stats:")
        print("colour          bullet         missile         bomb        health       level")
        print("black           0.2x bullet                                1 health     level 1")
        print("orange          0.5x bullet                                3 health     level 2")
        print("yellow          0.75x bullet   0.5x missile                5 health     level 3")
        print("blue            1x bullet      1x missile                  10 health    level 4")
        print("red             1.25x bullet   1.25x missile   1x bomb     25 health    level 5")
        print("purple          1.5x bullet    1.4x missile    1.2x bomb   50 health    level 6")
        print("pink            2x bullet      1.75x missile   1.5x bomb   100 health   level 7")
        print("white           3x bullet      2x missile      1.8x bomb   200 health   level 8")
        print("gold            5x bullet      3x missile      3x bomb     1000 health  level 9")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Bullets, missiles and bombs are the weapons.")
        print("Each weapon has different damage, duration and delay stats.")
        print("These are the default weapon stats:")
        print("weapon     damage         map travel      delay")
        print("bullets    1 damage       3 sec           1s")
        print("missiles   5 damage       1 sec           3s")
        print("bombs      25 damage      10 sec          30s")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Upgrades:")
        print("damage          +1 bullet      +2 missile      +5 bomb")
        print("speed           -7% bullet     -5% missile     -10% bomb")
        print("delay           -5% bullet     -7% missile     -10% bomb")
        print("health          +5 health")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Level ups:")
        print("damage          +2 bullet      +5 missile      +10 bomb")
        print("speed           -15% bullet   -10% missile     -25% bomb")
        print("delay           -10% bullet   -15% missile     -25% bomb")
        print("health          +20 health")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Avoid enemy fire and destroy enemies to gain points.")
        print("Enemies come in waves, with 8 waves per level")
        print("At the start you are the strongest character by a bit")
        print("By the end, you are the weakest character by a LOT")

        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("5323          The games name")
        print("Menu          Main section where all sections branch off from")
        print("Settings      Goes to the settings")
        print("Start         Begins the games selection")
        print("Tutorial      Explains the games premise and functions (hopefully)")
        print("Account       Brings up sign up/in")
        print("Sign up       Allows account creation")
        print("Sign in       Allows account log in")
        print("Leaderboard   Shows leaderboard of users who have the biggest high score")
        print("Customise     Allows a user to change their username/password for an account")
        print("Credits       Says who worked on every part")
        print("Settings      Opens the settings menu")
        print("Hz            Sets the refresh rate of the game")
        print("Sound         Effects can be toggled on and off (coming soon)")
        print("Music         Can be toggled on and off")
        print("Difficulty    Easy, normal, hard and impossible")
        print("Restart       Goes back to the start of the level")
        print("")
        placeholder = input("Menu: ")
        print("===============================================================================")
        print("")
        menu()

    #Leaderboard
    if menu_choice == "4":
        #top players scores
        print("")
        menu()

    #Accounts
    if menu_choice == "5":
        #accoount stuff
        print("")
        menu()

    #Credits
    if menu_choice == "6":
        print("")
        print("=================================== Credits ===================================")
        time.sleep(0.5)
        print("Producer       Luke Simcock")
        time.sleep(0.5)
        print("Directors      Luke Simcock")
        time.sleep(0.5)
        print("Designers      Luke Simcock")
        time.sleep(0.5)
        print("Level          Luke Simcock")
        time.sleep(0.5)
        print("UI             Luke Simcock")
        time.sleep(0.5)
        print("Artists        Luke Simcock")
        time.sleep(0.5)
        print("Concept        Luke Simcock")
        time.sleep(0.5)
        print("3D             Luke Simcock")
        time.sleep(0.5)
        print("Texture        Luke Simcock")
        time.sleep(0.5)
        print("Animation      Luke Simcock")
        time.sleep(0.5)
        print("VFX            Luke Simcock")
        time.sleep(0.5)
        print("Audio          Luke Simcock")
        time.sleep(0.5)
        print("Music          Luke Simcock")
        time.sleep(0.5)
        print("Sound          Luke Simcock")
        time.sleep(0.5)
        print("Composers      Luke Simcock")
        time.sleep(0.5)
        print("Voice Actors   Luke Simcock")
        time.sleep(0.5)
        print("Programmers    Luke Simcock")
        time.sleep(0.5)
        print("Engine         Luke Simcock")
        time.sleep(0.5)
        print("AI             Luke Simcock")
        time.sleep(0.5)
        print("Tools          Luke Simcock")
        time.sleep(0.5)
        print("Licensing      Luke Simcock")
        time.sleep(0.5)
        print("Publishers     Luke Simcock")
        placeholder = input("Continue: ")
        time.sleep(0.5)
        print("===============================================================================")
        print("")
        menu()



#Music
def music():
    #Music on or off
    global stop_music

    #Function to play a random song
    def play_random_song():
        song = random.choice(mp3_files)
        #print(f"Playing: {song}")
        pygame.mixer.music.load(os.path.join(music_folder, song))
        pygame.mixer.music.play()

    #Folder where your MP3s are
    music_folder = r"C:\Users\luke\Music\Majority And Minority"

    #Get a list of all MP3 files in that folder
    mp3_files = [f for f in os.listdir(music_folder) if f.lower().endswith(".mp3")]

    if not mp3_files:
        exit()

    #Initialize mixer
    pygame.mixer.init()

    #First song
    play_random_song()

    #Plays song
    while not stop_music:
        play_random_song()
        while not stop_music:
            time.sleep(0.001)
            if not pygame.mixer.music.get_busy() and not stop_music:
                play_random_song()
    return stop_music


start_title()
menu()