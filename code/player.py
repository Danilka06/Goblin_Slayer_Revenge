# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.pos = [i for i in pos]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.status = 'down'
        self.inventory = []
        self.weapon = 'Bare Hands'

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos[1] - 5 > 0:
            self.pos[1] += -5
            self.status = 'up'
        elif keys[pygame.K_s] and self.pos[1] + 5 < HEIGHT:
            self.pos[1] += 5
            self.status = 'down'
        else:
            self.pos[1] += 0

        if keys[pygame.K_d] and self.pos[0] + 5 < WIDTH:
            self.pos[0] += 5
            self.status = 'right'
        elif keys[pygame.K_a] and self.pos[0] - 5 > 0:
            self.pos[0] += -5
            self.status = 'left'
        else:
            self.pos[0] += 0
        self.rect = self.image.get_rect(topleft=self.pos)

