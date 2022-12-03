import pygame
import numpy as np

pygame.init()

PxM = 4.09

class Ball:

    def __init__(self):
        self.show = False
        self.D = 10
        self.Y0 = 600 - 100 - self.D*3
        self.X0 = 800
        self.Y = self.Y0
        self.X = self.X0
        self.T0 = 0
        self.isMoving = False


    def updatePosition(self):
        t = pygame.time.get_ticks()/1000
        if self.isMoving:

            theta = self.theta * np.pi/180
            Vx = self.V * np.cos(theta)
            Vy = self.V * np.sin(theta)

            self.X = (self.X0 + Vx* PxM * (t - self.T0))
            self.Y = self.Y0 - Vy * PxM * (t - self.T0) + 0.5 * 9.81 * (t - self.T0)**2*PxM

        if self.Y >= 800 - 25:
            self.isMoving = False
            self.show = False

    def shoot(self, X0, V, theta):
        self.show = True
        self.isMoving = True
        self.T0 = pygame.time.get_ticks()/1000
        # cannonDisplacement = 800 - towerPadding - towerWidth - X*PixelsPerMeter - 64
        self.X0 = 800 - 50 - 25 - X0*PxM - self.D
        self.V = V
        self.theta = theta

        print(self.X0)

    def render(self, screen):
        if self.show:
            pygame.draw.circle(screen, (255, 0, 0), (self.X, self.Y), self.D)
