#5323 pre game code

#Importations
import os
import pygame 
import random
import sys
import time
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
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
    bullet_speed =  20
    missile_speed = 8
    bomb_speed =    2

    #Enemy Intilisation

    global enemy_time
    global LorR_Enemy
    global LorR_Calc

    enemy_time = random.randint(45, 50)  # Pause duration in frames (3–5 seconds at 60 FPS)
    LorR_Enemy = random.choice([1, 100])     # Random left (-1) or right (+1)
    LorR_Calc = random.randint(0, 100)

    #Setting Up Window and Sprites values
    SCREEN_WIDTH = 1543
    SCREEN_HEIGHT = 864
    WHITE = (255, 255, 255)
    sprite_gap_to_border = 30
    player_size = 70
    enemy_size = 70

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            # Create the surface and assign it to the instance variable 'surf'
            self.surf = pygame.Surface((player_size, player_size))
            self.surf.fill((WHITE))  # This line was also misplaced - should be inside __init__
            # Now get the rect from the properly assigned surf
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - player_size/2 - sprite_gap_to_border)

        # Move the sprite based on user keypresses
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -player_speed)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, player_speed)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-player_speed, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(player_speed, 0)
            
            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= SCREEN_HEIGHT - player_size*3 - sprite_gap_to_border*2:
                self.rect.top = SCREEN_HEIGHT - player_size*3 - sprite_gap_to_border*2
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
            # Create the surface and assign it to the instance variable 'surf'
            self.surf = pygame.Surface((enemy_size, enemy_size))
            self.surf.fill((WHITE))  # This line was also misplaced - should be inside __init__
            # Now get the rect from the properly assigned surf
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size/2 + sprite_gap_to_border)

        # Move the sprite based on AI algorythm
        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc

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
                LorR_Enemy = enemy.rect.x / 1543 * 100
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

    #ESSENTIAL CODE DO NOT TOUCH
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()
    running = True

    #Create the screen object
    #The size is determined by the constant WIDTH and HEIGHT
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN) 
    pygame.display.set_caption("5323")

    # Instantiate player.
    player = Player()

    # Instantiate player.
    enemy = Enemy()

    #Groups
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    #GAME LOOP ITSELF
    while running:
        for event in pygame.event.get():            
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemy.update()

        #Cirtical Screen Stuff
        screen.fill("black")
        screen.blit(enemy.surf, enemy.rect)
        screen.blit(player.surf, player.rect)
        pygame.display.flip()
        clock.tick(hz)

    pygame.quit()
    sys.exit()

game()