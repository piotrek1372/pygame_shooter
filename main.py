import pygame
from settings import *
from player import Player
import sys

pygame.init()
SCREEN
def game():
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        SCREEN.fill(BG_COLOUR)
        all_sprites.update(dt)
        all_sprites.draw(SCREEN)

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()