import pygame



class Invader(pygame.sprite.Sprite):
    def __init__(self, image, position, points):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.points = points