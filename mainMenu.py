import pygame
import pygame.mixer
from screen import Screen
from esTxt import textt


def main_menu():
    seta_px = 190
    seta_py = 300
    pygame.init()
    scren = Screen(600, 1230, 60, (5, 0, 205))
    while True:
        color_text1 = 225, 225, 225
        color_text2 = 225, 225, 225
        if seta_px == 190 and seta_py == 420:
            color_text2 = 106, 20, 245
        if seta_px == 190 and seta_py == 300:
            color_text1 = 106, 20, 245
        seta = pygame.image.load("seta-removebg-preview.png")
        start = textt("Start", (color_text1), scren, 265, 300)
        Opt = textt("Options", (color_text2), scren, 265, 420)
        Tit = textt("O Jogo", (225, 225, 225), scren, 70, 50)
        scren.pint()
        scren.pntEsaMm(seta_px,seta_py)
        scren.des(seta, seta_px, seta_py)
        start.draw_text2()
        Tit.draw_text3()
        Opt.draw_text2()
        scren.atualiEfps()
