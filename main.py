import random

from dinozavr import *
from Kaktusik import *

pygame.init()

music = pygame.mixer.music.load("Музон.mp3")
pygame.mixer.music.play(-1)

width = 640
height = 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("DINO")
clock = pygame.time.Clock()
game_end = False
dino = Dino(width, height)
cactus = [Kaktusik(width,height,(width-20,height-60), dino)]
font = pygame.font.Font('ALGER.TTF', 45)
pause = False
pause_image = pygame.image.load('PAUSED.png ')


def spawn():
    cactus.append(Kaktusik(width,height,(cactus[-1].pos[0]+random.randint(300,340),height-60), dino))
while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dino.jump:
                    dino.jump = 1
                    dino.speed[1] = -dino.jump_speed
                    print(111)
            if event.key == pygame.K_RETURN:
                pause = not pause


    display.fill((0, 50, 255))
    if not pause:
        dino.move()
    dino.draw(display)
    text = font.render(str(dino.score), True, (255,255,255))
    textRect = text.get_rect(topright = (width-10, 5))
    display.blit(text, textRect)

    a=[]
    for i in cactus:
        i.draw(display)
        if not pause:
            i.move()
        if not (i.pos[0] < 0 or i.pos[0] > width):
            a.append(i)
    cactus = a
    if dino.die:
        game_end = True
    if not pause:
        spawn()
    if pause:
        display.blit(pause_image,pause_image.get_rect(topleft=(width/2-144,height/2-39)))
    pygame.display.update()
    clock.tick(340)
pygame.quit()

quit()
