import pygame
from settings import *
from player import Player
from enemy import Enemy
import sys, os
from bullet import Bullet

pygame.init()
pygame.mixer.init()
SCREEN
def game():
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Player()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(player)
    last_enemy_spawn_time = 0
    ENEMY_SPAWN_COOLDOWN = 1000
    score = 0
    font = pygame.font.Font(None, 40)
    shoot_sound = pygame.mixer.Sound(os.path.join('sfx', 'shoot.wav'))
    hit_sound = pygame.mixer.Sound(os.path.join('sfx', 'hit.wav'))
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
                    shoot_sound.play()
        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn_time > ENEMY_SPAWN_COOLDOWN:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)
            last_enemy_spawn_time = current_time
        SCREEN.fill(BG_COLOUR)
        all_sprites.update(dt)
        all_sprites.draw(SCREEN)
        score_text = font.render(f"Wynik: {score}", 1, PLAYER_COLOUR)
        SCREEN.blit(score_text, (10, 10))
        hits = pygame.sprite.spritecollide(player, enemies, 1)
        enemies_hit_by_bullets = pygame.sprite.groupcollide(bullets, enemies, 1, 1)
        for _ in enemies_hit_by_bullets:
            score += 100
            hit_sound.play()
        if hits:
            running = False

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()