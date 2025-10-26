import pygame
from settings import *
from player import Player
from enemy import Enemy
import sys
from bullet import Bullet

pygame.init()
SCREEN
def game():
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Player()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(player)
    for _ in range(5):
        enemy = Enemy()
        enemies.add(enemy)
    all_sprites.add(enemies)
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            bullet = Bullet()
            bullets.add(bullet)
            all_sprites.add(bullets)
        SCREEN.fill(BG_COLOUR)
        all_sprites.update(dt, keys_pressed)
        all_sprites.draw(SCREEN)
        hits = pygame.sprite.spritecollide(player, enemies, 1)
        if hits:
            running = False

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()