import pygame
import numpy as np
from PropertyBtn import PropertyBtn
from UpDownControls import UpDownControls
from ErrorHandler import ErrorHandler

# Initialize pygame
pygame.init()

# Define game screen
screen = pygame.display.set_mode((800, 600))

ErrHandler = ErrorHandler()


# UI

# UI background
uiWidth = 800
uiHeigth = 100
uiBG = pygame.Surface((uiWidth, uiHeigth))
uiBG.fill((128,128,128))

# UI Controls

VelocityBtn = PropertyBtn('Velocity', 20, pos = 0, ErrHandler = ErrHandler)
YBtn = PropertyBtn('Y', 0, pos = 1, ErrHandler = ErrHandler)

VelocityPMbtns = UpDownControls(VelocityBtn)
YPMbtns = UpDownControls(YBtn)


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



def cannon(x, y):
    screen.blit(cannonImg, (x, y))

def UI():

    # Fixed elements
    screen.blit(uiBG, (0, 600-100))
    screen.blit(Tower, (800 - towerWidth -  towerPadding, 0))
    ErrHandler.render(screen)

    #Dynamic elements
    screen.blit(bullseyeImg, (800 - towerPadding - towerWidth, towerHeight - towerWidth))
    VelocityBtn.render(screen)
    YBtn.render(screen)
    VelocityPMbtns.render(screen)
    YPMbtns.render(screen)

def checkClick(mouse):
    VelocityPMbtns.checkClick(mouse)
    YPMbtns.checkClick(mouse)


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

    cannon(cannonX, cannonY)
    UI()
    
    pygame.display.update()
