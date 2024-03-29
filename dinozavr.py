#импорт модулей
import pygame

class Dino():
    def __init__ (self, width, height):
#    ===================Настройки===================
        self.image1 = pygame.image.load("dino1.png")
        self.image2 = pygame.image.load("dino2.png")
        self.image = self.image1
        self.size = (40, 80)
        self.speed = [0, 1]
        self.width = width
        self.height = height
        self.pos = [40  , height - self.size[1]]
        self.jump = 0
        self.jump_height = 120
        self.jump_speed = 1
        self.jump_min_speed = 0.001
        self.score = 0
        self.die = False

# функцыя "draw"
    def draw(self, display):
        display.blit(self.image, self.image.get_rect(topleft=self.pos))

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if self.pos[1] >= self.height - self.size[1]:
            self.pos[1] = self.height - self.size[1]
            self.jump = 0
        elif self.jump == 1:
            self.speed[1] += self.jump_min_speed
            print (2)
        if self.pos[1]+self.size[1]<self.height-self.jump_height:
            self.speed[1] = 1
            print (3)
        if self.jump:
            self.image = self.image2
        else:
            self.image = self.image1
        if self.die:
            print ("dino.die")