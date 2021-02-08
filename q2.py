import pygame
import sys
from esTxt import draw_text
from colisoes import collisaEsquerdaParedeVertical, collisaDireitaVertical, collisaCimaHorizontal, collisaBaixoHorizontal
from q1 import game


def carto():
    altura = 600
    largura = 1230
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((largura, altura), 0, 32)
    font = pygame.font.SysFont(None, 20)
    font2 = pygame.font.SysFont(None, 70)
    font3 = pygame.font.Font("Gameplay.ttf", 150)
    terrp = pygame.image.load("quart-fer.png")
    terrp = pygame.transform.scale(terrp, (900, 720))
    vel = 10
    anim = 0
    IdleDonw = pygame.image.load("images\spritesTestes\imagem_1.png")
    IdleLeft = pygame.image.load("images\spritesTestes\imagem_4.png")
    IdleUp = pygame.image.load("images\spritesTestes\imagem_7.png")
    IdleRigth = pygame.image.load("images\spritesTestes\imagem_10.png")
    animImgDonw = ["images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_2.png",
                   "images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_3.png"]
    animImgLeft = ["images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_5.png",
                   "images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_6.png"]
    animImgUP = ["images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_8.png",
                 "images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_9.png"]
    animImgRight = ["images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_11.png",
                    "images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_12.png"]
    pos_x = 450 + 20
    pos_y = 500 - 50
    dire = [animImgDonw, animImgLeft, animImgRight, animImgUP]
    çao = 0
    voltar = range(410, 470)
    cara = pygame.image.load("cara_1.png")
    cara = pygame.transform.scale(cara, (60, 70))
    character = pygame.image.load("images\spritesTestes\imagem_4.png")
    screen.blit(terrp, (0, 0))
    screen.blit(character, (pos_x, pos_y))
    running = True
    while running:
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_LEFT]:
            pos_x -= vel
            anim += 1
            çao = 1
            if anim == 4:
                anim = 0
            character = pygame.image.load(animImgLeft[anim])
        if keys[pygame.K_RIGHT]:
            pos_x += vel
            anim += 1
            çao = 2
            if anim == 4:
                anim = 0
            character = pygame.image.load(animImgRight[anim])
        if keys[pygame.K_UP]:
            pos_y -= vel
            anim += 1
            çao = 3
            if anim == 4:
                anim = 0
            character = pygame.image.load(animImgUP[anim])
        if keys[pygame.K_DOWN]:
            pos_y += vel
            anim += 1
            çao = 0
            if anim == 4:
                anim = 0
            character = pygame.image.load(animImgDonw[anim])
        for tel in voltar:
            if pos_y == tel and pos_x == 510:
                running = False
                game()
        if pos_x >= 520:
            pos_x -= 10
        if pos_y <= 120:
            pos_y += 10
        if pos_x <= 180:
            pos_x += 10
        if pos_y >= 520:
            pos_y -= 10
        screen.blit(terrp, (0, 0))
        screen.blit(cara, (290, 230))
        screen.blit(character, (pos_x, pos_y))
        pygame.display.update()
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.update()
