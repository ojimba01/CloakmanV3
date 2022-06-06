import pygame
from pygame.locals import *
from config import *
from sprites import *

class player(object):
    def __init__(self,player_rec):
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.falling = False
        self.vertical_momentum = 0
        self.air_timer=0
        self.player_action = 'idle'
        self.player_frame = 0
        self.player_flip = False
        self.player_rect = pygame.Rect(player_rec)
        self.player_img_id = None
        self.player = None
        self.player_movement = None

        
        