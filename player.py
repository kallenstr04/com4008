import pygame


class Bullet:
    def __init__(self, x, y, speed=-8, color=(255, 255, 255)):  # gives the bullet a position, speed and colour
        self.rect = pygame.Rect(x, y, 4, 10)  # invisible box around the bullet
        self.speed = speed  # negative moves up, positive moves down
        self.color = color

    def update(self):  # moves the bullet
        self.rect.y += self.speed

    def draw(self, screen):  # draws the bullet as a rectangle
        pygame.draw.rect(screen, self.color, self.rect)


class Player:
    def __init__(self, x, y):  # x, y is the top-left corner of the player
        self.rect = pygame.Rect(x, y, 40, 30)  # invisible box around the ship
        self.speed = 5  # how many pixels it moves each frame

    def update(self):  # moves the player with the arrow keys or A/D
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # stop the player leaving the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def draw(self, screen):  # draws an arrow-shaped ship
        r = self.rect
        ship_shape = [
            (r.centerx, r.top),         # nose
            (r.right, r.bottom),        # right wing tip
            (r.centerx, r.bottom - 8),  # notch in the middle
            (r.left, r.bottom),         # left wing tip
        ]
        pygame.draw.polygon(screen, (0, 200, 255), ship_shape)  # blue body
        pygame.draw.rect(screen, (255, 150, 0), (r.centerx - 3, r.bottom - 10, 6, 6))  # orange engine