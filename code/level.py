# import preinstalled packages


# import not preinstalled packages
import pygame

# import project files
from settings import *
from code.player import Player
from code.debug import debug
from map.test import level_map
from code.tile import Tile
from code.random_map import RandomMap


class Level:
    def __init__(self):

        # get display surface
        self.screen = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # player
        self.player = None

        # cheat code
        self.cheat_code_activated = False

        # create map
        self.create_map()

    def create_map(self):
        TILE_SETTING = {
            "w": [(self.visible_sprites, self.obstacle_sprites),
                  pygame.image.load("../graphics/test/wall.png")],
            "r": [(self.visible_sprites, self.obstacle_sprites),
                  pygame.image.load("../graphics/test/box.png")],
            "d": [(self.visible_sprites, self.obstacle_sprites),
                  pygame.image.load("../graphics/test/door.png")],
            "g": [(self.visible_sprites),
                  pygame.image.load("../graphics/test/floor.png")],
            "p": [(self.visible_sprites, self.obstacle_sprites),
                  pygame.image.load("../graphics/test/player.png")]
        }

        self.map_object = RandomMap()
        self.map = self.map_object.map

        self.map[4][1] = "p"

        # for room_index, room in enumerate(self.map):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                x = TILESIZE * col_index
                y = TILESIZE * row_index + STATS_OFFSET

                if col in TILE_SETTING.keys():
                    if col == "p":
                        player_position = (x, y)
                        Tile((x, y), *TILE_SETTING["g"])
                    else:
                        Tile((x, y), *TILE_SETTING[col])
                else:
                    Tile((x, y), *TILE_SETTING["g"])

        self.player = Player(player_position, *TILE_SETTING["p"])

    def cheat_code(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHTBRACKET]:
            self.cheat_code_activated = True

        if self.cheat_code_activated:
            debug(pygame.mouse.get_pos())

    def run(self):
        # player
        self.player.update()

        # sprite groups draw
        self.visible_sprites.draw(self.screen)
        self.obstacle_sprites.draw(self.screen)

        # cheat code
        self.cheat_code()
        # debug(pygame.mouse.get_pos())
