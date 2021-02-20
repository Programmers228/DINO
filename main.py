import random
import os
import sys
import pickle

from Wrench import *
from dinozavr import *
from Kaktusik import *

pygame.init()
cheat = False
if "Hacker228.txt" in os.listdir(sys.path[0]):
    cheat = True

try:
    with open("data.dat", "rb") as file:
        high_score = pickle.load(file)
except:
    high_score = 0
music = pygame.mixer.music.load("Музон.mp3")
pygame.mixer.music.play(-1)
volume = 0.5
width = 640
height = 480
FPS = 340
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("DINO")
clock = pygame.time.Clock()
game_end = False
dino = Dino(width, height)
cactus = [Kaktusik(width, height, (width - 20, height - 60), dino, cheat)]
randomizer = random.randint(300, 340)
font = pygame.font.Font('ALGER.TTF', 45)
pause = False
pause_image = pygame.image.load('PAUSED.png')
gameover_image = pygame.image.load('GAME OVER.png')


def spawn():
    global randomizer
    if cactus[-1].pos[0] + randomizer < width:
        cactus.append(Kaktusik(width, height, (cactus[-1].pos[0] + randomizer, height - 60), dino, cheat))
        randomizer = random.randint(300, 340)


while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pause and not dino.die:
                if not dino.jump:
                    dino.jump = 1
                    dino.speed[1] = -dino.jump_speed
                    print(111)
            if event.key == pygame.K_RETURN:
                pause = not pause and not dino.die
            if event.key == pygame.K_KP_MINUS and volume > 0:
                volume = cround(volume, 0.02, '-')
                pygame.mixer.music.set_volume(volume)
                print(volume)
            if event.key == pygame.K_KP_PLUS and volume < 1:
                volume = cround(volume, 0.02, '+')
                pygame.mixer.music.set_volume(volume)
                print(volume)

    display.fill((0, 50, 255))
    if not pause and not dino.die:
        dino.move()
    dino.draw(display)
    if dino.score > high_score:
        high_score = dino.score
        with open("data.dat", "wb") as file:
            pickle.dump(high_score, file)

    text = font.render(str(dino.score), True, (255, 255, 255))
    textRect = text.get_rect(topright=(width - 10, 5))
    display.blit(text, textRect)

    text2 = font.render("HI " + str(high_score), True, (255, 255, 255))
    textRect2 = text2.get_rect(topright=(width - 10, 45))
    display.blit(text2, textRect2)

    a = []
    for i in cactus:
        i.draw(display)
        if not pause and not dino.die:
            i.move()
        if not (i.pos[0] < 0 or i.pos[0] > width):
            a.append(i)
    cactus = a
    if dino.die:
        display.blit(gameover_image, gameover_image.get_rect(topleft=(width / 2 - 144, height / 2 - 39)))
    if not pause and not dino.die:
        spawn()
    if pause:
        display.blit(pause_image, pause_image.get_rect(topleft=(width / 2 - 144, height / 2 - 39)))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

quit()