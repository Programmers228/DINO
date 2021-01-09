import random

from dinozavr import *
from Kaktusik import *

pygame.init()
width = 640
height = 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("DINO")
clock = pygame.time.Clock()
game_end = False
dino = Dino(width, height)
cactus = [Kaktusik(width,height,(width-20,height-60))]
def spawn():
    cactus.append(Kaktusik(width,height,(cactus[-1].pos[0]+random.randint(20,30),height-60)))
while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not dino.jump:
                    dino.jump = 1
                    dino.speed[1] = -dino.jump_speed
                    print(111)

    display.fill((0, 50, 255))
    dino.move()
    dino.draw(display)
    for i in cactus:
        i.draw(display)
    pygame.display.update()
    clock.tick(340)
pygame.quit()

quit()
