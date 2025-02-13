#All imported modules
import pygame
import random
from random import randint
from sys import exit
import math
from Spriteloader import loadSprite_x,loadSprite_y  #custom library



    


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ground_image = pygame.image.load("ground1.png").convert_alpha()
        self.groud_rect= self.ground_image.get_rect()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

class World():
    def __init__(self,player):
        self.surface_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.stage_list = []
    def appending(



class Stage1(World):
    def __init__(self,scroll):
        self.groundsurf = Ground()
        for n in range(20):
            self.surface_list.append(self.groundsurf.groundrect)
            screen.blit(self.groundsurf.ground_image, ((n * self.groundsurf.ground_width) - scroll * 1.5, WINDOW_HEIGHT - self.groundsurf.ground_height))
            self.stage_list.append(self.surface_list)

