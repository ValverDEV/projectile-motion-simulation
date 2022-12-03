import pygame

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 32)

class ErrorHandler:

    def __init__(self):
        self.activeError = False

    def raiseError(self, text):
        self.activeError = True
        self.text = font.render(text, True, (255, 0, 0))
        self.time = pygame.time.get_ticks()

    def render(self, screen):
        if self.activeError:
            if pygame.time.get_ticks() <= self.time + 2000:
                screen.blit(self.text, (0,70))
            else:
                self.activeError = False