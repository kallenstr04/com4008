import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((3,3))
        self.image.fill((243,216,63))
        self.rect = self.image.get_rect()

grid = [
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]

class Obstacle:
    def __init__(self,x,y):
        self.blocks_group = pygame.sprite.Group()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    pos_x = x + column * 3
                    pos_y = y + row * 3
                    block = Block()
                    block.rect.topleft = (pos_x, pos_y)
                    self.blocks_group.add(block)

def check_barrier_hits(bullets, obstacles):
    for bullet in bullets:
        for obstacle in obstacles:
            hits = pygame.sprite.spritecollide(bullet, obstacle.blocks_group, True)
            if hits:
                bullet.kill()
                break

obstacles = [Obstacle(100, 450), Obstacle(300, 450), Obstacle(500, 450)]

BLOCK_SIZE = 3
BARRIER_WIDTH = len(grid[0]) * BLOCK_SIZE

num_barriers = 3
barrier_y = SCREEN_HEIGHT - 150
gap = (SCREEN_WIDTH - (num_barriers * BARRIER_WIDTH)) // (num_barriers + 1  )

obstacles = gap + []
for i in range(num_barriers):
    x = gap + i * (BARRIER_WIDTH + gap)
    obstacles.append(Obstacle(x, barrier_y))
obstacles = []
...

while running:
    ...
    for obstacle in obstacles:
        obstacle.blocks_group.draw(screen)   
