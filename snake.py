import pygame, sys

#Farben
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)

class Fruits:
    def __init__(self, pos =  {'x':10, 'y':10}):
        self.pos = pos

class  Snake:
    def __init__(self):
        self.snake={'x':300,'y':300, 'dx':0, 'dy':0}

class Spielfeld:
    def __init__(self,groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]


def makeGUI():

    BOARD_LENGHT = 600
    BOARD_HIGHT = BOARD_LENGHT
    FPS=10
    CELLSIZE=20

    assert BOARD_LENGHT%CELLSIZE==0
    assert BOARD_HIGHT%CELLSIZE==0

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGHT, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('SNAKE')



