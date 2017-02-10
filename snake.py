import pygame, sys
import random as rd


# Halllo

#Farben
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)

class Fruits:
    def __init__(self, pos =  {'x':10, 'y':10}):
        self.pos = pos

class  Snake:
    def __init__(self):
        self.snake={'x':1,'y':1, 'dx':0, 'dy':0}

class Spielfeld:
    def __init__(self,groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(1, groesse - 1):
            self.felder[i][i] = 1

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse - 1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse - 1] = 1


def makeGUI():


    BOARD_LENGHT = 600
    BOARD_HIGHT = BOARD_LENGHT
    FPS=10
    CELLSIZE=20

    assert BOARD_LENGHT%CELLSIZE==0
    assert BOARD_HIGHT%CELLSIZE==0
    CELLWIDTH=int(BOARD_LENGHT/CELLSIZE)
    CELLHEIGHT=int(BOARD_HIGHT/CELLSIZE)

    my_feld=Spielfeld(CELLWIDTH)

    snake=Snake()


    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGHT, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('SNAKE')


    while True:
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():

            if (event.type==pygame.KEYUP and event.key==pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #snake
                if event.key==pygame.K_w:
                    if snake["dx"]==0:
                        snake["dx"]=-1
                    elif snake["dx"]==1:
                        snake["dx"]==0
                elif event.key==pygame.K_s:
                    if snake["dx"]==-1:
                        snake["dx"]=0
                    elif snake["dx"]==0:
                        snake["dx"]=1
                elif event.key==pygame.K_a:
                    if snake["dy"]==0:
                        snake["dy"]=-1
                    elif snake["dy"]==1:
                        snake["dy"]=0
                elif event.key==pygame.K_d:
                    if snake["dy"]==-1:
                        snake["dy"]=0
                    elif snake["dy"]==0:
                        snake["dy"]=1




        for x in range(0,BOARD_LENGHT,CELLSIZE):
            pygame.draw.line(DISPLAYSURF,BLACK,(x,0),(x,BOARD_LENGHT))

        for y in range(0,BOARD_HIGHT,CELLSIZE):
            pygame.draw.line(DISPLAYSURF,BLACK,(0,y),(BOARD_HIGHT,y))




        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=="__main__":
    makeGUI()