from Importfunctions import *
from Time import *
from Spriteloader import loadSprite_x,loadSprite_y
import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos,surface,groups):
        super().__init__(groups)
        self.image = surface
        self.image = pygame.transform.scale_by(self.image,2)
        self.rect = self.image.get_frect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

class PlayerSprites(Sprite):
    def __init__(self,pos,groups,tile_collision_group,platform_collision_group,bullet_group,weapon_group,create_weapon,enemygroup):
        surface = pygame.Surface ((40,60))
        all_sprites = groups
        print(groups)
        super().__init__(pos,surface,groups)
        self.playerwidth = 20 #380/19 as total width of sheet / totalSprites
        self.playerheight = 30 # Height ofSpritesheet, does not need to be changed
        self.spritesheet = pygame.image.load('Terraria_playable_char.png')
        self.playersprite_number = 7
        self.jumping = False
        self.playersprite_number = 1
        self.sf = 2 #60x90
        self.playerflip = True
        self.image = loadSprite_x(self.spritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
        self.speed = 450
        self.rect = self.image.get_rect(center= (pos))
        self.direction = pygame.math.Vector2()
        self.collision_tiles = tile_collision_group
        self.platformtiles = platform_collision_group
        self.speed_y = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.facing = 1


        self.inventory = []
        self.inventory.append("sword")
        self.inventory.append("bow")
        self.inventory.append("wand")
        self.currentitem = "sword"




        self.weapongroup = weapon_group
        self.bulletgroup = bullet_group
        self.createweapon = create_weapon
        self.weapon = Weapon(weapon_group,all_sprites)

        self.action_timer = Timefunctions(500)

    def inputs(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        if keys[pygame.K_1] and not self.action_timer.timeractive:
            self.invetorymethod(0)
            self.action_timer.starttimefunc()
            print("hehehe")
        if keys[pygame.K_2] and not self.action_timer.timeractive:
            self.invetorymethod(1)
            self.action_timer.starttimefunc()
            print("yipee")
        if keys[pygame.K_3] and not self.action_timer.timeractive: 
            self.invetorymethod(2)
            self.action_timer.starttimefunc()
            print("Yessir")
        if keys[pygame.K_x] and not self.action_timer.timeractive:
            weaponsurf = self.weapon.returnweaponsurf()
            self.createweapon(self.rect.center,-1 if self.playerflip else 1, weaponsurf)
            self.action_timer.starttimefunc()
            print(self.currentitem)
        if self.action_timer and self.currentitem == "sword":
            self.direction.x = 0

    def movement(self,dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += (self.speed_y * 200 * dt)
        #self.rect.y += self.direction.y*600*dt
        self.collision('vertical')

        self.speed_y = (self.speed_y+1.1**1.1*0.5) if self.speed_y< 8 else self.speed_y

 

    def collision(self,direction):
        keys = pygame.key.get_pressed()
        for sprite in self.collision_tiles:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                if direction == 'vertical':
                    if self.direction.y < 0 or self.speed_y <= 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0 or self.speed_y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.jumping=False
                        if keys[pygame.K_UP]:
                            self.speed_y = -10
                            self.jumping=True
        for sprite in self.platformtiles:
                if sprite.rect.colliderect(self.rect):
                    if direction == 'vertical' and keys[pygame.K_DOWN] != 1:
                        if self.direction.y > 0 or self.speed_y >= 0 and self.rect.bottom <= sprite.rect.bottom:
                            self.rect.bottom = sprite.rect.top
                            self.jumping=False
                            if keys[pygame.K_UP]: 
                                self.speed_y = -10
                                self.jumping=True

    def invetorymethod(self,currentitem):
        self.currentitem = self.inventory[currentitem]
        self.weapon.currentweapon(self.currentitem)

    def animation(self):
        if self.playersprite_number > 18 or self.playersprite_number < 7 :
            self.playersprite_number = 7
        if self.direction.x > 0: 
            self.playerflip = True
            self.facing = 1
        if self.direction.x < 0:
            self.playerflip = False
            self.facing = -1
        if self.direction.x != 0: self.playersprite_number+=1
        if self.direction.x == 0: self.playersprite_number = 1
        if self.jumping: self.playersprite_number=6
        self.image = loadSprite_x(self.spritesheet,self.playerwidth,self.playerheight,self.playersprite_number,self.sf,self.playerflip)
    


            
    def update(self,dt):
        self.action_timer.update()
        self.inputs()
        self.animation()
        self.movement(dt)


class Weapon(pygame.sprite.Sprite):
    def __init__(self,weapon_group,all_sprites):
        super().__init__()
        self.image = pygame.image.load(f"Graphics/Weapon/muramasa.png").convert_alpha()
        self.display_surface = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        self.weapongroup = weapon_group
        self.all_sprites = all_sprites
        self.usagetimer = Timefunctions(500)

    def currentweapon(self,weapon):
        if weapon == "sword":
            self.image = pygame.image.load(f"Graphics/Weapon/muramasa.png").convert_alpha()
        if weapon == "bow":
             self.image = pygame.image.load(f"Graphics/Weapon/phantasm.png").convert_alpha()
        if weapon == "wand":
            self.image = pygame.image.load(f"Graphics/Weapon/wandweapon.png").convert_alpha()
    
    def returnweaponsurf(self):
        return self.image
                

class Weaponsprite(Sprite):
    def __init__(self, surface, pos, groups, direction, enemygroup):
        self.pos = pos
        super().__init__(self.pos, surface, groups)
        self.image = surface
        self.image = pygame.transform.flip(self.image,direction == 1, False)
        self.timer = Timefunctions(300,methods=self.kill,autostart=True)
        self.hitframetimer = Timefunctions(500,methods=self.increment)
        self.enemygroup = enemygroup
        self.counter = True
    
    def increment(self):
        if self.counter == False: self.counter = True

    def collisions(self):
        for sprite in self.enemygroup:
            if sprite.rect.colliderect(self.rect):
                if self.counter:
                    sprite.hp -=1
                    self.hitframetimer.starttimefunc()
                    self.counter = False
                    print(sprite.hp)
                    if sprite.hp <= 0:
                        sprite.kill()
        

    def update(self,dt):
        self.timer.update()
        self.collisions()

class Enemy(Sprite):
    def __init__(self, pos, surface, groups):
        super().__init__(pos, surface, groups)
        #utility, main components
        self.batimg = pygame.image.load(f"Enemy/Bat.png").convert_alpha()
        self.width = 44
        self.height = 32
        self.spritenum = 1
        self.sf = 1
        self.flip = False
        self.image = loadSprite_y(self.batimg,self.width,self.height,self.spritenum,self.sf,self.flip)
        self.timer = Timefunctions(100, methods= self.increment,repeat=True,autostart=True)
        self.counter = True

        #Stats and game usage
        self.hp = 3

    
    def increment(self):
        if self.counter == False: self.counter = True


    def animations(self):
        if self.counter == True:
            self.spritenum +=1
            self.counter = False
            if self.spritenum == 4: self.spritenum = 1
        self.image = loadSprite_y(self.batimg,self.width,self.height,self.spritenum,self.sf,self.flip)
        
    
    def update(self,dt):
        self.animations()
        self.timer.update()