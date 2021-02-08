import pygame
import sys
from esTxt import textt
from colisoes import *
from GUI import GUI


def game():
    altura = 600
    largura = 1230
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((largura, altura), 0, 32)

    vel = 10
    anim = 0
    home = pygame.image.load("images\home.png")
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
    pos_x = 340
    pos_y = 130
    vida = 30
    vidaS = "Vida: "
    dire = [animImgDonw, animImgLeft, animImgRight, animImgUP]
    çao = 0
    character = pygame.image.load("images\spritesTestes\imagem_1.png")
    screen.blit(home, (0, 0))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_m:
                    GUI()
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
        if pos_x >= 640:
            pos_x -= 10
        if pos_y >= 420:
            pos_y -= 10
        if pos_x <= 30:
            pos_x += 10
        if pos_y <= 70:
            pos_y += 10
        pos_y = collisaCimaHorizontal(40, 310, 330, pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(340, 360, 250, pos_x, pos_y)
        pos_y = collisaCimaHorizontal(200, 250, 360, pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(340, 380, 210, pos_x, pos_y)
        pos_y = collisaCimaHorizontal(160, 210, 380, pos_x, pos_y)
        pos_x = collisaDireitaVertical(340, 390, 150, pos_x, pos_y)
        pos_y = collisaCimaHorizontal(40, 80, 380, pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(240, 330, 310, pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(340, 360, 110, pos_x, pos_y)
        screen.blit(home, (0, 0))
        EscrV = textt(vidaS+"{}".format(vida), (225, 225, 225), screen, 30, 30)
        EscrV.draw_text1()
        screen.blit(character, (pos_x, pos_y))
        pygame.display.update()
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.update()
