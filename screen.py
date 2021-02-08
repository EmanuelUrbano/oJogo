import pygame
import sys
from q1 import game
from opt import options


class Screen:
    def __init__(self, altura, largura, fps, cor):
        self.altura = altura
        self.largura = largura
        self.fps = fps
        self.cor = cor

    def criarTel(self):
        pygame.display.set_mode((self.largura, self.altura), 0, 32)

    def atualiEfps(self):
        pygame.time.Clock().tick(self.fps)
        pygame.display.update()

    def pint(self):
        pygame.display.set_mode(
            (self.largura, self.altura), 0, 32).fill(self.cor)

    def des(self, desa, x, y):
        pygame.display.set_mode(
            (self.largura, self.altura), 0, 32).blit(desa, (x, y))

    def pntEsa(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def pntEsaMm(self, seta_px, seta_py):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_e:
                    if seta_px == 190 and seta_py == 300:
                        game()
                    if seta_px == 190 and seta_py == 420:
                        options()
                if event.key == pygame.K_DOWN:
                    seta_py = 420
                if event.key == pygame.K_UP:
                    seta_py = 300
