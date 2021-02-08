import pygame
import sys
from screen import Screen


def GUI():
    scren =  Screen( 600,1230,60,(5, 0, 205))
    o = True
    while o:
        scren.pint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    o = False
        scren.atualiEfps()
