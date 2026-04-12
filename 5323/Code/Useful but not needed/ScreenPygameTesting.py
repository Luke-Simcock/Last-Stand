import pygame
from ctypes import windll

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# Get window handle
info = pygame.display.get_wm_info()
hwnd = info['window']

# Move window to (100, 100) - top-left corner
windll.user32.MoveWindow(hwnd, 0, 0, 800, 600, True)