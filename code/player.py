# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files
from settings import *
from fireball import Fireball


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.pos = list(pos)

        self.width, self.height = TILESIZE, TILESIZE
        self.rect = self.image.get_rect(topleft=self.pos)

        self.speed = 5
        self.direction = pygame.math.Vector2()

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

    def input(self):
        keys = pygame.key.get_pressed()

        # movement along axis y
        if keys[pygame.K_w] and self.rect.y - 5 > 0:
            self.status = 'up'
            self.direction.y = -1
        elif keys[pygame.K_s] and self.rect.y + self.height + 5 < HEIGHT:
            self.status = 'down'
            self.direction.y = 1
        else:
            self.status = "idle"
            self.direction.y = 0

        # movement along axis x
        if keys[pygame.K_d] and self.rect.x + self.width + 5 < WIDTH:
            self.status = 'right'
            self.direction.x = 1
        elif keys[pygame.K_a] and self.rect.x - 5 > 0:
            self.status = 'left'
            self.direction.x = -1
        else:
            self.status = "idle"
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)
        self.attack(self.status)
