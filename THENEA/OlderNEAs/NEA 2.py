#All imported modules
import pygame
import random
from random import randint
from sys import exit
from Spriteloader import loadSprite_x,loadSprite_y
#custom library

import pygame.tests


#Outside of mainloop, initialises all necessary objects and runs them at all times
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
global screen
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
global psprtglb #playerspriteglobal
scroll = 0



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
        self.sf = 3 #60x90
        self.gravity = 10
        self.flip = True
        self.image = loadSprite_x(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
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
            self.image = loadSprite_x(self.spritesheet,self.width,self.height,self.jumpsprite,self.sf,self.flip)
            self.exponentfall+=1


    def walking(self):
        keys = pygame.key.get_pressed()
        if self.playerwalk_index > 18: self.playerwalk_index = 7
        if keys[pygame.K_d]:
            self.flip = True
            self.walking_frames()
            self.rect.x +=5
        if keys[pygame.K_a]:
            self.flip = False
            self.playerwalk_index +=1
            self.walking_frames()
            self.rect.x -=5
        elif not (keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_SPACE]):
            self.sprite_number = 1
            self.image = loadSprite_x(self.idlesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
            
    def walking_frames(self):
        self.playerwalk_index +=1
        if self.playerwalk_index > 18 :
            self.playerwalk_index = 7
        self.sprite_number = self.playerwalk_index
        self.image = loadSprite_x(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
        
        
    def update(self):
       self.walking()
       self.jumping()

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = pygame.image.load('Enemy/Zombie1.png').convert_alpha() #38x144 resolution, sprites vertical
        self.width = 38
        self.height = 48
        self.exponent_fall = 1
        self.sf = 1.75
        self.sprite_number = 1
        self.gravity = 10
        self.walk_index = 1
        self.flip = True
        self.image = loadSprite_y(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
        self.rect = self.image.get_rect(midbottom = (100,320))
        
    def walking(self):
        self.walk_index+=0.2
        if self.walk_index >= 4:self.walk_index = 1
        self.sprite_number = self.walk_index//1
        self.image = loadSprite_y(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
        self.rect.x+=2
        

        
        
        
    def jumping(self):
        self.rect.y += self.gravity
        if self.gravity < 10:
            self.gravity += 1.09**self.exponentfall
        if self.rect.y >= 320:
            self.rect.y = 320
            self.exponentfall = 1
#         if self.rect.y == 320 and keys[pygame.K_SPACE]:
#             self.gravity = -24
#         if self.rect.y < 320:
#             self.image = loadSprite_x(self.spritesheet,self.width,self.height,self.jumpsprite,self.sf,self.flip)
#             self.exponentfall+=1
        
    def update(self):
        self.walking()
        self.jumping()
        


def pathfinding():
    return None 

bg_images = []
for i in range(4, 8):
    bg_image = pygame.image.load(f"NeonVeil/NeonVeilBG{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(5):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0)) #(image i in list, ((multiplier x * bg_width) - (x position of image * speed)
      speed += 0.2

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

enemy1 = pygame.sprite.GroupSingle()
enemy1.add(Enemy1())



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
        draw_bg()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and scroll > 0:
            scroll -= 5
        if key[pygame.K_RIGHT] and scroll < 3000:
            scroll += 5
        #screen.blit(sky_surf,(50,50))
        # screen.blit(blittesting, (300,300)) # testing for blits
        
        player.draw(screen)
        player.update()
        
        enemy1.draw(screen)
        enemy1.update()
        
                

    
def animated_sprite(picture, width, height, sheetno):
    return None
            
                


#exit()
