# All Imports
#-------------------------------------------------------------------------------
import pygame
# from movement import *
from pygame.locals import *
import sys
from config import *
from blocks import blocks
from player import player as p
from  movement import collision_test, move
from sprites import *
from load import *


#Clock Configuration
#-------------------------------------------------------------------------------
clock = pygame.time.Clock()

#Pygame Initialization
#-------------------------------------------------------------------------------
pygame.init()
pygame.display.set_caption("CloackMan")

#Window Configuration
#-------------------------------------------------------------------------------
WINDOW_SIZE = (WIN_WIDTH, WIN_HEIGHT)


#Block/Background Configuration
#-------------------------------------------------------------------------------
grass=blocks.transformsprites("blocks/tile001.png")
dirt=blocks.transformsprites("blocks/tile013.png")
scene = pygame.image.load("spritesheets/background/background.png")
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((320, 240))
true_display=pygame.transform.scale(display, WINDOW_SIZE)
screen.blit(true_display, (0,0))
# **scaling the display to window size
true_scene=pygame.transform.scale(scene, BACKGROUND)
true_scroll = [0,0]

tilemap = map.load_map('tilemap')

rect = pygame.Rect(100,100,32,32)
p1 = p(rect)

animation_database = {}

animation_database['run'] = sprites.load_animation('player_animations/run',[7,7,7,7,7,7])
animation_database['idle'] = sprites.load_animation('player_animations/idle',[7,7,7,7])
animation_database['jump'] = sprites.load_animation('player_animations/jump',[4,4,4])
animation_database['jumpdown'] = sprites.load_animation('player_animations/jumpdown',[4,4,4])

#Game Loop
while True:
    screen.blit(true_scene, (0,-480))
    tile_rects = []

# Below is the scrolling feaature within the game that allows the screen to essentially follow the p1.player.
    true_scroll[0] += (p1.player_rect.x-true_scroll[0]-222)/20
    true_scroll[1] += (p1.player_rect.y-true_scroll[1]-212)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    y = 0
# Populates the tiles with the correct images on to the screen in occordance with the tilemap.
    for row in tilemap:
        x = 0
        for tile in row:
            if tile == '2':
                screen.blit(grass, (x * TILE_SIZE - true_scroll[0], y * TILE_SIZE - true_scroll[1]))
            if tile == '1':
                screen.blit(dirt, (x * TILE_SIZE - true_scroll[0], y * TILE_SIZE - true_scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
# This is the coordinate/movement detection for the player [0,1]=[x,y].
    p1.player_movement = [0,0]
    if p1.moving_right == True:
        p1.player_movement[0] += 4
    if p1.moving_left == True:
        p1.player_movement[0] -= 4
    p1.player_movement[1] += p1.vertical_momentum
    p1.vertical_momentum += 0.2
    if p1.vertical_momentum > 4:
        p1.vertical_momentum = 4

# This is the key & direction detection for the sprite's frame.
    if p1.player_movement[0] == 0:
        p1.player_action,p1.player_frame = sprites.change_action(p1.player_action,p1.player_frame,'idle')
    if p1.player_movement[0] > 0 and collisions['bottom']==True:
        p1.player_flip = False
        p1.player_action,p1.player_frame = sprites.change_action(p1.player_action,p1.player_frame,'run')
    if p1.player_movement[0] < 0 and collisions['bottom']==True:
        p1.player_flip = True
        p1.player_action,p1.player_frame = sprites.change_action(p1.player_action,p1.player_frame,'run')
    if p1.player_movement[0] > 0:
        if p1.vertical_momentum < 0 :
            p1.player_flip = False
            p1.player_action,p1.player_frame = sprites.change_action(p1.player_action,p1.player_frame,'jump')
    if p1.player_movement[0] < 0:
        if p1.vertical_momentum < 0 :
            p1.player_flip = True
            p1.player_action,p1.player_frame = sprites.change_action(p1.player_action,p1.player_frame,'jump')
    p1.player_rect,collisions = move(p1.player_rect, p1.player_movement, tile_rects)

    if collisions['bottom']:
        p1.air_timer = 0
        p1.vertical_momentum = 0
        p1.jumping = False
    else:
        p1.air_timer += 1
    
    p1.player_frame += 1
    if p1.player_frame >= len(animation_database[p1.player_action]):
        p1.player_frame = 0
    p1.player_img_id = animation_database[p1.player_action][p1.player_frame]
    p1.player = animation_frames[p1.player_img_id]
    screen.blit(pygame.transform.flip(p1.player,p1.player_flip,False),(p1.player_rect.x-scroll[0],p1.player_rect.y-scroll[1]))

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                p1.moving_right = True
            if event.key == K_LEFT:
                p1.moving_left = True
            if event.key == K_UP:
                if (p1.air_timer < 6):
                    p1.jumping=True
                    p1.falling=False
                    p1.vertical_momentum = -6
                    p1.player_movement[1] = -5.2
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                p1.moving_right = False
            if event.key == K_LEFT:
                p1.moving_left = False
            if event.key == K_UP:
                p1.jumping = False


    pygame.display.update()
    clock.tick(60)
