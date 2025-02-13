#All imported modules
import pygame
import random
from random import randint
from sys import exit
import math
from Spriteloader import loadSprite_x,loadSprite_y  #custom library

import pygame.tests


#Outside of mainloop, initialises all necessary objects and runs them at all times
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
global psprtglb #playerspriteglobal


##bg_images = []
##bg_rects = []
##for i in range(4, 8):
##    bg_image = pygame.image.load(f"NeonVeil/NeonVeilBG{i}.png").convert_alpha()
##    bg_rect = bg_image.get_rect()
##    bg_images.append(bg_image)
##    bg_rects.append(bg_rect)
##bg_width = bg_images[1].get_width()



#2100,650

class World():
    def __init__(self,Player):
        self.surface_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
            super().__init__()
            self.display_surface = pygame.display.get_surface()

            # camera offset 
            self.offset = pygame.math.Vector2()
            self.half_w = self.display_surface.get_size()[0] // 2
            self.half_h = self.display_surface.get_size()[1] // 2

##            self.bg_images = []
##            self.bg_rects = []
##            for i in range(4, 8):
##                self.bg_image = pygame.image.load(f"NeonVeil/NeonVeilBG{i}.png").convert_alpha()
##                self.bg_rect = self.bg_image.get_rect()
##                self.bg_images.append(self.bg_image)
##                self.bg_rects.append(self.bg_rect)  

            self.bg_image = pygame.image.load(f"NeonVeil/NeonVeilBG4.png").convert_alpha()
            self.bg_rect = self.bg_image.get_rect(topleft = (0,0))
            
    def elementdraw(self):
        

        self.display_surface.blit(self.bg_image,self.bg_rect)

        for sprite in sorted(self.sprites(),key = lambda sprite : sprite.rect.centery):
            screen.blit(sprite.image,sprite.rect)



#Use sprites here
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__()
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
        self.sf = 3 #60x90
        self.playergravity = 10
        self.playerflip = True
        self.change_x = 0
        self.change_y = 0
        self.speed=3
        self.image = loadSprite_x(self.playerspritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
        self.rect = self.image.get_rect(midbottom = (pos))
        self.direction = pygame.math.Vector2()
        self.player_x = self.rect.x
        self.player_y = self.rect.y

    def jumping(self):
        self.change_y = self.playergravity
        self.rect.y += self.change_y
        if self.playergravity < 10:
            self.playergravity += 1.05**self.playerexponentfall
        if self.rect.y >= 320:
            self.rect.y = 320
            self.playerexponentfall = 1
        keys = pygame.key.get_pressed()
        if self.rect.y == 320 and keys[pygame.K_SPACE]:
            self.playergravity = -30
        if self.rect.y < 320:
            self.image = loadSprite_x(self.playerspritesheet,self.playerwidth,self.playerheight,self.playerjumpsprite,self.sf,self.playerflip)
            self.playerexponentfall+=5
        if self.rect.y >= WINDOW_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = WINDOW_WIDTH - self.rect.height


    def walking(self):
        self.rect.x += self.change_x
        keys = pygame.key.get_pressed()
        if self.playerwalk_index > 18: self.playerwalk_index = 7
        if keys[pygame.K_d]:
            self.playerflip = True
            self.walking_frames()
            self.change_x = self.speed
        if keys[pygame.K_a]:
            self.playerflip = False
            self.playerwalk_index +=1
            self.walking_frames()
            self.change_x = -self.speed
        elif not (keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_SPACE]):
            self.playersprite_number = 1
            self.image = loadSprite_x(self.playerspritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
            self.change_x = 0
        self.rect.x+=self.change_x
            
    def walking_frames(self):
        self.playerwalk_index +=1
        if self.playerwalk_index > 18 :
            self.playerwalk_index = 7
        self.playersprite_number = self.playerwalk_index
        self.image = loadSprite_x(self.playerspritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
        
        
    def update(self):
       self.walking()
       self.jumping()

class Enemy1(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.spritesheet = pygame.image.load('Enemy/Zombie1.png').convert_alpha() #38x144 resolution, sprites vertical
        self.width = 38
        self.height = 48
        self.exponent_fall = 1
        self.sf = 1.75
        self.sprite_number = 1
        self.gravity = 10
        self.walk_index = 1
        self.change_x = 0
        self.change_y = 0
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

# 
#      def calc_grav(self):
#         """ Calculate effect of gravity. """
#         if self.change_y == 0:
#             self.change_y = 1
#         else:
#             self.change_y += .35
#  
        
#  
    def update(self):
        self.walking()
        self.jumping()
        

    

def pathfinding():
    return None 




#Groups for sprites
#player = Player()


camera_group = CameraGroup()

player = pygame.sprite.GroupSingle()
player.add(Player((1280/2,720/2),camera_group))
enemy1 = pygame.sprite.Group()
enemy1.add(Enemy1((200,360),camera_group))
#Player((1280/2,720/2),camera_group)

#Level methods
world = World(Player)

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


neon_surface = pygame.image.load('NeonVeil/NeonVeilBG4.png').convert()
ground_image = pygame.image.load("ground.png").convert_alpha()
groud_rect= ground_image.get_rect()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

def draw_ground(scroll):
    for n in range(20):
        screen.blit(ground_image, ((n * ground_width) - scroll * 1.5, WINDOW_HEIGHT - ground_height))


def main():
    scroll = 0
    size = [WINDOW_WIDTH, WINDOW_HEIGHT]
    screen = pygame.display.set_mode(size)
    game_active = True
    running = True
    while running:
        if game_active == True:
            #draw_bg(scroll)
            
            draw_ground(scroll)
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and scroll > 0:
                scroll -= 5
            if key[pygame.K_d] and scroll < 3000:
                scroll += 5
    #         camera.x = playermain.playerx-WINDOW_WIDTH/2
    #         camera.y = playermain.playery-WINDOW_HEIGHT/2
            camera_group.update()
            camera_group.elementdraw()
##            player.draw(screen)
##            player.update()
            
            enemy1.draw(screen)
            enemy1.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit()
        pygame.display.update()
        clock.tick(60)

    
                

    
def animated_sprite(picture, width, height, sheetno):
    return None
            
main()

#exit()
