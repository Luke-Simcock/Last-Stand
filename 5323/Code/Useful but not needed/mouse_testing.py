import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP

x = 0


pygame.init()
clock = pygame.time.Clock()

while x == 0:
    mouse_buttons = pygame.mouse.get_pressed()
    print(mouse_buttons)