# import preinstalled packages


# import not preinstalled packages
import pygame

# import project files
from settings import *
from code.player import Player


class Level:
    def __init__(self):

        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # player
        self.player = Player()

    def run(self):
        pass
