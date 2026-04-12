#5323 Alpha 2.2.1

#Importations
import os
import pygame 
import random
import sys
import time
import threading
from ctypes import windll
from tkinter import *
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

background_image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "Sprites", "Other", "Background1.png")), (1280, 720))

#Game
def game():
    #Game Settings
    player_speed =  16
    enemy_speed =   10
    bullet_speed =  6

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

    player_health = 15 +80
    enemy1_health = 1000
    player_bullet_damage = 10
    enemy1_bullet_damage = 25

    #Globilisation
    global enemy_time
    global LorR_Enemy
    global LorR_Calc
    global sprite_timer
    global bullet1_shot
    global bullet2_shot
    global bullet1
    global bullet2
    global enemy_bullet1_shot
    global enemy_bullet2_shot
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
    enemy_bullet1_shot = False
    enemy_bullet2_shot = False 
    


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
            if self.rect.left < sprite_gap_to_left:
                self.rect.left = sprite_gap_to_left
            if self.rect.right > SCREEN_WIDTH - sprite_gap_to_right:
                self.rect.right = SCREEN_WIDTH -sprite_gap_to_right

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
                LorR_Enemy = enemy1.rect.x / 1543 * 100
                LorR_Calc = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < sprite_gap_to_left:
                self.rect.left = sprite_gap_to_left
            if self.rect.right > SCREEN_WIDTH - sprite_gap_to_right:
                self.rect.right = SCREEN_WIDTH - sprite_gap_to_right

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
    
    # Instantiate sprites
    player = Player()

    bullet1 = Bullet()
    bullet2 = Bullet()

    enemy1 = Enemy()

    enemy_bullet1 = Enemy_Bullet()
    enemy_bullet2 = Enemy_Bullet()


    #Groups
    players = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    players.add(player
                )
    enemies.add(enemy1,
                )
    bullets.add(bullet1,
                bullet2
                )
    enemy_bullets.add(enemy_bullet1,
                enemy_bullet2
                )
    all_sprites.add(bullet1,
                    bullet2,
                    enemy_bullet1,
                    enemy_bullet2,
                    player, 
                    enemy1
                    )
    
    bullet_delay_time = 0
    bullet_delay_base = 20

    enemy_bullet_delay_time = 0
    enemy_bullet_delay_base = 20

    def bullets_updating():
        bullet1.update()
        bullet2.update()

    #GAME LOOP ITSELF
    while running:
        true = True
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        Health_Player = textfont.render(f" {player_health}", 1, (255,255,255))
        Health_Enemy = textfont.render(f" {enemy1_health}", 1, (255,255,255))

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        Thread1 = threading.Thread(player.update(pressed_keys))
        Thread2 = threading.Thread(enemy1.update())
        Thread3 = threading.Thread(target = bullets_updating)
        Thread7 = threading.Thread(enemy_bullet1.update())
        Thread8 = threading.Thread(enemy_bullet2.update())

        Thread1.start()
        Thread2.start()
        Thread3.start()
        Thread7.start()
        Thread8.start()

        
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
        #Kills enemy bullets
        if pygame.sprite.spritecollideany(enemy_bullet1, players):
            enemy_bullet1_shot = False
            player_health -= enemy1_bullet_damage
        if pygame.sprite.spritecollideany(enemy_bullet2, players):
            enemy_bullet2_shot = False
            player_health -= enemy1_bullet_damage
    
        #Kills player
        if player_health <= 0:
            if pygame.sprite.spritecollideany(player, enemy_bullets):
                player.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                time.sleep(1.5)
                running = False
        if enemy1_health <= 0:
            if pygame.sprite.spritecollideany(enemy1, bullets):
                enemy1.kill()
                screen.blit(background_image, (0, 0))
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
                pygame.display.flip()
                time.sleep(1.5)
                running = False




        enemy_bullet_chance = random.randint(1,50)

        if enemy_bullet_chance == 5:
            if enemy_bullet_delay_time <= 0:
                if enemy_bullet1_shot == False:
                    enemy_bullet1_shot = True
                    enemy_bullet_delay_time = enemy_bullet_delay_base
                elif enemy_bullet1_shot and enemy_bullet2_shot == False:
                    enemy_bullet2_shot = True
                    enemy_bullet_delay_time = enemy_bullet_delay_base


        enemy_bullet_delay_time -= 2

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            if bullet_delay_time <= 0:
                if bullet1_shot == False:
                    bullet1_shot = True
                    bullet_delay_time = bullet_delay_base
                elif bullet1_shot and bullet2_shot == False:
                    bullet2_shot = True
                    bullet_delay_time = bullet_delay_base

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                if bullet_delay_time <= 0:
                    if bullet1_shot == False:
                        bullet1_shot = True
                        bullet_delay_time = bullet_delay_base
                    elif bullet1_shot and bullet2_shot == False:
                        bullet2_shot = True
                        bullet_delay_time = bullet_delay_base
        
        bullet_delay_time -= 2

        Thread1.join()
        Thread2.join()
        Thread3.join()
        Thread7.join()
        Thread8.join()

        #Cirtical Screen Stuff
        screen.blit(background_image, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        screen.blit(Health_Player, (60, 175))
        screen.blit(Health_Enemy, (1025, 175))
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()

game()