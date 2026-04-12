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
hz = 24
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
    enemy_bullet_speed =  6
    enemy_missile_speed = 20
    enemy_bomb_speed =    2

    #Enemy Intilisation

    #Setting Up Window and Sprites values
    SCREEN_WIDTH = 1543
    SCREEN_HEIGHT = 864
    WHITE = (255, 255, 255)
    sprite_gap_to_border = 75
    player_size_w = 90
    player_size_h = 144
    enemy_size_w = 72
    enemy_size_h = 56
    bullet_size_w = 24
    bullet_size_h = 63
    missile_size_w = 30
    missile_size_h = 132
    bomb_size_w = 54
    bomb_size_h = 132
    enemy_bullet_size_w = 24
    enemy_bullet_size_h = 63
    enemy_missile_size_w = 30
    enemy_missile_size_h = 132
    enemy_bomb_size_w = 54
    enemy_bomb_size_h = 132

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
    pygame.joystick.init()
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

    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN) 
    pygame.display.set_caption("5323")

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Frame1.png").convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - player_size_h/2 - sprite_gap_to_border)

        # Move the sprite based on user keypresses
        def update(self, pressed_keys):

            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

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


    class Enemy(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h/2 + sprite_gap_to_border)

        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
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

    class Enemy_Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_bullet_size_w, enemy_bullet_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy1.rect.x+23)
            self.rect.y = (enemy1.rect.y)

        def update(self):
            
            global sprite_timer, enemy_bullet1_shot, enemy_bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame2.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame3.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame4.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame5.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_bullet1_shot == True:
                enemy_bullet1.rect.move_ip(0, +enemy_bullet_speed)
            if enemy_bullet1_shot == False:
                enemy_bullet1.rect.x = (enemy1.rect.x+23)
                enemy_bullet1.rect.y = (enemy1.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy_bullet1.rect.bottom >= SCREEN_HEIGHT:
                enemy_bullet1_shot = False

            if enemy_bullet2_shot == True:
                enemy_bullet2.rect.move_ip(0, +enemy_bullet_speed)
            if enemy_bullet2_shot == False:
                enemy_bullet2.rect.x = (enemy1.rect.x+23)
                enemy_bullet2.rect.y = (enemy1.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy_bullet2.rect.bottom >= SCREEN_HEIGHT:
                enemy_bullet2_shot = False
    class Enemy_Missile(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Missile, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_missile_size_w, enemy_missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  + enemy_size_h/2, enemy1.rect.y + enemy_missile_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy_missile_shot

            if enemy_missile_shot == True:
                enemy_missile1.rect.move_ip(0, +enemy_missile_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame2.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame3.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame4.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame5.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_missile_shot == False:
                enemy_missile1.rect.x = (enemy1.rect.x + 30)
                enemy_missile1.rect.bottom = (enemy1.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_missile_size_w, enemy_missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
                
            if enemy_missile1.rect.top >= SCREEN_HEIGHT:
                enemy_missile_shot = False
    class Enemy_Bomb(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bomb, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_bomb_size_w, enemy_bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  - enemy_size_h/2, enemy1.rect.y - enemy_bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy_bomb_shot

            if enemy_bomb_shot == True:
                enemy_bomb1.rect.move_ip(0, +enemy_bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_bomb_shot == False:
                enemy_bomb1.rect.x = (enemy1.rect.x + 17)
                enemy_bomb1.rect.bottom = (enemy1.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_missile_size_w, enemy_missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy_bomb1.rect.bottom >= SCREEN_HEIGHT:
                enemy_bomb_shot = False


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
                    enemy1
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
        missile1.update()
        bomb1.update()
        enemy_bullet1.update()
        enemy_bullet2.update()
        enemy_missile1.update()
        enemy_bomb1.update()
        
        if sprite_timer == 0:
            sprite_timer = 100 
        else:
            sprite_timer -= 5

        #Kills player bullets
        if pygame.sprite.spritecollideany(bullet1, enemies):
            bullet1_shot = False
        if pygame.sprite.spritecollideany(bullet2, enemies):
            bullet2_shot = False
        if pygame.sprite.spritecollideany(missile1, enemies):
            missile_shot = False
        if pygame.sprite.spritecollideany(bomb1, enemies):
            bomb_shot = False
        #Kills enemy bullets
        if pygame.sprite.spritecollideany(player, enemy_bullets):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(player, enemy_missiles):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(player, enemy_bombs):
            player.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False

        #Kills player
        if pygame.sprite.spritecollideany(enemy_bullet1, players):
            enemy_bullet1_shot = False
        if pygame.sprite.spritecollideany(enemy_bullet2, players):
            enemy_bullet2_shot = False
        if pygame.sprite.spritecollideany(enemy_missile1, players):
            enemy_missile_shot = False
        if pygame.sprite.spritecollideany(enemy_bomb1, players):
            enemy_bomb_shot = False
        #kills enemy
        if pygame.sprite.spritecollideany(enemy1, bullets):
            enemy1.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy1, missiles):
            enemy1.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
            running = False
        if pygame.sprite.spritecollideany(enemy1, bombs):
            enemy1.kill()
            screen.blit(background_image, (0, 0))
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(hz)
            time.sleep(1.5)
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
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()

game()