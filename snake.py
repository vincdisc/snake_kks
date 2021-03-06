import pygame, sys
import random as rd

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
PINK = (238, 18, 137)
ORANGE = (238, 69, 0)
VIOLETTE = (139, 0, 139)
BLUE = (0, 0, 139)

farbenliste = [PINK, ORANGE, VIOLETTE, BLUE, GREEN]

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
            self.fout = open('Ergebnisse', 'a')


        def write(self, name):
            self.fout.write(name)

        def beenden(self):
            self.fout.close()






def makemenu():
    BOARD_LENGHT = 600
    BOARD_HIGHT = BOARD_LENGHT
    FPS = 8
    CELLSIZE = 20

    assert BOARD_LENGHT % CELLSIZE == 0
    assert BOARD_HIGHT % CELLSIZE == 0
    CELLWIDTH = int(BOARD_LENGHT / CELLSIZE)

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGHT, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('MENU')



    while True:
        DISPLAYSURF.fill(WHITE)

        spielbutton = Button()
        spielbutton.create_button(DISPLAYSURF, GREEN, 50, 50, 150, 50, 0, "Spiel", BLACK)

        rangbutton = Button()
        rangbutton.create_button(DISPLAYSURF, GREEN, 300, 50, 150, 50, 0, "Liste", BLACK)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:  # Definition ESC Taste
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    makegame()

            elif event.type==pygame.MOUSEBUTTONDOWN:
                spielbutton.pressed(pygame.mouse.get_pos())
                makegame()



        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeend():
    BOARD_LENGHT = 600
    BOARD_HIGHT = BOARD_LENGHT
    FPS = 8
    CELLSIZE = 20

    assert BOARD_LENGHT % CELLSIZE == 0
    assert BOARD_HIGHT % CELLSIZE == 0
    CELLWIDTH = int(BOARD_LENGHT / CELLSIZE)

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGHT, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('ENDE')



    punktespeichern(punkte)

    print("Done")

    while True:
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:  # Definition ESC Taste
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    makemenu()

        pygame.display.update()
        FPSCLOCK.tick(FPS)










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


    global punkte
    punkte=0

    snake = Snake()
    frucht = Fruits()

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((GANZE_LAENGE, BOARD_HIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('SNAKE')

    while True:
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

        # Snake wird von Rand gestopt

        for i in range(len(my_feld.felder)):
            for j in range(len(my_feld.felder[i])):
                if my_feld.felder[i][j] == 1:
                    randliste = {'x': i, 'y': j}
                    if randliste == snake.körperteile[0]:
                        makeend()

        snake.update()

        for x in range(0, BOARD_LENGHT, CELLSIZE):  # zeichnet senkrechte lienien
            pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, BOARD_LENGHT))

        for y in range(0, BOARD_HIGHT, CELLSIZE):  # zeichnet horizontale lienien
            pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (BOARD_HIGHT, y))

        # Spielablauf

        punktezahl=Button()
        punktezahl.create_button(DISPLAYSURF,WHITE,650,100,150,60,0,str(punkte),BLACK)


        if snake.körperteile[
            0] == frucht.koord:  # wenn eine frucht gegessen wird, wird hier eine neue frucht aufgerufen
            snake.körper_hinzufügen()
            frucht.frucht_neupos()
            punkte+=1
            print(punkte)


        for i in snake.körperteile[1:]:  # wenn die schlange mit sich selbst kollidiert esc spiel
            if snake.körperteile[0] == i:
                makeend()

        for körperteil in snake.körperteile:
            make_rectangle_snake(körperteil, DISPLAYSURF, CELLSIZE)

        # frucht
        make_rectangle_fruit(frucht, DISPLAYSURF, CELLSIZE)



        pygame.display.update()
        FPSCLOCK.tick(FPS)





def punktespeichern(zahl):
    tabelle=File()
    name=input("Gebe deinen Namen ein:")
    tabelle.write(name+ ": " + str(zahl) + "\n")
    tabelle.beenden()


def board_to_pixel_koord(i, j, width):
    return i * width, j * width


def make_rectangle_snake(dict, display, size):
    x, y = board_to_pixel_koord(dict["x"], dict["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, GREEN, the_rect)


def make_rectangle_fruit(frucht, display, size):
    x, y = board_to_pixel_koord(frucht.koord["x"], frucht.koord["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, frucht.zufallsfarbe(), the_rect)


if __name__ == "__main__":
    makemenu()