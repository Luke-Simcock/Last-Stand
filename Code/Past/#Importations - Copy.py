#Importations
import pygame 
import sys
import random
import time
import os

#Game Settings
hz = 144
bullet_shoot = False
missile_shoot = False
bomb_shoot = False

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
player_speed = 7

player = pygame.Rect(WIDTH//2-40, HEIGHT-80, player_size, player_size)
running = True

#Weapons
#bullets
bullet_size = 20
bullet_speed = 10
missile_size = 20
missile_speed = 4
bomb_size = 20
bomb_speed = 1
player_bullet = pygame.Rect(player.x, player.y, bullet_size, bullet_size)
player_missile = pygame.Rect(player.x, player.y, missile_size, missile_size)
player_bomb = pygame.Rect(player.x, player.y, bomb_size, bomb_size)


#GAME LOOP ITSELF
while running:
    
    #Players Movement
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if keys[pygame.K_SPACE] or event.type == pygame.JOYBUTTONDOWN and event.button == 5: #Bullet shoot
            bullet_shoot = True
        if keys[pygame.K_m] or event.type == pygame.JOYBUTTONDOWN and event.button == 2: #Missile shoot
            missile_shoot = True
        if keys[pygame.K_b] or event.type == pygame.JOYBUTTONDOWN and event.button == 1: #Bomb shoot
            bomb_shoot = True

    #Joystick Stuff
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        
        # Axis 0: Left/Right movement
        left_x = joystick.get_axis(0)

        #Player Movement
        if left_x <= 0.1: player.x -= player_speed*abs(left_x)
        if left_x >= -0.1: player.x += player_speed*abs(left_x)

    if keys[pygame.K_a]: player.x -= player_speed
    if keys[pygame.K_d]: player.x += player_speed
    
    player.x = max(0, min(WIDTH - player_size, player.x))
    player.y = max(0, min(HEIGHT - player_size, player.y))

    if bullet_shoot is False:
        #move bullets to player
        player_bullet.x = player.x + 25
        player_bullet.y = player.y

    if bullet_shoot is True:
        player_bullet.y -= bullet_speed
        if player_bullet.y <= 10:
            bullet_shoot = False



    if missile_shoot is False:
        #move missile to player
        player_missile.x = player.x + 25
        player_missile.y = player.y
    
    if missile_shoot is True:
        player_missile.y -= missile_speed
        if player_missile.y <= 10:
            missile_shoot = False



    if bomb_shoot is False:
        #move bomb to player
        player_bomb.x = player.x + 25
        player_bomb.y = player.y
    
    if bomb_shoot is True:
        player_bomb.y -= bomb_speed
        if player_bomb.y <= 10:
            bomb_shoot = False



    #Drawing Characters
    pygame.draw.rect(screen, WHITE, player)

    #Drawing Weapons
    pygame.draw.rect(screen, WHITE, player_bullet)
    pygame.draw.rect(screen, WHITE, player_missile)
    pygame.draw.rect(screen, WHITE, player_bomb)

    #Kills Game
    if keys[pygame.K_ESCAPE]: sys.exit()

    #Cirtical Screen Stuff
    pygame.display.flip()
    screen.fill("black")
    clock.tick(hz)

pygame.quit()
sys.exit()