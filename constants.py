import pygame

pygame.init()

#Game sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

#MAP VARS
MAP_WIDTH = 30
MAP_HEIGHT = 30

#Color definitions
COLOR_BLACK = (0 , 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

#Game colors
COLOR_DEFAULT_BG = COLOR_GREY

#SPRITES
S_PLAYER = pygame.image.load("data\Minitaur_32x32.png")
S_ENEMY = pygame.image.load("data\Hydra_32x32.png")
S_WALL = pygame.image.load("data\StoneWall_32x32.png")
S_FLOOR = pygame.image.load("data\StoneFloor_32x32.png")