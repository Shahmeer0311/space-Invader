import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load("spaces.png")
pygame.display.set_caption("space Invader") 
icon = pygame.image.load("justUfo.png")
pygame.display.set_icon(icon)
playerimg = pygame.image.load("spaceship1.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change =  0 
enemyimg = []
enemyX = []
enemyY = []
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 6
for
