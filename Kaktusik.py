import pygame

class Kaktusik():
    def __init__(self, width, height, pos):
        self.image = pygame.image.load("kaktusik.png")
        self.size = (20, 60)
        self.speed = [0, -1]
        self.width = width
        self.height = height
        self.pos = pos
    def draw(self, display):
        display.blit(self.image,self.image.get_rect(topleft=self.pos))
