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

farbenliste=[PINK,ORANGE,VIOLETTE,BLUE,GREEN,BLACK]

CELLWIDTH = 0





class Fruits:
    def __init__(self, pos =  {'x':rd.randint(0,29), 'y':rd.randint(0,29)}):
        self.koord = pos
        self.farbe = rd.randint(1, len(farbenliste) - 1)

    def zufallsfarbe(self):
        return farbenliste[self.farbe]

    def frucht_neupos(self,pos = None):
        if pos is None:
            pos = {'x': rd.randint(0, 29), 'y': rd.randint(0, 29)}

        self.koord=pos
        self.farbe = rd.randint(1, len(farbenliste) - 1)




class  Snake:
    def __init__(self):
        self.körperteile = [{'x':rd.randint(3,27),'y':rd.randint(3,27)}]
        self.richtung={'dx':0, 'dy':0}




    def körper_hinzufügen(self):
        x = self.körperteile[0]['x'] + self.richtung['dx']
        y = self.körperteile[0]['y'] + self.richtung['dy']
        nechst = {'x': x, 'y': y}
        self.körperteile.insert(0,nechst)


    def update(self):
        x = self.körperteile[0]['x'] + self.richtung['dx']
        y = self.körperteile[0]['y'] + self.richtung['dy']
        nechst = {'x':x,'y':y}
        for i in range(len(self.körperteile)):
            tmp = self.körperteile[i]
            self.körperteile[i] = nechst
            nechst = tmp



class Spielfeld:
    def __init__(self,groesse):
        self.felder = [[0 for j in range(groesse+1)] for i in range(groesse+1)]

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse] = 1







def makeGUI():

    BOARD_LENGHT = 600
    BOARD_HIGHT = BOARD_LENGHT
    FPS = 5
    CELLSIZE = 20

    assert BOARD_LENGHT % CELLSIZE == 0
    assert BOARD_HIGHT % CELLSIZE == 0
    CELLWIDTH = int(BOARD_LENGHT / CELLSIZE)
    CELLHEIGHT = int(BOARD_HIGHT / CELLSIZE)



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

                elif event.key==pygame.K_a:
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

        snake.update()

        #Spielablauf

        if snake.körperteile[0]==frucht.koord:
            snake.körper_hinzufügen()
            frucht.frucht_neupos()

        for i in snake.körperteile[1:]:
            if snake.körperteile[0]==i:
                pygame.quit()
                sys.exit()



        for körperteil in snake.körperteile:
            make_rectangle_snake(körperteil, DISPLAYSURF, CELLSIZE)



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