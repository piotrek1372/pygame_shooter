import pygame
from settings import RESOLUTION, PLAYER_COLOUR

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((300, 400))
        self.image.fill(PLAYER_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.centerx = RESOLUTION[0] // 2
        self.rect.centery = RESOLUTION[1] // 2
        self.pos = pygame.math.Vector2(self.rect.center)
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = 300
    def update(self, dt):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.vel.x = -1
        elif keys_pressed[pygame.K_RIGHT]:
            self.vel.x = 1
        if keys_pressed[pygame.K_UP]:
            self.vel.y = -1
        elif keys_pressed[pygame.K_DOWN]:
            self.vel.y = 1
        else:
            self.vel = pygame.math.Vector2(0, 0)
        self.pos += self.vel * self.speed * dt