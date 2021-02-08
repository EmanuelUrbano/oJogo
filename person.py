import pygame

class per:
    def __init__(self, sprtsParadC, sprtsAndndC, sprtsParadB, sprtsAndndB, sprtsParadE, sprtsAndndE, sprtsParadD, sprtsAndndD, pos_x, pos_y, vel,spriteA):
        self.sprtParadC = sprtsParadC
        self.sprtsAndndC = sprtsAndndC
        self.sprtParadB = sprtsParadB
        self.sprtsAndndB = sprtsAndndB
        self.sprtParadE = sprtsParadE
        self.sprtsAndndE = sprtsAndndE
        self.sprtParadD = sprtsParadD
        self.sprtsAndndD = sprtsAndndD
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = vel
        self.anim = 0
        self.dire = [self.sprtsAndndB, self.sprtsAndndE,
                     self.sprtsAndndD, self.sprtsAndndC]
        self.cao = 0
        self.spriteA = pygame.image.load(spriteA)

    def andar(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.pos_x -= self.vel
            self.anim += 1
            self.cao = 1
            if self.anim == 4:
                self.anim = 0
            self.spriteA = pygame.image.load(self.sprtsAndndE[self.anim])
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.pos_x += self.vel
            self.anim += 1
            self.cao = 2
            if self.anim == 4:
                self.anim = 0
            self.spriteA = pygame.image.load(self.sprtsAndndD[self.anim])
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.pos_y -= self.vel
            self.anim += 1
            self.cao = 3
            if anim == 4:
                anim = 0
            self.spriteA = pygame.image.load(self.sprtsAndndC[self.anim])
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.pos_y += self.vel
            anim += 1
            self.anim = 0
            if self.anim == 4:
                self.anim = 0
            self.spriteA = pygame.image.load(self.sprtsAndndB[self.anim])
