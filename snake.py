import pygame, sys
import random as rd


# Halllo

#Farben
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,200,0)
PINK=(238,18,137)
ORANGE=(238,69,0)
VIOLETTE=(139,0,139)
BLUE=(0,0,139)

farbenliste=[PINK,ORANGE,VIOLETTE,BLUE]

#Zufallsfarbe




class Fruits:
    def __init__(self, pos =  {'x':10, 'y':10}):
        self.koord = pos
        self.farbe = rd.randint(1, len(farbenliste) - 1)

    def zufallsfarbe(self):

        return farbenliste[self.farbe]

class  Snake:
    def __init__(self):
        self.koord={'x':1,'y':1}
        self.richtung={'dx':0, 'dy':0}

class Spielfeld:
    def __init__(self,groesse):
        self.felder = [[0 for j in range(groesse+1)] for i in range(groesse+1)]

        for i in range(groesse):
            self.felder[-1][i] = 1
            self.felder[groesse][i] = 1
            self.felder[i][-1] = 1
            self.felder[i][groesse] = 1


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
    frucht=Fruits()


    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGHT, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('SNAKE')


    while True:
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type==pygame.KEYDOWN:
                #snake
                if event.key==pygame.K_a:
                    if snake.richtung["dx"]==0:
                        snake.richtung["dx"]=-1
                        snake.richtung["dy"] = 0
                    elif snake.richtung["dx"]==1:
                        snake.richtung["dx"]==0
                        snake.richtung["dy"] = 0
                elif event.key==pygame.K_d:
                    if snake.richtung["dx"]==-1:
                        snake.richtung["dx"]=0
                        snake.richtung["dy"] = 0
                    elif snake.richtung["dx"]==0:
                        snake.richtung["dx"]=1
                        snake.richtung["dy"] = 0
                elif event.key==pygame.K_w:
                    if snake.richtung["dy"]==0:
                        snake.richtung["dy"]=-1
                        snake.richtung["dx"]=0
                    elif snake.richtung["dy"]==1:
                        snake.richtung["dy"]=0
                        snake.richtung["dx"] = 0
                elif event.key==pygame.K_s:
                    if snake.richtung["dy"]==-1:
                        snake.richtung["dy"]=0
                        snake.richtung["dx"] = 0
                    elif snake.richtung["dy"]==0:
                        snake.richtung["dy"]=1
                        snake.richtung["dx"] = 0




        for x in range(0,BOARD_LENGHT,CELLSIZE):
            pygame.draw.line(DISPLAYSURF,BLACK,(x,0),(x,BOARD_LENGHT))

        for y in range(0,BOARD_HIGHT,CELLSIZE):
            pygame.draw.line(DISPLAYSURF,BLACK,(0,y),(BOARD_HIGHT,y))

        #schlange
        if my_feld.felder[snake.koord['x'] + snake.richtung['dx']][snake.koord['y']+snake.richtung['dy']]== 0:
            snake.koord['x'] = snake.koord['x'] + snake.richtung['dx']
            snake.koord['y'] = snake.koord['y'] + snake.richtung['dy']
        else:
            snake.richtung['dy'] = 0
            snake.richtung['dx'] = 0

        make_rectangle_snake(snake.koord, DISPLAYSURF, CELLSIZE)

        #frucht
        make_rectangle_fruit(frucht,DISPLAYSURF,CELLSIZE)



        pygame.display.update()
        FPSCLOCK.tick(FPS)


def board_to_pixel_koord(i,j,width):
    return i*width, j*width


def make_rectangle_snake(dict, display, size):
    x,y=board_to_pixel_koord(dict["x"],dict["y"],size)
    the_rect = pygame.Rect(x,y, size,size)
    pygame.draw.rect(display, GREEN, the_rect)

def make_rectangle_fruit(frucht,display,size):
    x,y=board_to_pixel_koord(frucht.koord["x"],frucht.koord["y"],size)
    the_rect=pygame.Rect(x,y,size,size)
    pygame.draw.rect(display,frucht.zufallsfarbe(),the_rect)




if __name__=="__main__":
    makeGUI()