import pygame
from settings import *
from player import Player
from enemy import Enemy
import sys, os
from bullet import Bullet
from settings import RESOLUTION

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
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
    shoot_sound.set_volume(1)
    hit_sound.set_volume(1)
    game_over = False
    while running:
        dt = clock.tick(FPS) / 1000
        if not game_over:
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
            all_sprites.update(dt)
            all_sprites.draw(SCREEN)
            hits = pygame.sprite.spritecollide(player, enemies, 1)
            enemies_hit_by_bullets = pygame.sprite.groupcollide(bullets, enemies, 1, 1)
            for _ in enemies_hit_by_bullets:
                score += 100
                hit_sound.play()
            if hits:
                game_over = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        score_text = font.render(f"Wynik: {score}", 1, PLAYER_COLOUR)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.fill(BG_COLOUR)
        if game_over:
            game_over_font = pygame.font.Font(None, 72)
            game_over_text = game_over_font.render("Koniec Gry!", 1, (255, 0, 0))
            game_over_text_rect = game_over_text.get_rect(center=(RESOLUTION[0] // 2, RESOLUTION[1] // 2))
            SCREEN.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()