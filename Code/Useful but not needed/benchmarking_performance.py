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
hz = 100
placeholder = "" #can be changed with no effect
stop_music = False
menu_choice = ""
settings_choice = ""
background_image = pygame.image.load('C:/Sprites/Other/Background.png')

#Game
def game():
    #Game Settings
    player_speed =  16
    enemy_speed =   10
    bullet_speed =  6
    missile_speed = 20
    bomb_speed =    2

    #Enemy Intilisation

    #Setting Up Window and Sprites values
    SCREEN_WIDTH = 1543
    SCREEN_HEIGHT = 864
    WHITE = (255, 255, 255)
    NOTWHITE = (255, 0, 255)
    sprite_gap_to_border = 75
    player_size_w = 90
    player_size_h = 144
    enemy_size_w1 = 72
    enemy_size_h1 = 56
    enemy_size_w2 = 72
    enemy_size_h2 = 56
    enemy_size_w3 = 72
    enemy_size_h3 = 56
    bullet_size_w = 24
    bullet_size_h = 63
    missile_size_w = 30
    missile_size_h = 132
    bomb_size_w = 54
    bomb_size_h = 132

    #Globilisation
    global enemy_time1
    global LorR_Enemy1
    global LorR_Calc1
    global enemy_time2
    global LorR_Enemy2
    global LorR_Calc2
    global enemy_time3
    global LorR_Enemy3
    global LorR_Calc3
    global sprite_timer
    global bullet1_shot
    global bullet2_shot
    global missile_shot
    global bomb_shot
    global bullet1
    global bullet2
    global enemy1_bullet1_shot
    global enemy1_bullet2_shot
    global enemy1_missile_shot
    global enemy1_bomb_shot
    global enemy1_bullet1
    global enemy1_bullet2
    global enemy2_bullet1_shot
    global enemy2_bullet2_shot
    global enemy2_missile_shot
    global enemy2_bomb_shot
    global enemy2_bullet1
    global enemy2_bullet2
    global enemy3_bullet1_shot
    global enemy3_bullet2_shot
    global enemy3_missile_shot
    global enemy3_bomb_shot
    global enemy3_bullet1
    global enemy3_bullet2


    enemy_time1 = random.randint(45, 50) 
    LorR_Enemy1 = random.choice([1, 100])
    LorR_Calc1 = random.randint(0, 100)
    enemy_time2 = random.randint(45, 50) 
    LorR_Enemy2 = random.choice([1, 100])
    LorR_Calc2 = random.randint(0, 100)
    enemy_time3 = random.randint(45, 50) 
    LorR_Enemy3 = random.choice([1, 100])
    LorR_Calc3 = random.randint(0, 100)
    sprite_timer = 100

    #ESSENTIAL CODE DO NOT TOUCH
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()
    running = True
    bullet1_shot = False
    bullet2_shot = False 
    missile_shot = False
    bomb_shot = False
    enemy1_bullet1_shot = False
    enemy1_bullet2_shot = False 
    enemy1_missile_shot = False
    enemy1_bomb_shot = False
    enemy2_bullet1_shot = False
    enemy2_bullet2_shot = False 
    enemy2_missile_shot = False
    enemy2_bomb_shot = False
    enemy3_bullet1_shot = False
    enemy3_bullet2_shot = False 
    enemy3_missile_shot = False
    enemy3_bomb_shot = False

    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF)
    clock = pygame.time.Clock() 
    pygame.display.set_caption("5323")
    # Setup
    

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Frame1.png").convert(),
                (player_size_w, player_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - player_size_h/2 - sprite_gap_to_border)

        # Move the sprite based on user keypresses
        def update(self, pressed_keys):

            global sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Frame1.png").convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            
            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Frame2.png").convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            
            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Frame3.png").convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            
            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Frame4.png").convert(),
                    (player_size_w, player_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Frame5.png").convert(),
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

            
            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH-25:
                self.rect.right = SCREEN_WIDTH-25

            if self.rect.top <= SCREEN_HEIGHT - player_size_h*2 - sprite_gap_to_border*2:
                self.rect.top = SCREEN_HEIGHT - player_size_h*2 - sprite_gap_to_border*2
            if self.rect.bottom >= SCREEN_HEIGHT-75:
                self.rect.bottom = SCREEN_HEIGHT-75

    class Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)   

        def update(self):
            
            global sprite_timer, bullet1_shot, bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/Bullet/Frame5.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if bullet1_shot == True:
                bullet1.rect.move_ip(0, -bullet_speed)
            if bullet1_shot == False:
                bullet1.rect.x = (player.rect.x+33)
                bullet1.rect.y = (player.rect.y)
            if bullet1.rect.top <= 0:
                bullet1_shot = False

            if bullet2_shot == True:
                bullet2.rect.move_ip(0, -bullet_speed)
            if bullet2_shot == False:
                bullet2.rect.x = (player.rect.x+33)
                bullet2.rect.y = (player.rect.y)
            if bullet2.rect.top <= 0:
                bullet2_shot = False

    class Missile(pygame.sprite.Sprite):

        def __init__(self):
            super(Missile, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
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
                        pygame.image.load("C:/Sprites/Player/Weapons/Missiles/Frame1.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Missiles/Frame2.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Missiles/Frame3.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Missiles/Frame4.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Missiles/Frame5.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if missile_shot == False:
                missile1.rect.x = (player.rect.x + 30)
                missile1.rect.bottom = (player.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if missile1.rect.top <= 0:
                missile_shot = False

    class Bomb(pygame.sprite.Sprite):

        def __init__(self):
            super(Bomb, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
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
                        pygame.image.load("C:/Sprites/Player/Weapons/Bombs/Frame1.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Bombs/Frame2.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Bombs/Frame3.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Bombs/Frame4.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Player/Weapons/Bombs/Frame5.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if bomb_shot == False:
                bomb1.rect.x = (player.rect.x + 17)
                bomb1.rect.bottom = (player.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if bomb1.rect.top <= 0:
                bomb_shot = False  



    class Enemy1(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w1, enemy_size_h1))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h1/2 + sprite_gap_to_border)

        def update(self):
            
            global enemy_time1, LorR_Enemy1, LorR_Calc1, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w1, enemy_size_h1))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w1, enemy_size_h1))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w1, enemy_size_h1))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
                    (enemy_size_w1, enemy_size_h1))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)

            #Enemy Movement
            if enemy_time1 > 0:
                enemy_time1 -= 1

                #timer runs out
                if LorR_Enemy1 >= LorR_Calc1:  
                    self.rect.move_ip(-enemy_speed, 0)   #left
                elif LorR_Enemy1 < LorR_Calc1: 
                    self.rect.move_ip(enemy_speed, 0)   #right

            else:
                #Reset
                enemy_time1 = random.randint(45, 50)
                LorR_Enemy1 = enemy1.rect.x / 1543 * 100
                LorR_Calc1 = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class Enemy_Bullet1(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bullet1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy1.rect.x+23)
            self.rect.y = (enemy1.rect.y)

        def update(self):
            
            global sprite_timer, enemy1_bullet1_shot, enemy1_bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame5.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy1_bullet1_shot == True:
                enemy1_bullet1.rect.move_ip(0, +bullet_speed)
            if enemy1_bullet1_shot == False:
                enemy1_bullet1.rect.x = (enemy1.rect.x+23)
                enemy1_bullet1.rect.y = (enemy1.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy1_bullet1.rect.bottom >= SCREEN_HEIGHT:
                enemy1_bullet1_shot = False

            if enemy1_bullet2_shot == True:
                enemy1_bullet2.rect.move_ip(0, +bullet_speed)
            if enemy1_bullet2_shot == False:
                enemy1_bullet2.rect.x = (enemy1.rect.x+23)
                enemy1_bullet2.rect.y = (enemy1.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy1_bullet2.rect.bottom >= SCREEN_HEIGHT:
                enemy1_bullet2_shot = False

    class Enemy_Missile1(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Missile1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  + enemy_size_h1/2, enemy1.rect.y + missile_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy1_missile_shot

            if enemy1_missile_shot == True:
                enemy1_missile1.rect.move_ip(0, +missile_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame2.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame3.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame4.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame5.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy1_missile_shot == False:
                enemy1_missile1.rect.x = (enemy1.rect.x + 30)
                enemy1_missile1.rect.bottom = (enemy1.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
                
            if enemy1_missile1.rect.top >= SCREEN_HEIGHT:
                enemy1_missile_shot = False

    class Enemy_Bomb1(pygame.sprite.Sprite):
        
        def __init__(self):
            super(Enemy_Bomb1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  - enemy_size_h1/2, enemy1.rect.y - bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy1_bomb_shot

            if enemy1_bomb_shot == True:
                enemy1_bomb1.rect.move_ip(0, +bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy1_bomb_shot == False:
                enemy1_bomb1.rect.x = (enemy1.rect.x + 17)
                enemy1_bomb1.rect.bottom = (enemy1.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy1_bomb1.rect.bottom >= SCREEN_HEIGHT:
                enemy1_bomb_shot = False
    


    class Enemy2(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy2, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Enemies/Level 1/2/Frame1.png").convert(),
                (enemy_size_w2, enemy_size_h2))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h2/2 + sprite_gap_to_border*2)

        def update(self):
            
            global enemy_time2, LorR_Enemy2, LorR_Calc2, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/2/Frame1.png").convert(),
                    (enemy_size_w2, enemy_size_h2))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/2/Frame2.png").convert(),
                    (enemy_size_w2, enemy_size_h2))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/2/Frame3.png").convert(),
                    (enemy_size_w2, enemy_size_h2))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/2/Frame4.png").convert(),
                    (enemy_size_w2, enemy_size_h2))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)

            #Enemy Movement
            if enemy_time2 > 0:
                enemy_time2 -= 1

                #timer runs out
                if LorR_Enemy2 >= LorR_Calc2:  
                    self.rect.move_ip(-enemy_speed, 0)   #left
                elif LorR_Enemy2 < LorR_Calc2: 
                    self.rect.move_ip(enemy_speed, 0)   #right

            else:
                #Reset
                enemy_time2 = random.randint(45, 50)
                LorR_Enemy2 = enemy2.rect.x / 1543 * 100
                LorR_Calc2 = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class Enemy_Bullet2(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bullet2, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bullet_size_w, bullet_size_w))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy2.rect.x+23)
            self.rect.y = (enemy2.rect.y)

        def update(self):
            
            global sprite_timer, enemy2_bullet1_shot, enemy2_bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_w))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_w))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_w))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_w))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame5.png").convert(),
                    (bullet_size_w, bullet_size_w))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy2_bullet1_shot == True:
                enemy2_bullet1.rect.move_ip(0, +bullet_speed)
            if enemy2_bullet1_shot == False:
                enemy2_bullet1.rect.x = (enemy2.rect.x+23)
                enemy2_bullet1.rect.y = (enemy2.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy2_bullet1.rect.bottom >= SCREEN_HEIGHT:
                enemy2_bullet1_shot = False

            if enemy2_bullet2_shot == True:
                enemy2_bullet2.rect.move_ip(0, +bullet_speed)
            if enemy2_bullet2_shot == False:
                enemy2_bullet2.rect.x = (enemy2.rect.x+23)
                enemy2_bullet2.rect.y = (enemy2.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy2_bullet2.rect.bottom >= SCREEN_HEIGHT:
                enemy2_bullet2_shot = False

    class Enemy_Missile2(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Missile2, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy2.rect.x  + enemy_size_h2/2, enemy2.rect.y + missile_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy2_missile_shot

            if enemy2_missile_shot == True:
                enemy2_missile1.rect.move_ip(0, +missile_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame2.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame3.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame4.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame5.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy2_missile_shot == False:
                enemy2_missile1.rect.x = (enemy2.rect.x + 30)
                enemy2_missile1.rect.bottom = (enemy2.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
                
            if enemy2_missile1.rect.top >= SCREEN_HEIGHT:
                enemy2_missile_shot = False

    class Enemy_Bomb2(pygame.sprite.Sprite):
        
        def __init__(self):
            super(Enemy_Bomb2, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy2.rect.x  - enemy_size_h2/2, enemy2.rect.y - bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy2_bomb_shot

            if enemy2_bomb_shot == True:
                enemy2_bomb1.rect.move_ip(0, +bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy2_bomb_shot == False:
                enemy2_bomb1.rect.x = (enemy2.rect.x + 17)
                enemy2_bomb1.rect.bottom = (enemy2.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy2_bomb1.rect.bottom >= SCREEN_HEIGHT:
                enemy2_bomb_shot = False



    class Enemy3(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy3, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w3, enemy_size_h3))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h3/2 + sprite_gap_to_border*3)

        def update(self):
            
            global enemy_time3, LorR_Enemy3, LorR_Calc3, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w3, enemy_size_h3))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w3, enemy_size_h3))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w3, enemy_size_h3))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
                    (enemy_size_w3, enemy_size_h3))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)

            #Enemy Movement
            if enemy_time3 > 0:
                enemy_time3 -= 1

                #timer runs out
                if LorR_Enemy3 >= LorR_Calc3:  
                    self.rect.move_ip(-enemy_speed, 0)   #left
                elif LorR_Enemy3 < LorR_Calc3: 
                    self.rect.move_ip(enemy_speed, 0)   #right

            else:
                #Reset
                enemy_time3 = random.randint(45, 50)
                LorR_Enemy3 = enemy3.rect.x / 1543 * 100
                LorR_Calc3 = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class Enemy_Bullet3(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bullet3, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy3.rect.x+23)
            self.rect.y = (enemy3.rect.y)

        def update(self):
            
            global sprite_timer, enemy3_bullet1_shot, enemy3_bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame5.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy3_bullet1_shot == True:
                enemy3_bullet1.rect.move_ip(0, +bullet_speed)
            if enemy3_bullet1_shot == False:
                enemy3_bullet1.rect.x = (enemy3.rect.x+23)
                enemy3_bullet1.rect.y = (enemy3.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy3_bullet1.rect.bottom >= SCREEN_HEIGHT:
                enemy3_bullet1_shot = False

            if enemy3_bullet2_shot == True:
                enemy3_bullet2.rect.move_ip(0, +bullet_speed)
            if enemy3_bullet2_shot == False:
                enemy3_bullet2.rect.x = (enemy3.rect.x+23)
                enemy3_bullet2.rect.y = (enemy3.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy3_bullet2.rect.bottom >= SCREEN_HEIGHT:
                enemy3_bullet2_shot = False

    class Enemy_Missile3(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Missile3, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (missile_size_w, missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy3.rect.x  + bullet_size_h/2, enemy3.rect.y + missile_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy3_missile_shot

            if enemy3_missile_shot == True:
                enemy3_missile1.rect.move_ip(0, +missile_speed)

                if sprite_timer == 300:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame2.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame3.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame4.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame5.png").convert(),
                        (missile_size_w, missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy3_missile_shot == False:
                enemy3_missile1.rect.x = (enemy3.rect.x + 30)
                enemy3_missile1.rect.bottom = (enemy3.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
                
            if enemy3_missile1.rect.top >= SCREEN_HEIGHT:
                enemy3_missile_shot = False

    class Enemy_Bomb3(pygame.sprite.Sprite):
        
        def __init__(self):
            super(Enemy_Bomb3, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (bomb_size_w, bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy3.rect.x  - bullet_size_h/2, enemy3.rect.y - bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy3_bomb_shot

            if enemy3_bomb_shot == True:
                enemy3_bomb1.rect.move_ip(0, +bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                        (bomb_size_w, bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy3_bomb_shot == False:
                enemy3_bomb1.rect.x = (enemy3.rect.x + 17)
                enemy3_bomb1.rect.bottom = (enemy3.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (missile_size_w, missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy3_bomb1.rect.bottom >= SCREEN_HEIGHT:
                enemy3_bomb_shot = False



    # Instantiate sprites
    player =   Player()
    bullet1 =  Bullet()
    bullet2 =  Bullet()
    missile1 = Missile()
    bomb1 =    Bomb()

    enemy1 = Enemy1()
    enemy1_bullet1 =  Enemy_Bullet1()
    enemy1_bullet2 =  Enemy_Bullet1()
    enemy1_missile1 = Enemy_Missile1()
    enemy1_bomb1 =    Enemy_Bomb1()

    enemy2 =          Enemy2()
    enemy2_bullet1 =  Enemy_Bullet2()
    enemy2_bullet2 =  Enemy_Bullet2()
    enemy2_missile1 = Enemy_Missile2()
    enemy2_bomb1 =    Enemy_Bomb2()

    enemy3 =         Enemy3()
    enemy3_bullet1 =  Enemy_Bullet3()
    enemy3_bullet2 =  Enemy_Bullet3()
    enemy3_missile1 = Enemy_Missile3()
    enemy3_bomb1 =    Enemy_Bomb3()

    #Groups
    players =         pygame.sprite.Group()
    enemies =         pygame.sprite.Group()
    bullets =         pygame.sprite.Group()
    missiles =        pygame.sprite.Group()
    bombs =           pygame.sprite.Group()
    enemy1_bullets =  pygame.sprite.Group()
    enemy1_missiles = pygame.sprite.Group()
    enemy1_bombs =    pygame.sprite.Group()
    enemy2_bullets =  pygame.sprite.Group()
    enemy2_missiles = pygame.sprite.Group()
    enemy2_bombs =    pygame.sprite.Group()
    enemy3_bullets =  pygame.sprite.Group()
    enemy3_missiles = pygame.sprite.Group()
    enemy3_bombs =    pygame.sprite.Group()
    all_sprites =     pygame.sprite.Group()

    players.add(player)
    
    bullets.add(bullet1,
                bullet2)
    missiles.add(missile1)
    bombs.add(bomb1)
    

    enemies.add(enemy1,
                enemy2,
                enemy3)
    
    enemy1_bullets.add (enemy1_bullet1,
                        enemy1_bullet2)
    enemy2_bullets.add (enemy1_bullet1,
                        enemy1_bullet2)
    enemy3_bullets.add (enemy1_bullet1,
                        enemy1_bullet2)
    
    enemy1_missiles.add(enemy1_missile1)
    enemy2_missiles.add(enemy2_missile1)
    enemy3_missiles.add(enemy3_missile1)

    enemy1_bombs.add(enemy1_bomb1)
    enemy2_bombs.add(enemy2_bomb1)
    enemy3_bombs.add(enemy3_bomb1)
    

    all_sprites.add(bullet1,
                    bullet2,
                    missile1,
                    bomb1, 
                    enemy1_bullet1,
                    enemy1_bullet2,
                    enemy1_missile1,
                    enemy1_bomb1,
                    enemy2_bullet1,
                    enemy2_bullet2,
                    enemy2_missile1,
                    enemy2_bomb1,
                    enemy3_bullet1,
                    enemy3_bullet2,
                    enemy3_missile1,
                    enemy3_bomb1,
                    player, 
                    enemy1)
    
    bullet_delay_time = 0
    bullet_delay_base = 20

    missile_delay_time = 0
    missile_delay_base = 75

    bomb_delay_time = 0
    bomb_delay_base = 75

    enemy1_bullet_delay_time =  0
    enemy1_bullet_delay_base =  20
    enemy1_missile_delay_time = 0
    enemy1_missile_delay_base = 75
    enemy1_bomb_delay_time =    0
    enemy1_bomb_delay_base =    75
    enemy2_bullet_delay_time =  0
    enemy2_bullet_delay_base =  20
    enemy2_missile_delay_time = 0
    enemy2_missile_delay_base = 75
    enemy2_bomb_delay_time =    0
    enemy2_bomb_delay_base =    75
    enemy3_bullet_delay_time =  0
    enemy3_bullet_delay_base =  20
    enemy3_missile_delay_time = 0
    enemy3_missile_delay_base = 75
    enemy3_bomb_delay_time =    0
    enemy3_bomb_delay_base =    75

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        clock.tick(10000)
        screen.fill((0, 0, 0))
        
            
        pygame.display.flip()
        fps = clock.get_fps()
        print(fps)
        

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        bullet1.update()
        bullet2.update()
        missile1.update()
        bomb1.update()

        enemy1.update()
        enemy1_bullet1.update()
        enemy1_bullet2.update()
        enemy1_missile1.update()
        enemy1_bomb1.update()

        enemy2.update()
        enemy2_bullet1.update()
        enemy2_bullet2.update()
        enemy2_missile1.update()
        enemy2_bomb1.update()

        enemy3.update()
        enemy3_bullet1.update()
        enemy3_bullet2.update()
        enemy3_missile1.update()
        enemy3_bomb1.update()
        
        if sprite_timer == 0:
            sprite_timer = 100 
        else:
            sprite_timer -= 5

        if pygame.sprite.spritecollideany(bullet1, enemies):
            bullet1_shot = False
        if pygame.sprite.spritecollideany(bullet2, enemies):
            bullet2_shot = False
        if pygame.sprite.spritecollideany(missile1, enemies):
            missile_shot = False
        if pygame.sprite.spritecollideany(bomb1, enemies):
            bomb_shot = False
        if pygame.sprite.spritecollideany(enemy1_bullet1, enemies):
            bullet1_shot = False
        if pygame.sprite.spritecollideany(enemy1_bullet2, enemies):
            bullet2_shot = False
        if pygame.sprite.spritecollideany(enemy1_missile1, enemies):
            missile_shot = False
        if pygame.sprite.spritecollideany(enemy1_bomb1, enemies):
            bomb_shot = False
        if pygame.sprite.spritecollideany(enemy2_bullet1, enemies):
            bullet1_shot = False
        if pygame.sprite.spritecollideany(enemy2_bullet2, enemies):
            bullet2_shot = False
        if pygame.sprite.spritecollideany(enemy2_missile1, enemies):
            missile_shot = False
        if pygame.sprite.spritecollideany(enemy2_bomb1, enemies):
            bomb_shot = False
        if pygame.sprite.spritecollideany(enemy3_bullet1, enemies):
            bullet1_shot = False
        if pygame.sprite.spritecollideany(enemy3_bullet2, enemies):
            bullet2_shot = False
        if pygame.sprite.spritecollideany(enemy3_missile1, enemies):
            missile_shot = False
        if pygame.sprite.spritecollideany(enemy3_bomb1, enemies):
            bomb_shot = False
        

        if pygame.sprite.spritecollideany(enemy1, bullets):
            #do bullet damage
            enemy1.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False    
        if pygame.sprite.spritecollideany(enemy1, missiles):
            #do missile damage
            enemy1.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy1, bombs):
            #do bomb damage
            enemy1.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy2, bullets):
            #do bullet damage
            enemy2.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy2, missiles):
            #do missile damage
            enemy2.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy2, bombs):
            #do bomb damage
            enemy2.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy3, bullets):
            #do bullet damage
            enemy3.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False   
        if pygame.sprite.spritecollideany(enemy3, missiles):
            #do missile damage
            enemy3.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy3, bombs):
            #do bomb damage
            enemy3.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False     
        if pygame.sprite.spritecollideany(enemy1_bullet1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy1_missile1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy1_bomb1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy2_bullet1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy2_missile1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy2_bomb1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy3_bullet1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy3_missile1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy3_bomb1, players):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        enemy1_bullet_chance = random.randint (1,50)
        enemy1_missile_chance = random.randint(1,50)
        enemy1_bomb_chance = random.randint   (1,50)
        
        enemy2_bullet_chance = random.randint (1,50)
        enemy2_missile_chance = random.randint(1,50)
        enemy2_bomb_chance = random.randint   (1,50)
        
        enemy3_bullet_chance = random.randint (1,50)
        enemy3_missile_chance = random.randint(1,50)
        enemy3_bomb_chance = random.randint   (1,50)

        if enemy1_bullet_chance == 5:
            if enemy1_bullet_delay_time <= 0:
                if enemy1_bullet1_shot == False:
                    enemy1_bullet1_shot = True
                    enemy1_bullet_delay_time = enemy1_bullet_delay_base
                elif enemy1_bullet1_shot and enemy1_bullet2_shot == False:
                    enemy1_bullet2_shot = True
                    enemy1_bullet_delay_time = enemy1_bullet_delay_base
        if enemy1_missile_chance == 5:
            if enemy1_missile_delay_time <= 0:
                if enemy1_missile_shot == False:
                    enemy1_missile_shot = True
                    enemy1_missile_delay_time = enemy1_missile_delay_base
        if enemy1_bomb_chance == 5:
            if enemy1_bomb_delay_time <= 0:
                if enemy1_bomb_shot == False:
                    enemy1_bomb_shot = True
                    enemy1_bomb_delay_time = enemy1_bomb_delay_base       
        if enemy2_bullet_chance == 5:
            if enemy2_bullet_delay_time <= 0:
                if enemy2_bullet1_shot == False:
                    enemy2_bullet1_shot = True
                    enemy2_bullet_delay_time = enemy2_bullet_delay_base
                elif enemy2_bullet1_shot and enemy2_bullet2_shot == False:
                    enemy2_bullet2_shot = True
                    enemy2_bullet_delay_time = enemy2_bullet_delay_base
        if enemy2_missile_chance == 5:
            if enemy2_missile_delay_time <= 0:
                if enemy2_missile_shot == False:
                    enemy2_missile_shot = True
                    enemy2_missile_delay_time = enemy2_missile_delay_base
        if enemy2_bomb_chance == 5:
            if enemy2_bomb_delay_time <= 0:
                if enemy2_bomb_shot == False:
                    enemy2_bomb_shot = True
                    enemy2_bomb_delay_time = enemy2_bomb_delay_base 
        if enemy3_bullet_chance == 5:
            if enemy3_bullet_delay_time <= 0:
                if enemy3_bullet1_shot == False:
                    enemy3_bullet1_shot = True
                    enemy3_bullet_delay_time = enemy3_bullet_delay_base
                elif enemy3_bullet1_shot and enemy3_bullet2_shot == False:
                    enemy3_bullet2_shot = True
                    enemy3_bullet_delay_time = enemy3_bullet_delay_base
        if enemy3_missile_chance == 5:
            if enemy3_missile_delay_time <= 0:
                if enemy3_missile_shot == False:
                    enemy3_missile_shot = True
                    enemy3_missile_delay_time = enemy3_missile_delay_base
        if enemy3_bomb_chance == 5:
            if enemy3_bomb_delay_time <= 0:
                if enemy3_bomb_shot == False:
                    enemy3_bomb_shot = True
                    enemy3_bomb_delay_time = enemy3_bomb_delay_base 

        enemy1_bullet_delay_time -= 2
        enemy1_missile_delay_time -= 2
        enemy1_bomb_delay_time -= 2

        enemy2_bullet_delay_time -= 2
        enemy2_missile_delay_time -= 2
        enemy2_bomb_delay_time -= 2

        enemy3_bullet_delay_time -= 2
        enemy3_missile_delay_time -= 2
        enemy3_bomb_delay_time -= 2

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
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                if bullet_delay_time <= 0:
                    if bullet1_shot == False:
                        bullet1_shot = True
                        bullet_delay_time = bullet_delay_base
                    elif bullet1_shot and bullet2_shot == False:
                        bullet2_shot = True
                        bullet_delay_time = bullet_delay_base
            if event.button == 2:
                if missile_delay_time <= 0:
                    if missile_shot == False:
                        missile_shot = True
                        missile_delay_time = missile_delay_base
            if event.button == 1:
                if bomb_delay_time <= 0:
                    if bomb_shot == False:
                        bomb_shot = True
                        bomb_delay_time = bomb_delay_base
        

        bullet_delay_time -= 2
        missile_delay_time -= 2
        bomb_delay_time -= 2


        #Cirtical Screen Stuff
        screen.blit(background_image, (0, 0))
        for entity in all_sprites:
            pygame.draw.rect(screen, NOTWHITE, enemy2)
            pygame.draw.rect(screen, WHITE, enemy3)
            screen.blit(entity.surf, entity.rect) 
            
        pygame.display.flip()

    pygame.quit()
    sys.exit()

game()