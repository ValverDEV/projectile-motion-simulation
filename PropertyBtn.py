import pygame

pygame.init()

font = pygame.font.Font(pygame.font.get_default_font(), 32)
color = (0,0,0)
green = (35, 224, 112)

class PropertyBtn:

    def __init__(self, name, value, pos, ErrHandler):
        self.name = name
        self.value = value
        self.pos = pos
        self.ErrHandler = ErrHandler

    def render(self, screen):
        text = font.render(f'{self.name}: {self.value}', True, color, green)
        h = text.get_height()
        offset = 10

        if self.pos == 0:
            self.y = 600 - 50 - h - offset
            screen.blit(text, (10 , self.y))

        if self.pos == 1:
            self.y = 600 - 50  + offset
            screen.blit(text, (10 , self.y))

    def valueChange(self, isPlus):

        changeAmount = 1

        if isPlus:
            self.value += changeAmount
            return

        if self.value - changeAmount < 0:
            self.ErrHandler.raiseError(f'{self.name} cannot be negative')
            return
        
        self.value -= changeAmount
