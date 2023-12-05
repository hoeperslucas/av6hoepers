import pygame
from pygame.locals import *
from random import randint
#from backend.rotas.incluir import insert

pygame.init()
clock = pygame.time.Clock()

# definicoes de variaveis
wscreen = 640
hscreen = 480
xcar = wscreen/2
ycar = hscreen/2
point = 0

# variaveis obstaculos
yob1 = 160
xob1 = 590

yob2 = 160
xob2 = 530

yob3 = 160
xob3 = 470

yob4 = 160
xob4 = 410

yob5 = 160
xob5 = 350

a1 = 3
a2 = 3
a3 = 3
a4 = 3
a5 = 3


def endgame():

    pygame.quit()
    print(f'pontuação final: {point}')


# tela


screen = pygame.display.set_mode((wscreen, hscreen))
pygame.display.set_caption('jojinho')

while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    # controla eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            endgame()
            break

    # estrada
    road = pygame.draw.rect(screen, (255, 255, 255), (0, 160, 640, 160))

    line1 = pygame.draw.line(screen, (255, 255, 255), (0, 140), (640, 140), 5)
    line2 = pygame.draw.line(screen, (255, 255, 255), (0, 340), (640, 340), 5)

    # carro
    car = pygame.draw.rect(screen, (0, 255, 255), (xcar, ycar, 50, 30))

    ob1 = pygame.draw.rect(screen, (0, 0, 255), (xob1, yob1, 50, 30))
    ob2 = pygame.draw.rect(screen, (255, 0, 0), (xob2, yob2, 50, 30))
    ob3 = pygame.draw.rect(screen, (255, 0, 255), (xob3, yob3, 50, 30))
    ob4 = pygame.draw.rect(screen, (0, 255, 0), (xob4, yob4, 50, 30))
    ob5 = pygame.draw.rect(screen, (255, 255, 0), (xob5, yob5, 50, 30))

    xob1 -= a1
    xob2 -= a2
    xob3 -= a3
    xob4 -= a4
    xob5 -= a5

    if car.colliderect(ob1) or car.colliderect(ob2) or car.colliderect(ob3) or car.colliderect(ob4) or car.colliderect(ob5):

        endgame()
        break

    if car.colliderect(line1):
        mup = 0
    else:
        mup = 5

    if car.colliderect(line2):
        mdown = 0
    else:
        mdown = 5

    # randomiza obstaculos
    if xob1 <= -50:
        xob1 = 640
        yob1 = randint(160, 290)
        a1 = randint(1, 5)
        point += 10
    point += 1

    if xob2 <= -50:
        xob2 = 640
        yob2 = randint(160, 290)
        a2 = randint(1, 5)
        point += 10

    if xob3 <= -50:
        xob3 = 640
        yob3 = randint(160, 290)
        a3 = randint(3, 5)
        point += 10

    if xob4 <= -50:
        xob4 = 640
        yob4 = randint(160, 290)
        a4 = randint(3, 6)
        point += 10

    if xob5 <= -50:
        xob5 = 640
        yob5 = randint(160, 290)
        a5 = randint(3, 6)
        point += 10

    # movimentacao vertical
    if pygame.key.get_pressed()[K_w]:
        ycar -= mup

    elif pygame.key.get_pressed()[K_s]:
        ycar += mdown

    # movimentacao horizontal
    if pygame.key.get_pressed()[K_a]:
        xcar -= 10
    elif pygame.key.get_pressed()[K_d]:
        xcar += 2

    pygame.display.update()
