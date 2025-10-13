import pygame
from settings import RESOLUTION, BULLET_COLOUR
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(BULLET_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.speed = 600
    def update(self, dt, keys_pressed):
        self.rect.x += self.speed * dt
        if self.rect.left > RESOLUTION[0]:
            self.kill()