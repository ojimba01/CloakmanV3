import pygame
from pygame.locals import *
from config import *
class blocks(object):
    def __init__(self):
        pass
    def transformsprites(filename):
        transform = pygame.image.load(filename)
        fulltransform = pygame.transform.scale(transform, (32,32)) 
        return fulltransform