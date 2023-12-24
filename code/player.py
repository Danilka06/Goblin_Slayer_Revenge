# import preinstalled packages
import sys

# import not preinstalled packages
import pygame

# import project files
from settings import *
from main import Game


class Hero(pygame.sprite.Sprite):
    def __init__(self, Game, sheet, columns, rows, pos):
        super().__init__(Game.player_group, Game.all_sprites)
        # self.frames = []
        # self.cut_sheet(sheet, columns, rows)
        # self.cur_frame = 0
        self.image = pygame.draw.rect(Game.screen, (255, 255, 255), ((0, 0), (60, 100)))
        self.rect = self.image.get_rect().move(
            app.tile_width * pos[0] + 15, app.tile_height * pos[1] + 5)
        self.step = (0, 0)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        # if self.step[0]:
        #    self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        #    self.image = self.frames[self.cur_frame]
        self.rect.x += self.step[0]
        self.rect.y += self.step[1]
        if pygame.sprite.spritecollideany(self, Game.tiles_group):
            self.rect.x -= self.step[0]
            self.rect.y -= self.step[1]
        self.step = (0, 0)
