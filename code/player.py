# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files
from settings import *
from fireball import Fireball


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.width, self.hight = 64, 64
        self.image = image
        self.pos = [i for i in pos]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.status = 'down'
        self.inventory = []
        self.weapon = 'Bare Hands'

    def attack(self, side):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Fireball((self.pos[0] - 28, self.pos[1]), side)
        elif keys[pygame.K_RIGHT]:
            Fireball((self.pos[0] + 64, self.pos[1]), side)
        elif keys[pygame.K_UP]:
            Fireball((self.pos[0], self.pos[1] - 28), side)
        elif keys[pygame.K_DOWN]:
            Fireball((self.pos[0], self.pos[1] + 64), side)

    def walk(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos[1] - 5 > 0:
            self.pos[1] += -5
            self.status = 'up'
        elif keys[pygame.K_s] and self.pos[1] + self.hight + 5 < HEIGHT:
            self.pos[1] += 5
            self.status = 'down'
        else:
            self.pos[1] += 0

        if keys[pygame.K_d] and self.pos[0] + self.width + 5 < WIDTH:
            self.pos[0] += 5
            self.status = 'right'
        elif keys[pygame.K_a] and self.pos[0] - 5 > 0:
            self.pos[0] += -5
            self.status = 'left'
        else:
            self.pos[0] += 0
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self):
        self.walk()
        self.attack(self.status)
