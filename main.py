from dinozavr import *

pygame.init()
width = 640
height = 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("DINO")
clock = pygame.time.Clock()
game_end = False
dino = Dino(width, height)
while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

    display.fill((0, 50, 255))
    dino.draw(display)
    pygame.display.update()
pygame.quit()
quit()
