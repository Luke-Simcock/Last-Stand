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

#Game
def game():
    #Game Settings
    
    #speed normilisation
    player_speed =  14
    enemy_speed =   10
    bullet_speed =  10
    missile_speed = 8
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

    #Globilisation
    global enemy_time
    global LorR_Enemy
    global LorR_Calc
    global sprite_timer
    global bullet1_shot
    global bullet2_shot
    global bullet3_shot

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

    class Bullet(pygame.sprite.Sprite):

        def __init__(self):
            super(Bullet, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Weapons/Bullet/Frame1.png").convert(),
                (bullet_size_w, bullet_size_h))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (player.rect.x  + player_size_h/2, player.rect.y + bullet_size_h/2)   

        def update(self):
            
            global sprite_timer, bullet1_shot, bullet2_shot, bullet3_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Weapons/Bullet/Frame1.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Weapons/Bullet/Frame2.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Weapons/Bullet/Frame3.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Weapons/Bullet/Frame4.png").convert(),
                    (bullet_size_w, bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Users/luke/OneDrive - Riverside College Halton/lessons/unit 4 (Ben)/5323/Sprites/Weapons/Bullet/Frame5.png").convert(),
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

    # Instantiate sprites
    player = Player()

    enemy1 = Enemy()

    bullet1 = Bullet()
    bullet2 = Bullet()
    bullet3 = Bullet()

    #Groups
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    enemies.add(enemy1
                )

    bullets.add(bullet1,
                bullet2,
                bullet3
                )
    
    all_sprites.add(player, 
                    enemy1, 
                    bullet1,
                    bullet2,
                    bullet3 
                    )
    
    bullet_delay_time = 0
    bullet_delay_base = 3

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
        
        if sprite_timer == 0:
            sprite_timer = 100 
        else:
            sprite_timer -= 5

        if pygame.sprite.spritecollideany(enemy1, bullets):
            enemy1.kill()
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
                    bullet_delay_time = 30
                elif bullet1_shot and bullet2_shot == False:
                    bullet2_shot = True
                    bullet_delay_time = 30
                elif bullet1_shot and bullet2_shot and bullet3_shot == False:
                    bullet3_shot = True
                    bullet_delay_time = 30

        bullet_delay_time -= bullet_delay_base

        #Cirtical Screen Stuff
        screen.fill("black")
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()

game()