import pygame
from settings import RESOLUTION, BULLET_COLOUR
from player import Player as p
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(BULLET_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (p.pos)
        self.speed = 600
    def update(self, dt, keys_pressed):
        self.rect.x += self.speed * dt
        if self.rect.left == RESOLUTION[0]:
            self.kill()