import pygame
from settings import RESOLUTION, ENEMY_COLOUR
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(ENEMY_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(-100, - 50), randint(0, RESOLUTION[1]))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = randint(150, 250)
    def update(self, dt, keys_pressed):
        self.pos.x += self.speed * dt
        self.rect.center = self.pos
        if self.rect.left > RESOLUTION[0]:
            self.kill