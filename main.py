import pygame
import numpy as np
from PropertyBtn import PropertyBtn
from UpDownControls import UpDownControls
from ErrorHandler import ErrorHandler
from CalculateBtn import CalculateBtn
from LaunchInfo import LaunchInfo
from Ball import Ball

# Initialize pygame
pygame.init()

# Define game screen
screen = pygame.display.set_mode((800, 600))

ErrHandler = ErrorHandler()

# Problem variables
Y0 = 0
V0 = 20

Y = Y0
V = V0


# UI

# UI background
uiWidth = 800
uiHeigth = 100
uiBG = pygame.Surface((uiWidth, uiHeigth))
uiBG.fill((128,128,128))

# UI Controls

VelocityBtn = PropertyBtn('Velocity', V0, pos = 0, ErrHandler = ErrHandler)
YBtn = PropertyBtn('Y', Y0, pos = 1, ErrHandler = ErrHandler)

VelocityPMbtns = UpDownControls(VelocityBtn)
YPMbtns = UpDownControls(YBtn)

CalcBtn = CalculateBtn(ErrHandler)

Info = LaunchInfo()

Bola = Ball()


# Tower
towerWidth = 25
towerHeight = 600 - uiHeigth
towerPadding = 50
Tower = pygame.Surface((towerWidth, towerHeight))
Tower.fill((0, 0, 0))

# Cannon
cannonImg = pygame.image.load('./assets/cannon.png')
cannonSize = 64
cannonX = 800 - cannonSize - towerWidth - towerPadding
cannonY = 600 - cannonSize - uiHeigth

# Bullseye
bullseyeImg = pygame.image.load('./assets/bullseye.png')
bullseyeImg = pygame.transform.scale(bullseyeImg, (towerWidth, towerWidth))


# Other calculations

cannonRangePXs = 800 - towerPadding - towerWidth - 50 # cannon padding left
cannonRangeMeters = 165

PixelsPerMeter = cannonRangePXs/cannonRangeMeters
print(PixelsPerMeter)
    

def UI():

    # Fixed elements
    screen.blit(uiBG, (0, 600-100))
    screen.blit(Tower, (800 - towerWidth -  towerPadding, 0))
    ErrHandler.render(screen)

    #Dynamic elements
    VelocityBtn.render(screen)
    YBtn.render(screen)
    VelocityPMbtns.render(screen)
    YPMbtns.render(screen)
    CalcBtn.render(screen)

    Y = YBtn.value
    V = VelocityBtn.value

    CalcBtn.Y = Y
    CalcBtn.V = V

    X = CalcBtn.X

    Info.X = X
    Info.theta = CalcBtn.theta

    Info.render(screen)

    targetYDisplacement = towerHeight - towerWidth - Y*PixelsPerMeter
    cannonDisplacement = 800 - towerPadding - towerWidth - X*PixelsPerMeter - 64

    screen.blit(bullseyeImg, (800 - towerPadding -
                towerWidth, targetYDisplacement))

    screen.blit(cannonImg, (cannonDisplacement, cannonY))

    if Bola.isMoving:
        Bola.updatePosition()

    Bola.render(screen)


def checkClick(mouse):
    VelocityPMbtns.checkClick(mouse)
    YPMbtns.checkClick(mouse)
    CalcBtn.checkClick(mouse, Bola)


# Game loop
running = True
while running:

    screen.fill((255,255,255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            checkClick(mouse_pos)

    UI()
    
    pygame.display.update()
