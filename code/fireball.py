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
            self.direction.y = -1
        elif self.status == 'down':
            self.direction.y = 1
        elif self.status == 'left':
            self.direction.x = -1
        elif self.status == 'right':
            self.direction.x = 1
        self.move(self.speed)

    def collision(self, direction):
        """Collision detection depending on direction"""
        if self.status == 'left' or self.status == 'right':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving left
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving right
                        self.hitbox.left = sprite.hitbox.right

        if self.status == 'up' or self.status == 'down':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving up
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving down
                        self.hitbox.top = sprite.hitbox.bottom
