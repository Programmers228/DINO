import pygame

image = pygame.image.load("kaktusik.png")

class Kaktusik():
    def __init__(self, width, height, pos, dino, cheat):
        self.image = image
        self.size = (20, 60)
        self.speed = [-1, 0]
        self.width = width
        self.height = height
        self.pos = list(pos)
        self.dino = dino
        self.cheked = False
        self.cheat = cheat

    def draw(self, display):
        display.blit(self.image,self.image.get_rect(topleft=self.pos))

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        if (self.dino.pos[0] >= self.pos[0] and self.dino.pos[0] <= self.pos[0] + self.size[0]) or (self.dino.pos[0] + self.dino.size[0] >= self.pos[0] and self.dino.pos[0] + self.dino.size[0] <= self.pos[0] + self.size[0]):
            if (self.dino.pos[1] >= self.pos[1] and self.dino.pos[1] <= self.pos[1] + self.size[1]) or (self.dino.pos[1] + self.dino.size[1] >= self.pos[1] and self.dino.pos[1] + self.dino.size[1] <=self.pos[1] + self.size[1]):
                if not self.cheat:
                    self.dino.die = True


        if self.dino.pos[0] > self.pos[0] + self.size[0] and not self.cheked:
            self.cheked = True
            self.dino.score += 1