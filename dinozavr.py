import pygame


class Dino():
    def __init__(self, width, height):
        self.image = pygame.image.load("dino.png")
        self.size = (40, 80)
        self.speed = [0, -1]
        self.width = width
        self.height = height
        self.pos = [0, height - self.size[1]]
        self.jump = 0
        self.jump_height = 160
        self.jump_speed = 10
        self.jump_min_speed = 0

    def draw(self, display):
        display.blit(self.image, self.image.get_rect(topleft=self.pos))

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if self.pos[1] >= self.height - self.size[1]:
            self.pos[1] = self.height - self.size[1]
            self.jump = 0
        if self.jump == 1:
            self.speed[1] -= self.jump_min_speed
            print (1)
        if self.pos[1]<self.height -self.jump_height:
            self.speed[1] = -100
            print (2)