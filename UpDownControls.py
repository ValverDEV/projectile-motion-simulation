import pygame

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 32)
color = (0, 0, 0)
green = (35, 224, 112)

class UpDownControls:

    def __init__(self, target):
        self.target = target

    def render(self, screen):
        plus = font.render(f'+', True, color)
        minus = font.render(f'-', True, color)
        hp = plus.get_height()
        wp = plus.get_width()
        hm = minus.get_height()
        wm = minus.get_width()
        pBG = pygame.Surface((hp, hp))
        mBG = pygame.Surface((hp, hp))
        pBG.fill(green)
        mBG.fill(green)
        pBG.blit(plus, (hp/2 - wp/2, hp/2 - hp/2))
        mBG.blit(minus, (hp/2 - wm/2, hp/2 - hm/2))
        x = 300

        self.plusX = x
        self.minusX = x + 2*hp
        self.sideSize = hp
        self.plusRect = pygame.Rect(self.plusX, self.target.y, hp, hp)
        self.minusRect = pygame.Rect(self.minusX, self.target.y, hp, hp)

        screen.blit(pBG, (self.plusX, self.target.y))
        screen.blit(mBG, (self.minusX, self.target.y))

    def checkClick(self, pos):

        if self.plusRect.collidepoint(pos):
            self.target.valueChange(True)

        if self.minusRect.collidepoint(pos):
            self.target.valueChange(False)