import pygame, sys
import random as rd
import os

# Farben
WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
GREEN   = (  0, 200,   0)
PINK    = (238,  18, 137)
ORANGE  = (238,  69,   0)
VIOLETTE= (139,   0, 139)
BLUE    = (  0,   0, 139)
BLUE2   = (  0,   0, 255)
CYAN    = (  0, 255, 255)
BROWN   = (139,  69,  19)
BROWN1  = (210, 105,  30)
GREY    = (119, 136, 153)
GREY1   = ( 92,  92,  92)
GREEN2  = (  0, 100,   0)
GREEN3  = (202, 255, 112)
GREEN4  = ( 34, 139,  34)
GREEN5  = (124, 252,   0)
ORANGE1 = (255, 140,   0)
ORANGE2 = (250, 128, 114)
RED     = (255,   0,   0)
RED1    = (205,   0,   0)
VIOLET1 = (255,   0, 255)
GELB    = (255, 215,   0)
GELB1   = (255, 255,   0)
VIOLET2 = (178,  58, 238)

farbenliste = [PINK, ORANGE, VIOLETTE, BLUE, BLUE2, CYAN, BROWN, BROWN1, GREY, GREY1, GREEN2, GREEN3, GREEN4, GREEN5, ORANGE1, ORANGE2, RED, RED1, VIOLET1, VIOLET2, GELB, GELB1]

CELLWIDTH = 0


class Fruits:
    def __init__(self, pos={'x': rd.randint(2, 27), 'y': rd.randint(2, 27)}):  # Liste mit der ersten Frucht
        self.koord = pos
        self.farbe = rd.randint(1, len(farbenliste) - 1)

    def zufallsfarbe(self):  # Zufällige farbe der Frucht
        return farbenliste[self.farbe]

    def frucht_neupos(self, pos=None):  # funktion für eine neue frucht, wenn die verherige gefressen wurde
        if pos is None:
            pos = {'x': rd.randint(3, 26), 'y': rd.randint(3, 26)}

        self.koord = pos
        self.farbe = rd.randint(1, len(farbenliste) - 1)


class Snake:
    def __init__(self):
        self.körperteile = [{'x': rd.randint(3, 27), 'y': rd.randint(3,
                                                                     27)}]  # liste der Körperteile mit zufallsvariabel für den ersten Körper teil
        self.richtung = {'dx': 0, 'dy': 0}  # richting der Schlange

    def körper_hinzufügen(self):  # funktion um einen neuen Körper hinzuzufügen
        x = self.körperteile[0]['x'] + self.richtung['dx']
        y = self.körperteile[0]['y'] + self.richtung['dy']
        nechst = {'x': x, 'y': y}
        self.körperteile.insert(0, nechst)

    def update(self):  # fügt neues körperteil hinzu, updated die Liste
        x = self.körperteile[0]['x'] + self.richtung['dx']
        y = self.körperteile[0]['y'] + self.richtung['dy']
        nechst = {'x': x, 'y': y}
        for i in range(len(self.körperteile)):
            tmp = self.körperteile[i]
            self.körperteile[i] = nechst
            nechst = tmp


class Spielfeld:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse + 1)] for i in range(groesse + 1)]  # Spielfeld

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse - 1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse - 1] = 1


class Button:

    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, WHITE, (x,y,length,height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print ("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False



class File:

        def __init__(self):
            #self.a=open('Ergebnisse','a')
            pass




        def write(self, name, punkte):

            #self.a.close()
            try:
                self.fout=open('Ergebnisse','r+')
            except:
                self.fout=open('Ergebnisse','a')
                self.fout.write(name)
            else:
                if os.stat("Ergebnisse").st_size==0:
                    self.fout.write(name)
                else:
                    for line in self.fout:
                        tmp=line.split(":")
                        zahl=int(tmp[1])
                        print(tmp)

                        if zahl<punkte:
                            pass
                            print("Drin")
                        else:
                            print(punkte)
                            print("im else")
                            self.fout.write(name)
                            break

        def beenden(self):
            self.fout.close()






def makemenu(DISPLAYSURF):

    pygame.display.set_caption('MENU')

    DISPLAYSURF.fill(WHITE)


    spielbutton = Button()
    spielbutton.create_button(DISPLAYSURF, GREEN, 50, 50, 150, 50, 0, "Spiel", BLACK)

    rangbutton = Button()
    rangbutton.create_button(DISPLAYSURF, GREEN, 300, 50, 150, 50, 0, "Liste", BLACK)

    mehrspielbutton = Button()  # neu
    mehrspielbutton.create_button(DISPLAYSURF, GREEN, 50, 200, 150, 50, 0, "1 vs. 1", BLACK)  # neu

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:  # Definition ESC Taste
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()



        elif event.type == pygame.MOUSEBUTTONDOWN:
            if spielbutton.pressed(pygame.mouse.get_pos()):
                return False,True,False

            elif mehrspielbutton.pressed(pygame.mouse.get_pos()):
                return False,False,True

    return True,False,False



def makeend(DISPLAYSURF,punkte):

    pygame.display.set_caption('ENDE')

    punkte=punkte



    print("Done")


    DISPLAYSURF.fill(WHITE)



    if punkte!=0:
        speicherkommentar=Button()
        speicherkommentar.create_button(DISPLAYSURF,GREEN,200,200,400,200,0,"Name in Console",BLACK)
        pygame.display.update()

        punktespeichern(punkte)





    else:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:  # Definition ESC Taste
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    return False, True

    return True, False






def makegame():
    GANZE_LAENGE=800
    BOARD_LENGHT = 600
    BOARD_HIGHT = BOARD_LENGHT
    FPS = 8
    CELLSIZE = 20

    assert BOARD_LENGHT % CELLSIZE == 0
    assert BOARD_HIGHT % CELLSIZE == 0
    CELLWIDTH = int(BOARD_LENGHT / CELLSIZE)

    my_feld = Spielfeld(CELLWIDTH)


    punkte=0
    punkte2=0

    snake = Snake()
    snake2=Snake()
    frucht = Fruits()

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((GANZE_LAENGE, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('SNAKE')


    isMenu = True

    isEnd=False

    isGame=False

    is1vs1=False

    while True:

        if isMenu:
            isMenu, isGame, is1vs1 = makemenu(DISPLAYSURF)

        elif isEnd:
            isEnd, isMenu = makeend(DISPLAYSURF,punkte)


        elif isGame:
            DISPLAYSURF.fill(WHITE)


            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:  # Definition ESC Taste
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    elif event.key == pygame.K_a:  # Steuerung schlange 1
                        if snake.richtung["dx"] == 0:
                            snake.richtung["dx"] = -1
                            snake.richtung["dy"] = 0
                        elif snake.richtung["dx"] == 1:
                            snake.richtung["dx"] == 0
                            snake.richtung["dy"] = 0

                    elif event.key == pygame.K_d:
                        if snake.richtung["dx"] == -1:
                            snake.richtung["dx"] = 0
                            snake.richtung["dy"] = 0
                        elif snake.richtung["dx"] == 0:
                            snake.richtung["dx"] = 1
                            snake.richtung["dy"] = 0

                    elif event.key == pygame.K_w:
                        if snake.richtung["dy"] == 0:
                            snake.richtung["dy"] = -1
                            snake.richtung["dx"] = 0
                        elif snake.richtung["dy"] == 1:
                            snake.richtung["dy"] = 0
                            snake.richtung["dx"] = 0

                    elif event.key == pygame.K_s:
                        if snake.richtung["dy"] == -1:
                            snake.richtung["dy"] = 0
                            snake.richtung["dx"] = 0
                        elif snake.richtung["dy"] == 0:
                            snake.richtung["dy"] = 1
                            snake.richtung["dx"] = 0



            # Rand wird gezeichnet

            for i in range(len(my_feld.felder)):
                for j in range(len(my_feld.felder[i])):
                    if my_feld.felder[i][j] == 1:
                        x, y = board_to_pixel_koord(i, j, CELLSIZE)
                        appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
                        pygame.draw.rect(DISPLAYSURF, BLACK, appleRect)

            snake.update()

            for x in range(0, BOARD_LENGHT, CELLSIZE):  # zeichnet senkrechte lienien
                pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, BOARD_LENGHT))

            for y in range(0, BOARD_HIGHT, CELLSIZE):  # zeichnet horizontale lienien
                pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (BOARD_HIGHT, y))

            # Spielablauf

            punktezahl = Button()
            punktezahl.create_button(DISPLAYSURF, WHITE, 650, 100, 150, 60, 0, str(punkte), BLACK)

            if snake.körperteile[
                0] == frucht.koord:  # wenn eine frucht gegessen wird, wird hier eine neue frucht aufgerufen
                snake.körper_hinzufügen()
                frucht.frucht_neupos()
                punkte += 1
                print(punkte)

            for i in snake.körperteile[1:]:  # wenn die schlange mit sich selbst kollidiert esc spiel
                if snake.körperteile[0] == i:
                    snake=Snake()

                    isEnd=True

            for körperteil in snake.körperteile:
                make_rectangle_snake(körperteil, DISPLAYSURF, CELLSIZE,GREEN)

            # frucht
            make_rectangle_fruit(frucht, DISPLAYSURF, CELLSIZE)

            # Snake wird von Rand gestopt

            for i in range(len(my_feld.felder)):
                for j in range(len(my_feld.felder[i])):
                    if my_feld.felder[i][j] == 1:
                        randliste = {'x': i, 'y': j}
                        if randliste == snake.körperteile[0]:
                            snake = Snake()

                            isEnd=True

        elif is1vs1:

            DISPLAYSURF.fill(WHITE)

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:  # Definition ESC Taste
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    elif event.key == pygame.K_a:  # Steuerung schlange 1
                        if snake.richtung["dx"] == 0:
                            snake.richtung["dx"] = -1
                            snake.richtung["dy"] = 0
                        elif snake.richtung["dx"] == 1:
                            snake.richtung["dx"] == 0
                            snake.richtung["dy"] = 0

                    elif event.key == pygame.K_d:
                        if snake.richtung["dx"] == -1:
                            snake.richtung["dx"] = 0
                            snake.richtung["dy"] = 0
                        elif snake.richtung["dx"] == 0:
                            snake.richtung["dx"] = 1
                            snake.richtung["dy"] = 0

                    elif event.key == pygame.K_w:
                        if snake.richtung["dy"] == 0:
                            snake.richtung["dy"] = -1
                            snake.richtung["dx"] = 0
                        elif snake.richtung["dy"] == 1:
                            snake.richtung["dy"] = 0
                            snake.richtung["dx"] = 0

                    elif event.key == pygame.K_s:
                        if snake.richtung["dy"] == -1:
                            snake.richtung["dy"] = 0
                            snake.richtung["dx"] = 0
                        elif snake.richtung["dy"] == 0:
                            snake.richtung["dy"] = 1
                            snake.richtung["dx"] = 0

                    elif event.key == pygame.K_LEFT:  # Steuerung schlange 2 alles neu
                        if snake2.richtung["dx"] == 0:
                            snake2.richtung["dx"] = -1
                            snake2.richtung["dy"] = 0
                        elif snake2.richtung["dx"] == 1:
                            snake2.richtung["dx"] == 0
                            snake2.richtung["dy"] = 0

                    elif event.key == pygame.K_RIGHT:
                        if snake2.richtung["dx"] == -1:
                            snake2.richtung["dx"] = 0
                            snake2.richtung["dy"] = 0
                        elif snake2.richtung["dx"] == 0:
                            snake2.richtung["dx"] = 1
                            snake2.richtung["dy"] = 0

                    elif event.key == pygame.K_UP:
                        if snake2.richtung["dy"] == 0:
                            snake2.richtung["dy"] = -1
                            snake2.richtung["dx"] = 0
                        elif snake2.richtung["dy"] == 1:
                            snake2.richtung["dy"] = 0
                            snake2.richtung["dx"] = 0

                    elif event.key == pygame.K_DOWN:
                        if snake2.richtung["dy"] == -1:
                            snake2.richtung["dy"] = 0
                            snake2.richtung["dx"] = 0
                        elif snake2.richtung["dy"] == 0:
                            snake2.richtung["dy"] = 1
                            snake2.richtung["dx"] = 0

            # Rand wird gezeichnet

            for i in range(len(my_feld.felder)):
                for j in range(len(my_feld.felder[i])):
                    if my_feld.felder[i][j] == 1:
                        x, y = board_to_pixel_koord(i, j, CELLSIZE)
                        appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
                        pygame.draw.rect(DISPLAYSURF, BLACK, appleRect)

            # Snake wird von Rand gestopt

            for i in range(len(my_feld.felder)):
                for j in range(len(my_feld.felder[i])):
                    if my_feld.felder[i][j] == 1:
                        randliste = {'x': i, 'y': j}
                        if randliste == snake.körperteile[0]:
                            snake=Snake()
                            snake2=Snake()
                            punkte = 0
                            punkte2=0
                            isEnd=True
                        elif randliste == snake2.körperteile[0]:
                            snake=Snake()
                            snake2=Snake()
                            punkte = 0
                            punkte2 = 0
                            isEnd=True
            snake2.update()
            snake.update()

            for x in range(0, BOARD_LENGHT, CELLSIZE):  # zeichnet senkrechte lienien
                pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, BOARD_LENGHT))

            for y in range(0, BOARD_HIGHT, CELLSIZE):  # zeichnet horizontale lienien
                pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (BOARD_HIGHT, y))

            # Spielablauf

            punktezahl = Button()
            punktezahl.create_button(DISPLAYSURF, WHITE, 650, 100, 150, 60, 0, str(punkte), BLACK)

            punktezahl2 = Button()
            punktezahl2.create_button(DISPLAYSURF, WHITE, 650, 300, 150, 60, 0, str(punkte2), BLACK)

            if snake.körperteile[
                0] == frucht.koord:  # wenn eine frucht gegessen wird, wird hier eine neue frucht aufgerufen
                snake.körper_hinzufügen()
                frucht.frucht_neupos()
                punkte += 1
                print(punkte)

            elif snake2.körperteile[0] == frucht.koord:
                snake2.körper_hinzufügen()
                frucht.frucht_neupos()
                punkte2 += 1
                print(punkte2)

            for i in snake.körperteile[1:]:  # wenn die schlange mit sich selbst kollidiert esc spiel
                if snake.körperteile[0] == i:
                    snake = Snake()
                    snake2 = Snake()
                    punkte = 0
                    punkte2 = 0
                    isEnd = True

            for i in snake2.körperteile[1:]:  # wenn die schlange mit sich selbst kollidiert esc spiel
                if snake2.körperteile[0] == i:
                    snake = Snake()
                    snake2 = Snake()
                    punkte = 0
                    punkte2 = 0
                    isEnd = True

            for i in snake.körperteile[0:]:
                if snake2.körperteile[0] == i:
                    snake = Snake()
                    snake2 = Snake()
                    isEnd = True
            for i in snake2.körperteile[0:]:
                if snake.körperteile[0] == i:
                    snake = Snake()
                    snake2 = Snake()
                    punkte = 0
                    punkte2 = 0
                    isEnd = True

            for körperteil in snake.körperteile:
                make_rectangle_snake(körperteil, DISPLAYSURF, CELLSIZE, GREEN)

            for körperteil in snake2.körperteile:
                make_rectangle_snake(körperteil, DISPLAYSURF, CELLSIZE, CYAN)
            # frucht
            make_rectangle_fruit(frucht, DISPLAYSURF, CELLSIZE)





        pygame.display.update()
        FPSCLOCK.tick(FPS)






def punktespeichern(zahl):
    tabelle=File()
    name=input("Gebe deinen Namen ein:")

    tabelle.write(name+ ":" + str(zahl) + ":\n",zahl)

    tabelle.beenden()


def board_to_pixel_koord(i, j, width):
    return i * width, j * width


def make_rectangle_snake(dict, display, size,color):
    x, y = board_to_pixel_koord(dict["x"], dict["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, color, the_rect)


def make_rectangle_fruit(frucht, display, size):
    x, y = board_to_pixel_koord(frucht.koord["x"], frucht.koord["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, frucht.zufallsfarbe(), the_rect)


if __name__ == "__main__":
    makegame()
