import pygame
from settings import RESOLUTION, PLAYER_COLOUR

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((300, 400))
        self.image.fill(PLAYER_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 0