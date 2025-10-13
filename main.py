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
        all_sprites.add(enemy)
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.right, player.rect.centery)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
        keys_pressed = pygame.key.get_pressed()
        SCREEN.fill(BG_COLOUR)
        all_sprites.update(dt, keys_pressed)
        all_sprites.draw(SCREEN)
        hits = pygame.sprite.spritecollide(player, enemies, 1)
        pygame.sprite.groupcollide(bullets, enemies, 1, 1)
        if hits:
            running = False

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()