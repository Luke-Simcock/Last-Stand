#Importations
import pygame 
import sys
import random
import time
import os

#Game Settings
hz = 240

#Enemy Intilisation
enemy_time = random.randint(45, 50)  # Pause duration in frames (3–5 seconds at 60 FPS)
LorR_Enemy = random.choice([1, 100])     # Random left (-1) or right (+1)
LorR_Calc = random.randint(0, 100)

#ESSENTIAL CODE DO NOT TOUCH
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

#Setting Up Window
WIDTH = 1543
HEIGHT = 864

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN) 
pygame.display.set_caption("5323")

#Player Colour
WHITE = (255, 255, 255)
player_size = 70
player_speed = 1
enemy_speed = 0.7

#Players Assignment
enemy_rect = pygame.Rect(WIDTH//2-40, 10, player_size, player_size)
player_rect = pygame.Rect(WIDTH//2-40, HEIGHT-80, player_size, player_size)
running = True

#GAME LOOP ITSELF
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    #Players Movement
    keys = pygame.key.get_pressed()

    #Joystick Stuff
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        
        # Axis 0: Left/Right movement
        left_x = joystick.get_axis(0)

        #Player Movement
        if left_x <= 0.1: player_rect.x -= player_speed*abs(left_x)
        if left_x >= -0.1: player_rect.x += player_speed*abs(left_x)

    if keys[pygame.K_a]: player_rect.x -= player_speed
    if keys[pygame.K_d]: player_rect.x += player_speed
    
    player_rect.x = max(0, min(WIDTH - player_size, player_rect.x))
    player_rect.y = max(0, min(HEIGHT - player_size, player_rect.y))


    #Enemy Movement
    if enemy_time > 0:
        enemy_time -= 1

        #timer runs out
        if LorR_Enemy >= LorR_Calc:  
            enemy_rect.x -= enemy_speed   #left
        elif LorR_Enemy < LorR_Calc: 
            enemy_rect.x += enemy_speed   #right

    else:
        #Reset
        enemy_time = random.randint(45, 50)  # Pause duration in frames (3–5 seconds at 60 FPS)
        LorR_Enemy = enemy_rect.x / 1543 * 100
        LorR_Calc = random.randint(0, 100) 
        
    enemy_rect.x = max(0, min(WIDTH - player_size, enemy_rect.x))
    enemy_rect.y = max(0, min(HEIGHT - player_size, enemy_rect.y))

    #Drawing Characters
    pygame.draw.rect(screen, WHITE, player_rect)
    pygame.draw.rect(screen, WHITE, enemy_rect)

    #Kills Game
    if keys[pygame.K_ESCAPE]: sys.exit()

    #Cirtical Screen Stuff
    pygame.display.flip()
    screen.fill("black")
    clock.tick(hz)

pygame.quit()
sys.exit()