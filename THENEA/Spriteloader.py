import pygame

# spritesheet parameter needs to be in form of pygame.image.load('some dir')
# if the png has a transparant background then use pygame.image.load('some dir').convert_alpha

# width and height relate to the width and height of the sprite

# scale factor is to do with how large you want the character

# to load the sprite you need to do screen.blit(Spriteloader.loadSprite(*args), (x,y))
def loadSprite_x(spritesheet, width, height, sprite_number, scale_factor,reverse_image):
    x_cor = sprite_number*width
    image = pygame.Surface((width, height),pygame.SRCALPHA, 32)
    image.blit(spritesheet, (0,0), (x_cor-width, 0, x_cor, height))
    image = pygame.transform.scale(image, (width*scale_factor,height*scale_factor))
    if reverse_image == True: image = pygame.transform.flip(image,True,False)
    return image

def loadSprite_y(spritesheet, width, height, sprite_number, scale_factor,reverse_image):
    y_cor = sprite_number*height
    image = pygame.Surface((width, height),pygame.SRCALPHA, 32)
    image.blit(spritesheet, (0,0), (0, y_cor-height, width, y_cor))
    image = pygame.transform.scale(image, (width*scale_factor,height*scale_factor))
    if reverse_image == True: image = pygame.transform.flip(image,True,False)
    return image
