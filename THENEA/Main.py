#All imported modules
from Importfunctions import *
from SpriteGroups import *
import pytmx 

        




class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()
        
    def draw(self,target_pos):
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)



class Gamemain:
    def __init__(self):
        #Set variables
        pygame.init()
        self.current_stage_val = 0
        self.scroll = 0
        self.size = [WINDOW_WIDTH, WINDOW_HEIGHT]
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((1280,720))
        self.allSprites = AllSprites()
        self.collisiontiles = pygame.sprite.Group()
        self.platformtiles = pygame.sprite.Group()
        self.weapongroup =  pygame.sprite.Group()
        self.projectilegroup = pygame.sprite.Group()
        self.enemysprites = pygame.sprite.Group()
        self.Tileimgsize=32

        #Images to be used
        self.load_Stage()
            
    def load_Stage(self):   
        tmx_map = load_pygame('Maps\WIP.tmx')

        for x, y, image in tmx_map.get_layer_by_name('Background1').tiles():
            image.set_colorkey("Black")
            image = image.convert_alpha()
            Sprite((x * self.Tileimgsize,y * self.Tileimgsize), image, self.allSprites)
    
        for x, y, image in tmx_map.get_layer_by_name('Background2').tiles():
            image.set_colorkey("Black")
            image = image.convert_alpha()
            Sprite((x * self.Tileimgsize,y * self.Tileimgsize), image, self.allSprites)
        

        for x, y, image in tmx_map.get_layer_by_name('Platform').tiles():
            image.set_colorkey("Black")
            image = image.convert_alpha()
            Sprite((x * self.Tileimgsize,y * self.Tileimgsize), image, (self.allSprites,self.platformtiles))

        for x, y, image in tmx_map.get_layer_by_name('Main').tiles():
            image.set_colorkey("Black")
            image = image.convert_alpha()
            Sprite((x * self.Tileimgsize,y * self.Tileimgsize), image, (self.allSprites,self.collisiontiles)) 
            
        mainarray = tmx_map.get_layer_by_name("Main")
        maindata = mainarray.data

        for object in tmx_map.get_layer_by_name("Entities"):
            if object.name == "Player":
                self.player = PlayerSprites((object.x*2, object.y*2), self.allSprites, self.collisiontiles,self.platformtiles,self.projectilegroup,self.weapongroup,self.create_weapon,self.enemysprites)
            if object.name == "Enemy":
                self.enemy = Enemy((object.x*2,object.y*2), image, (self.allSprites,self.enemysprites))

        
    def create_weapon(self, pos, direction,surf):
        x = pos[0] + direction * -10 if direction == -1 else pos[0] + direction * -10 - surf.get_width()
        Weaponsprite(surf,(x,pos[1]-50),(self.weapongroup,self.allSprites),direction,self.enemysprites)


        
    def run(self):
        scroll = 0
        while self.running:
            dt = self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()

            self.allSprites.update(dt)
            self.screen.fill('#C7A5F8')
            self.allSprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Gamemain()
    game.run()