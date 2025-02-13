#All imported modules
import pygame
import random
from random import randint
from sys import exit
from Spriteloader import loadSprite #custom library

import pygame.tests


#Outside of mainloop, initialises all necessary objects and runs them at all times
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
global screen
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
global psprtglb #playerspriteglobal
psprtglb = 1
global playerx
playerx = 640
global playery
playery = 320



neon_surface = pygame.image.load('NeonVeil/NeonVeilBG4.png').convert()
#sky_surf = pygame.image.load('Sky.png').convert()


#2100,650






#Use sprites here
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idlesheet = pygame.image.load('Terraria_idle.png').convert_alpha()
        self.spritesheet =pygame.image.load('Terraria_playable_char.png').convert_alpha() 
        self.width = 20 #380/19 as total width of sheet / total sprites
        self.height = 30 # Height of spritesheet, does not need to be changed
        self.jumpsprite = 6
        self.exponentfall = 1
        self.playerwalk_index = 7
        self.playerwalk_index2 = 18
        self.idle_index = 1
        self.sprite_number = 1
        self.sf = 3
        self.gravity = 10
        self.flip = True
        self.image = loadSprite(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
        self.rect = self.image.get_rect(midbottom = (640,320))

    def jumping(self):
        self.rect.y += self.gravity
        if self.gravity < 10:
            self.gravity += 1.09**self.exponentfall
        keys = pygame.key.get_pressed()
        if self.rect.y >= 320:
            self.rect.y = 320
            self.exponentfall = 1
        if self.rect.y == 320 and keys[pygame.K_SPACE]:
            self.gravity = -24
        if self.rect.y < 320:
            self.image = loadSprite(self.spritesheet,self.width,self.height,self.jumpsprite,self.sf,self.flip)
            self.exponentfall+=1


    def walking(self):
        keys = pygame.key.get_pressed()
        if self.playerwalk_index > 18: self.playerwalk_index = 7
        if keys[pygame.K_d]:
            self.flip = True
            self.playerwalk_index +=1
            if self.playerwalk_index > 18:
                self.playerwalk_index == 7
            self.sprite_number = self.playerwalk_index
            self.image = loadSprite(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
            self.rect.x +=5
        if keys[pygame.K_a]:
            self.flip = False
            self.playerwalk_index +=1
            if self.playerwalk_index > 18 :
                self.playerwalk_index = 7
            self.sprite_number = self.playerwalk_index
            self.image = loadSprite(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
            self.rect.x -=5
        elif not (keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_SPACE]):
            self.sprite_number = 1
            self.image = loadSprite(self.idlesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
        
        
    def update(self):
       self.walking()
       self.jumping()

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__(init)__()
        self.spritesheet = pygame.image.load().convert_alpha
        
        
        
        
#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())



#blittesting = pygame.image.load('Terraria_playable_char.png').convert_alpha()

#Run the mainloop here
game_active = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
    pygame.display.update()
    clock.tick(60)
    if game_active == True:
        screen.blit(neon_surface,(0,0))
        #screen.blit(sky_surf,(50,50))
        # screen.blit(blittesting, (300,300)) # testing for blits
        
        player.draw(screen)
        player.update()
        
                
def image_size(picture):
    width = picture.width
    height = picture.height
    
def animated_sprite(picture, width, height, sheetno):
    return None
            
                


#exit()
