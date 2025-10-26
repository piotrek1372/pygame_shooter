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
    enemies = pygame.sprite.Group()
    all_sprites.add(player)
    for _ in range(5):
        enemies.add(enemy)
    all_sprites.add(enemies)
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        SCREEN.fill(BG_COLOUR)
        all_sprites.update(dt)
        all_sprites.draw(SCREEN)
        hits = pygame.sprite.spritecollide(player, enemies, 1)
        if hits:
            running = False

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()