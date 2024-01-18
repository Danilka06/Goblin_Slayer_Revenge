# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image, name):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)  # hitbox can be smaller than rect to simulate camera
