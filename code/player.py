# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files
from settings import *
from fireball import Fireball
from entity import Entity


class Player(Entity):
    def __init__(self, pos, groups, image, obstacle_sprites, visible_sprites):
        super().__init__(groups)
        self.image = image
        self.pos = list(pos)

        self.attacking = False
        self.attack_cooldown = 700
        self.attack_time = 0
        self.obstacle_sprites = obstacle_sprites  # obstacle sprites group ( for Entity )
        self.visible_sprites = visible_sprites

        self.width, self.height = TILESIZE, TILESIZE  # player size
        self.rect = self.image.get_rect(topleft=self.pos)
        self.hitbox = self.rect.inflate(0, 0)  # hitbox can be smaller than rect to simulate camera ( for Entity )

        self.speed = 5  # player speed

        self.status = 'down'  # player status ["up", "down", "left", "right", "idle"]
        self.inventory = []
        self.weapon = 'Bare Hands'

    def attack(self):
        if self.available_attack():
            self.attack_time = pygame.time.get_ticks()  # getting the time of the recent attack
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                Fireball((self.visible_sprites,), (self.rect.x - 28, self.rect.y),
                         'left', self.obstacle_sprites)
            elif keys[pygame.K_RIGHT]:
                Fireball((self.visible_sprites,), (self.rect.x + 64, self.rect.y),
                         'right', self.obstacle_sprites)
            elif keys[pygame.K_UP]:
                Fireball((self.visible_sprites,), (self.rect.x, self.rect.y - 28),
                         'up', self.obstacle_sprites)
            elif keys[pygame.K_DOWN]:
                Fireball((self.visible_sprites,), (self.rect.x, self.rect.y + 64),
                         'down', self.obstacle_sprites)

    def available_attack(self):
        # checking if cooldown is over for Fireball
        current_time = pygame.time.get_ticks()

        return current_time - self.attack_time >= self.attack_cooldown

    def input(self):
        """Checking move buttons pressing"""
        keys = pygame.key.get_pressed()

        # movement along axis y
        if keys[pygame.K_w]:
            self.status = 'up'
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.status = 'down'
            self.direction.y = 1
        else:
            self.status = "idle"  # no one button on axis y isn't pressed
            self.direction.y = 0

        # movement along axis x
        if keys[pygame.K_d]:
            self.status = 'right'
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.status = 'left'
            self.direction.x = -1
        else:
            self.status = "idle"  # no one button on axis x isn't pressed
            self.direction.x = 0

    def update(self):
        self.input()
        self.attack()
        self.move(self.speed)
