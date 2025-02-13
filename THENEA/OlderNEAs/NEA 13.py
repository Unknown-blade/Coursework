#All imported modules
import pygame
import random
from random import randint
from sys import exit
import math
from Spriteloader import loadSprite_x,loadSprite_y  #custom library
from Stagetilemaps import *

import pygame.tests


#Outside of mainloop, initialises all necessary objects and runs them at all times
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()


#2100,650










class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ground_image = pygame.Surface([63,63])
        self.ground_image = pygame.image.load("ground1.png").convert_alpha()
        self.rect= self.ground_image.get_rect()
    def return_ground(self):
        return self.ground_image



    

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.idlesheet = pygame.image.load('Terraria_idle.png').convert_alpha()
        self.playerspritesheet =pygame.image.load('Terraria_playable_char.png').convert_alpha() 
        self.playerwidth = 20 #380/19 as total width of sheet / total sprites
        self.playerheight = 30 # Height of spritesheet, does not need to be changed
        self.playerjumpsprite = 6
        self.playerexponentfall = 1
        self.playerwalk_index = 7
        self.playerwalk_index2 = 18
        self.playeridle_index = 1
        self.playersprite_number = 1
        self.sf = 2.1 #60x90
        self.playergravity = 10
        self.playerflip = True
        self.speed=5
        self.speed_y = 0
        self.image = loadSprite_x(self.playerspritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
        self.rect = self.image.get_rect(center= (pos))
        self.direction = pygame.math.Vector2()
        self.change_y=0
        self.tilecollisionlist = camera_group.tilelist


    def inputs(self):
        keys = pygame.key.get_pressed()
        if self.playerwalk_index > 18: self.playerwalk_index = 7
        self.direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        if self.direction.x <= -1: self.horizontal = "left"
        if self.direction.x >= 1: self.horizontal == "right"
        elif self.direction.x == 0: self.horizontal = ""
        self.direction.y = int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
        if self.direction.y >= 1: self.vertical = "down"
        elif self.direction.y <= -1: self.vertical = "up"
        elif self.direction.y == 0: self.vertical = ""
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self,dt):
        self.rect.x+=self.direction.x*self.speed*dt
        self.collision("horizontal")
        self.rect.y+=self.direction.y*self.speed*dt
        self.collision("vertical")

    def collision(self,direction):
        for tile in self.tilecollisionlist:
            if tile[1].colliderect(self.rect.x+self.direction.x,self.rect.y,self.playerwidth,self.playerheight):
                if self.direction.x > 0: self.rect.right = tile[1].left-self.direction.x
                if self.direction.x < 0: self.rect.left = tile[1].right-self.direction.x
            
    def jumping(self):
        if self.direction.y and self.change_y==1:
            self.direction.y = -2
            self.change_y=0
                

    def walking_frames(self):
        self.playerwalk_index +=1
        if self.playerwalk_index > 18 :
            self.playerwalk_index = 7
        self.playersprite_number = self.playerwalk_index
        self.image = loadSprite_x(self.playerspritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
        

            
    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.inputs()
        self.move(dt)
        if keys[pygame.K_SPACE]: self.jumping()
        self.rect.center += self.direction*self.speed

       
        
            
        

##class Enemy1(pygame.sprite.Sprite):
##    def __init__(self,pos,group):
##        super().__init__(group)
##        self.spritesheet = pygame.image.load('Enemy/Zombie1.png').convert_alpha() #38x144 resolution, sprites vertical
##        self.width = 38
##        self.height = 48
##        self.exponent_fall = 1
##        self.sf = 1.75
##        self.sprite_number = 1
##        self.gravity = 10
##        self.walk_index = 1
##        self.change_x = 0
##        self.change_y = 0
##        self.flip = True
##        self.image = loadSprite_y(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
##        self.rect = self.image.get_rect(midbottom = (100,320))
##        
##    def walking(self):
##        self.walk_index+=0.2
##        if self.walk_index >= 4:self.walk_index = 1
##        self.sprite_number = self.walk_index//1
##        self.image = loadSprite_y(self.spritesheet,self.width,self.height,self.sprite_number,self.sf,self.flip)
##        self.rect.x+=2        
##        
##    def jumping(self):
##        self.rect.y += self.gravity
##        if self.gravity < 10:
##            self.gravity += 1.09**self.exponentfall
##        if self.rect.y >= 320:
##            self.rect.y = 320
##            self.exponentfall = 1
##         if self.rect.y == 320 and keys[pygame.K_SPACE]:
##             self.gravity = -24
##         if self.rect.y < 320:
##             self.image = loadSprite_x(self.spritesheet,self.width,self.height,self.jumpsprite,self.sf,self.flip)
##             self.exponentfall+=1
##
## 
##      def calc_grav(self):
##         """ Calculate effect of gravity. """
##         if self.change_y == 0:
##             self.change_y = 1
##         else:
##             self.change_y += .35
###  
        
#  
##    def update(self):
##        self.walking()
##        self.jumping()

        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.tilelist = []
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.bg_width = int(self.display_surface.get_size()[0])
        self.bg_height = int(self.display_surface.get_size()[1])
        print(self.bg_width)
        self.bgbg_image = pygame.image.load(f"NeonVeil/NeonVeilBG4.png").convert_alpha()
        self.ground_image = pygame.image.load("ground.png").convert_alpha()
        self.bgbg_rect = self.bgbg_image.get_rect(center = (0,0))
        print(self.bgbg_rect)
        self.offsetposlocal = (640,320)
        self.tilesize = 64
        
        
        #Images to be used in #draw_stages
        self.ground_image = pygame.Surface([63,63])
        self.ground_image = pygame.image.load("ground1.png").convert_alpha()
        
        #Tilemap conversions
        self.datamap = Stage0.tilemap()
        row=0
        for rows in self.datamap:
            self.typing = ""
            column = 0
            for tile in rows:
                if tile == 1:
                    img = pygame.transform.scale(self.ground_image, (self.tilesize,self.tilesize))
                    img_rect = img.get_rect()
                    img_rect.x = column * self.tilesize
                    img_rect.y = row * self.tilesize
                    tile = (img, img_rect)
                    self.tilelist.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(self.ground_image, (self.tilesize,self.tilesize))
                    img_rect = img.get_rect()
                    img_rect.x = column * self.tilesize
                    img_rect.y = row * self.tilesize
                    tile = (img, img_rect)
                    self.tilelist.append(tile)
                print(tile)
                column+=1
            row+=1
        
        

        self.bg_images = []
        self.bg_rects = []
        for i in range(5, 8):
            self.bg_image = pygame.image.load(f"NeonVeil/NeonVeilBG{i}.png").convert_alpha()
            self.bg_rect = self.bg_image.get_rect()
            self.bg_images.append(self.bg_image)
            self.bg_rects.append(self.bg_rect)

    

    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h


    def draw_bg(self,scroll):
        self.display_surface.blit(self.bgbg_image,(self.offsetposlocal[0]-2174,self.offsetposlocal[1]-400))
        for n in range(10):
            speed = 3
            count=0
            for i in self.bg_images:
                self.display_surface.blit(i, ((n * int(i.get_size()[0])) - scroll * speed, 0)) #(image i in list, ((multiplier x * bg_width) - (x position of image * speed)
                speed += 0.1

    def draw_stages(self,current_stage,stage0):
        for tile in self.tilelist:
            surface_offset = tile[1].topleft - self.offset
            screen.blit(tile[0], surface_offset)
        
        
        

    def elementdraw(self,player):

        self.center_target_camera(player)
        for sprite in sorted(self.sprites()):
            screen.blit(sprite.image,(player.rect.x,player.rect.y))
        
        # for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):
        #     offsetpos = sprite.rect.center -self.offset
        #     self.offsetposlocal = offsetpos
        #     screen.blit(sprite.image,offsetpos)
        

#Use sprites here

        

    

def pathfinding():
    return None 




#Groups for sprites
#player = Player()


camera_group = CameraGroup()
player = Player((640,360),camera_group)
stage0 = Stage0()
ground = Ground()
##enemy1 = pygame.sprite.Group()
##enemy1.add(Enemy1((200,360),camera_group))


#Level methods

#Run the mainloop here


##def draw_bg(scroll):
##    for n in range(5):
##        speed = 5
##        for i in bg_images:
##            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
##            bg_rect.x = i * bg_width + scroll
##            screen.blit(i, ((n * bg_width) - scroll * speed, 0)) #(image i in list, ((multiplier x * bg_width) - (x position of image * speed)
##            speed += 0.2
##            pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
##          for n in range(0, tiles):
##              screen.blit(bg, (i * bg_width + scroll, 0))
##              bg_rect.x = n * bg_width + scroll
##              pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)






##class Tree(pygame.sprite.Sprite):
##    def __init__(self,pos,group):
##        super().__init__(group)
##        self.image = pygame.image.load('Enemy/Zombie1.png').convert_alpha()
##        self.rect = self.image.get_rect(topleft = pos)
##            
##for i in range(20):
##    random_x = randint(1000,2000)
##    random_y = randint(1000,2000)
##    Tree((random_x,random_y),camera_group)

class Main:
    def __init__(self):
        #Set variables
        pygame.init()
        self.scroll = 0
        self.val = 0
        size = [WINDOW_WIDTH, WINDOW_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def run(self):

        dt = self.clock.tick(60)/1000
        game_active = True
        running = True
        while running:
            if game_active == True:
                key = pygame.key.get_pressed()
                if key[pygame.K_a] and self.scroll > 0:
                    self.scroll -= 3
                if key[pygame.K_d] and self.scroll < 3000:
                    self.scroll += 3
                camera_group.draw_bg(self.scroll)
                camera_group.draw_stages(self.val,stage0)
                camera_group.update(dt)
                camera_group.elementdraw(player)
    ##            player.draw(screen)
    ##            player.update()
                
    ##            enemy1.draw(screen)
    ##            enemy1.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit()
            pygame.display.update()

    
                
            
main = Main()
main.run()

#exit()