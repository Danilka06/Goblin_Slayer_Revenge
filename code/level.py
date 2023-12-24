# import preinstalled packages


# import not preinstalled packages
import pygame

# import project files
from settings import *
from code.player import Player
from code.debug import debug
from map.test import level_map
from code.tile import Tile


class Level:
    def __init__(self):

        # get display surface
        self.screen = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # player
        self.player = None

        # create map
        self.create_map()

    def create_map(self):
        for room_index, room in enumerate(level_map):
            for row_index, row in enumerate(room):
                for col_index, col in enumerate(row):
                    x = TILESIZE * col_index
                    y = TILESIZE * row_index + STATS_OFFSET

                    if col == "w":
                        # w - wall
                        Tile((x, y),
                             (self.visible_sprites, self.obstacle_sprites),
                             pygame.image.load("../graphics/test/wall.png"))
                    elif col == "r":
                        # r - rock
                        Tile((x, y),
                             (self.visible_sprites, self.obstacle_sprites),
                             pygame.image.load("../graphics/test/box.png"))
                    elif col == "d":
                        # d - door
                        Tile((x, y),
                             (self.visible_sprites, self.obstacle_sprites),
                             pygame.image.load("../graphics/test/door.png"))
                    elif col == "g":
                        # g - goblin
                        Tile((x, y),
                             (self.visible_sprites),
                             pygame.image.load("../graphics/test/floor.png"))
                    elif col == "p":
                        # p - player
                        Tile((x, y),
                             (self.visible_sprites),
                             pygame.image.load("../graphics/test/floor.png"))

                        self.player = Player((x, y),
                                             (self.visible_sprites, self.obstacle_sprites),
                                             pygame.image.load("../graphics/test/player.png"))
                    else:
                        # floor
                        Tile((x, y),
                             (self.visible_sprites),
                             pygame.image.load("../graphics/test/floor.png"))

    def run(self):
        self.visible_sprites.draw(self.screen)
        self.obstacle_sprites.draw(self.screen)

        # debug(pygame.mouse.get_pos())
