import pygame
import math
import pygame


SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLISSION_DISTANCE_=27

pygame.init()

scree =  pygame.Screen.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT))