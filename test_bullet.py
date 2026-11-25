import pygame
from player import Bullet, Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

SHOT_DELAY = 1000          # 1 second between player shots
RESPAWN_PROTECTION = 2000  # 2 seconds of safety after respawning
TEST_FIRE_DELAY = 1500     # how often the test target fires (for testing only)

player = Player(380, 540)
bullets = []          # the player's bullets
enemy_bullets = []    # bullets that can hurt the player
lives = 3
last_shot_time = -SHOT_DELAY
invincible_until = 0
game_over = False

# ---- TEST ONLY: a target to shoot at, replace with your colleague's enemies ----
target = pygame.Rect(380, 80, 40, 30)
target_flash_until = 0
last_test_fire = 0

running = True
while running:
    now = pygame.time.get_ticks()

    # ---- input ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            if now - last_shot_time >= SHOT_DELAY:
                bullets.append(Bullet(player.rect.centerx - 2, player.rect.top - 10))
                last_shot_time = now
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            # restart
            player = Player(380, 540)
            bullets = []
            enemy_bullets = []
            lives = 3
            invincible_until = 0
            game_over = False

    if not game_over:
        # ---- movement ----
        player.update()
        for b in bullets:
            b.update()
        for b in enemy_bullets:
            b.update()

        # ---- TEST ONLY: the target fires a bullet straight down ----
        if now - last_test_fire >= TEST_FIRE_DELAY:
            enemy_bullets.append(Bullet(target.centerx - 2, target.bottom, speed=5, color=(255, 80, 80)))
            last_test_fire = now

        # ---- collision: player bullets hit the target ----
        for b in bullets[:]:
            if b.rect.colliderect(target):
                bullets.remove(b)
                target_flash_until = now + 150   # flash to show the hit

        # ---- collision: enemy bullets hit the player ----
        if now >= invincible_until:
            for b in enemy_bullets:
                if b.rect.colliderect(player.rect):
                    lives -= 1
                    enemy_bullets.clear()
                    if lives > 0:  # respawn in the middle with a short safe period
                        player.rect.x = 380
                        invincible_until = now + RESPAWN_PROTECTION
                    else:
                        game_over = True
                    break

        # ---- remove bullets that left the screen ----
        bullets = [b for b in bullets if b.rect.bottom > 0]
        enemy_bullets = [b for b in enemy_bullets if b.rect.top < 600]

    # ---- drawing ----
    screen.fill((0, 0, 0))

    # the player flashes while protected after respawning
    if not game_over and (now >= invincible_until or (now // 100) % 2 == 0):
        player.draw(screen)

    target_colour = (255, 255, 255) if now < target_flash_until else (120, 120, 120)
    pygame.draw.rect(screen, target_colour, target)   # TEST ONLY

    for b in bullets:
        b.draw(screen)
    for b in enemy_bullets:
        b.draw(screen)

    screen.blit(font.render(f"Lives: {lives}", True, (255, 255, 255)), (10, 10))

    if game_over:
        text = font.render("GAME OVER  -  press R to restart", True, (255, 255, 0))
        screen.blit(text, text.get_rect(center=(400, 300)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()