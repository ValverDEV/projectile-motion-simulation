import pygame

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 32)

class LaunchInfo:

    def __init__(self):
        self.X = 0
        self.theta = 0

    def render(self, screen):
        textX = font.render(f'X = {self.X}', True, (0,0,0))
        textTheta = font.render(f'Theta = {self.theta}', True, (0,0,0))

        h = textX.get_height()

        screen.blit(textX, (0, 0))
        screen.blit(textTheta, (0, 0 + h))
