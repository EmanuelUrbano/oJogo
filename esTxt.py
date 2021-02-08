import pygame


class textt:
    def __init__(self, texts, color, surface, x, y):
        self.font1 = pygame.font.SysFont(None, 20)
        self.font2 = pygame.font.SysFont(None, 70)
        self.font3 = pygame.font.Font("Gameplay.ttf", 150)
        self.x = x
        self.y = y
        self.texts = texts
        self.surface = surface
        self.color = color

    def draw_text1(self):
        textobj = self.font1.render(self.texts, 1, self.color)
        self.surface.des(textobj, self.x, self.y)

    def draw_text2(self):
        textobj = self.font2.render(self.texts, 1, self.color)
        self.surface.des(textobj, self.x, self.y)

    def draw_text3(self):
        textobj = self.font3.render(self.texts, 1, self.color)
        self.surface.des(textobj, self.x, self.y)
