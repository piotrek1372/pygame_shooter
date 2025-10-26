import pygame
from settings import *
from player import Player
from enemy import Enemy
import sys

pygame.init()
SCREEN
def game():
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Player()
    enemy = Enemy()
    all_sprites.add(player)
    for _ in range(5):
        all_sprites.add(enemy)
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        SCREEN.fill(BG_COLOUR)
        all_sprites.update(dt)
        all_sprites.draw(SCREEN)
        hits = pygame.sprite.spritecollide(player, enemy, 1)
        if hits:
            running = False

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()