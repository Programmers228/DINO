import pygame


class Dino():
    def __init__(self, width, height):
        self.image = pygame.image.load("dino.png")
        self.size = (40, 80)
        self.speed = [0, 0]
        self.width = width
        self.height = height
        self.pos = [0, height - self.size[1]]

    def draw(self, display):
        display.blit(self.image, self.image.get_rect(topleft=self.pos))

    
