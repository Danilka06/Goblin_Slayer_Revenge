# import preinstalled packages

# import not preinstalled packages
import pygame

# import project files


class Entity(pygame.sprite.Sprite):
    """Entity - inherited class for all creatures like player and enemy"""
    def __init__(self, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        """Entity moving and checking for collision"""

        # to fix speed of diagonal moving
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        # self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        # self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        """Collision detection depending on direction"""
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom
