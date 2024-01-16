# import preinstalled packages

# import not preinstalled packages
import pygame


class Fireball(pygame.sprite.Sprite):
    def __init__(self, pos, status):
        super().__init__()
        self.width, self.hight = 34, 18
        self.status = status
        self.image = pygame.image.load("../graphics/test/fireball.png")
        self.pos = [i for i in pos]
        self.rect = self.image.get_rect(topleft=self.pos)

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