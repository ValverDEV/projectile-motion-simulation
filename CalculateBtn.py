import pygame
from maximize import maximize_x

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 32)
color = (0, 0, 0)
green = (35, 224, 112)

class CalculateBtn:

    def __init__(self, ErrHandler):
        self.ErrHandler = ErrHandler
        self.X = 0
        self.theta = 0 

    def render(self, screen):
        text = font.render('Calculate & Shoot', True, color, green)
        h = text.get_height()
        
        self.h = h
        self.w = text.get_width()

        self.x = 800 - 300
        self.y = 600 - 50 - h/2

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        screen.blit(text, (self.x, self.y))

    def maximize(self):
        self.X, self.theta = maximize_x(self.V, self.Y)

    def checkSolution(self):
        if self.V**2 > 2*9.81*self.Y:
            return True
        
        self.ErrHandler.raiseError('No solution, V^2 > 2*g*Y is necessary')

    def checkClick(self, pos):

        if self.rect.collidepoint(pos):
            if self.checkSolution():
                self.maximize()
