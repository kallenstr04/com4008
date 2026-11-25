import pygame
from Barriers import SCREEN_WIDTH, Obstacle

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

barrier = Obstacle(100, 100)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    barrier.blocks_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()