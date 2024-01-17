# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files
from entity import Entity


class Fireball(Entity):
    def __init__(self, groups, pos, status, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/fireball.png")
        self.pos = list(pos)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.obstacle_sprites = obstacle_sprites  # obstacle sprites group ( for Entity )
        self.hitbox = self.rect.inflate(0, 0)  # hitbox can be smaller than rect to simulate camera ( for Entity )

        self.speed = 10  # player speed

        self.status = status
        self.width, self.height = 34, 18

    def update(self):
        if self.status == 'up':
            self.pos = (self.pos[0], self.pos[1] - 2)
        elif self.status == 'down':
            self.pos = (self.pos[0], self.pos[1] + 2)
        elif self.status == 'left':
            self.pos = (self.pos[0] - 2, self.pos[1])
        elif self.status == 'right':
            self.pos = (self.pos[0] + 2, self.pos[1])
        self.rect = self.image.get_rect(topleft=self.pos)