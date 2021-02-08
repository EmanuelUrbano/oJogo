import pygame,sys
from esTxt import textt
def options():
    altura = 600
    largura = 1230
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((largura,altura), 0, 32)
    es=textt("opt",(225,225,225),screen,40,400)
    running = True
    while running:
        screen.fill((0,0,0))
        es.draw_text1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 
        pygame.display.update()
        mainClock.tick(60)