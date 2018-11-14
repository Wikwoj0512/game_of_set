import random
import pygame
import json



pygame.init()

started=False
zdj=[]
for i in range(0,82):
    zdj.append(pygame.image.load('grafiki/nr.png'.replace('nr',str(i))))


RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)

size = (1300, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("SET")
screen.fill(WHITE)
done = False

clock = pygame.time.Clock()
gameState=0
font = pygame.font.Font("HighlandGothicFLF.ttf", 20)


with open('cards','r')as f:
    a=f.read()
    cards= json.loads(a)
    cardsleft=json.loads(a)


mouse_state = 0
mouse_x = 0
mouse_y = 0


gameState = 0

class field():
    global cardsleft,cards
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.nocards=[[1,1],[1,2],[1,3],[1,4],[2,1],[2,2],[2,3],[2,4],[3,1],[3,2],[3,3],[3,4]]
        self.col5=False
        self.ids=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self.sets=0

        for i in self.nocards:
            self.addcard(i[0],i[1])
    def addcard(self,x,y):
        if self.col5:
            card=self.ids[4][-1]
            self.ids[4].pop(-1)
            self.ids[y - 1][x - 1] = card
        else:
            if not len(cardsleft)==0:
                card = random.choice(list(cardsleft.values()))
                cardsleft.pop(str(card['ide']))
                self.ids[y-1][x-1]=card['ide']
            else:
                if f.sets:
                    self.ids[y - 1][x - 1] = 0
                else:
                    gameState=1
                    return

    def check(self):
        y1=gracz.clicked[0][1] - 1
        x1=gracz.clicked[0][0]-1
        blok1=cards[str(self.ids[x1][y1])]
        x2=gracz.clicked[1][0] - 1
        y2=gracz.clicked[1][1] - 1
        blok2 = cards[str(self.ids[x2][y2])]
        x3=gracz.clicked[2][0] - 1
        y3=gracz.clicked[2][1] - 1
        blok3 = cards[str(self.ids[x3][y3])]
        if ((blok1['t'] == blok2['t'] and blok2['t'] == blok3['t']) or (
                blok1['t'] != blok2['t'] and blok2['t'] != blok3['t'] and blok1['t'] != blok3['t'])) and \
                ((blok1['k'] == blok2['k'] and blok2['k'] == blok3['k']) or (
                        blok1['k'] != blok2['k'] and blok2['k'] != blok3['k'] and blok1['k'] != blok3['k'])) \
                and (((blok1['w'] == blok2['w'] and blok2['w'] == blok3['w']) or (
                blok1['w'] != blok2['w'] and blok2['w'] != blok3['w'] and blok1['w'] != blok3['w']))) and \
                ((blok1['n'] == blok2['n'] and blok2['n'] == blok3['n']) or
                 (blok1['n'] != blok2['n'] and blok2['n'] != blok3['n'] and blok1['n'] != blok3['n'])):
            print('SET')

            gracz.sets.append([blok1['ide'],blok2['ide'],blok3['ide']])
            if x1<4:
                f.addcard(y1+1,x1+1)
            if x2<4:
                f.addcard(y2+1,x2+1)
            if x3<4:
                f.addcard(y3+1,x3+1)

            if f.col5:
                f.col5=False
                f.columns=4
                f.ids.pop()


    def checkai(self):
        try:
            y1=ai.clicked[0][1] - 1
            x1=ai.clicked[0][0]-1
            blok1=cards[str(self.ids[x1][y1])]
            x2=ai.clicked[1][0] - 1
            y2=ai.clicked[1][1] - 1
            blok2 = cards[str(self.ids[x2][y2])]
            x3=ai.clicked[2][0] - 1
            y3=ai.clicked[2][1] - 1
            blok3 = cards[str(self.ids[x3][y3])]

            if ((blok1['t'] == blok2['t'] and blok2['t'] == blok3['t']) or (
                    blok1['t'] != blok2['t'] and blok2['t'] != blok3['t'] and blok1['t'] != blok3['t'])) and \
                    ((blok1['k'] == blok2['k'] and blok2['k'] == blok3['k']) or (
                            blok1['k'] != blok2['k'] and blok2['k'] != blok3['k'] and blok1['k'] != blok3['k'])) \
                    and (((blok1['w'] == blok2['w'] and blok2['w'] == blok3['w']) or (
                    blok1['w'] != blok2['w'] and blok2['w'] != blok3['w'] and blok1['w'] != blok3['w']))) and \
                    ((blok1['n'] == blok2['n'] and blok2['n'] == blok3['n']) or
                     (blok1['n'] != blok2['n'] and blok2['n'] != blok3['n'] and blok1['n'] != blok3['n'])):
                print('SET')

                ai.sets.append([blok1['ide'],blok2['ide'],blok3['ide']])
                if x1<4:
                    f.addcard(y1+1,x1+1)
                if x2<4:
                    f.addcard(y2+1,x2+1)
                if x3<4:
                    f.addcard(y3+1,x3+1)

                if f.col5:
                    f.col5=False
                    f.columns=4
                    f.ids.pop()
        except:
            pass


    def checkset(self,pos):

        y1 = pos[0][1]
        x1 = pos[0][0]
        x2 = pos[1][0]
        y2 = pos[1][1]
        x3 = pos[2][0]
        y3 = pos[2][1]
        if not self.ids[x1][y1] ==0 and not self.ids[x2][y2]==0 and not self.ids[x3][y3]==0:
            blok1 = cards[str(self.ids[x1][y1])]
            blok2 = cards[str(self.ids[x2][y2])]
            blok3 = cards[str(self.ids[x3][y3])]
            if ((blok1['t'] == blok2['t'] and blok2['t'] == blok3['t']) or (
                    blok1['t'] != blok2['t'] and blok2['t'] != blok3['t'] and blok1['t'] != blok3['t'])) and \
                    ((blok1['k'] == blok2['k'] and blok2['k'] == blok3['k']) or (
                            blok1['k'] != blok2['k'] and blok2['k'] != blok3['k'] and blok1['k'] != blok3['k'])) \
                    and (((blok1['w'] == blok2['w'] and blok2['w'] == blok3['w']) or (
                    blok1['w'] != blok2['w'] and blok2['w'] != blok3['w'] and blok1['w'] != blok3['w'])) )and \
                    ((blok1['n'] == blok2['n'] and blok2['n'] == blok3['n']) or
                     (blok1['n'] != blok2['n'] and blok2['n'] != blok3['n'] and blok1['n'] != blok3['n'])):
                # print(blok1)
                # print(blok2)
                # print(blok3)
                # print([[x1+1,y1+1],[x2+1,y2+1],[x3+1,y3+1]])
                return True


    def checkforsets(self):
        for c in range(0,len(self.ids)):
            for r in range(0,self.rows):
                for c2 in range(0,self.columns):
                    for r2 in range(0,self.rows):
                        if c!=c2 and r!=r2:
                            for c3 in range(0,self.columns):
                                for r3 in range(0,self.rows):
                                    if c != c2 and r != r2 and c!=c3 and r!=r3:
                                        if self.checkset([[c,r],[c2,r2],[c3,r3]]):
                                            return True



f=field(3,4)



class player():
    def __init__(self):
        self.clicked=[[0,0],[0,0],[0,0]]
        self.sets=[]

gracz=player()
ai=player()

class Button():
    def __init__(self):
        self.textBoxes = {}

    # ----Clicked In----
    def clickedIn(self, x, y, width, height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 1 and mouse_x >= x and mouse_x <= (x + width) and mouse_y >= y and mouse_y <= (y + height):
            return True

    # ----Clicked Out----
    def clickedOut(self, x, y, width, height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 1 and mouse_x < x or mouse_state == 1 and mouse_x > (
                x + width) or mouse_state == 1 and mouse_y < y or mouse_state == 1 and mouse_y > (y + height):
            return True

    def hovering(self, x, y, width, height):
        global mouse_state, mouse_x, mouse_y
    # ----Hovering----
        if mouse_state == 0 and mouse_x >= x and mouse_x <= (x + width) and mouse_y >= y and mouse_y <= (y + height):
            return True

    # ----Click Button----
    def clickButton(self, x, y, width, height, normalColor, hoverColor, textFont, text, textColor, stateHolding=False,
                    stateVariable=0, state=1):
        if not self.clickedIn(x, y, width, height) and not self.hovering(x, y, width, height):
            pygame.draw.rect(screen, normalColor, (x, y, width, height))
        elif self.hovering(x, y, width, height):
            pygame.draw.rect(screen, hoverColor, (x, y, width, height))
        if stateHolding == True and stateVariable == state:
            pygame.draw.rect(screen, hoverColor, (x, y, width, height))
        buttonText = textFont.render(text, True, textColor)
        buttonText_x = buttonText.get_rect().width
        buttonText_y = buttonText.get_rect().height
        screen.blit(buttonText, (((x + (width / 2)) - (buttonText_x / 2)), ((y + (height / 2)) - (buttonText_y / 2))))
        if self.clickedIn(x, y, width, height):
            return True


button = Button()

def zapis():
    pozycje={'done':done,'columns':f.columns,'rows':f.rows,'ids':f.ids}
    with open('field.txt','w') as file:
        file.write(json.dumps(pozycje))
def odczyt():
    try:
        with open('aiclicked.txt','r') as file:
            return  json.loads(file.read())
    except:
        pass

def draw():
    screen.fill(WHITE)
    if gameState==0:
        for c in range(0,f.columns):
            for r in range(0,f.rows):
                x=c+1
                y=r+1
                id=f.ids[c][r]
                pozx=x*250 -110 if not f.col5 else  x*250-210
                pozy=y*150-110
                if [c+1,r+1] in gracz.clicked:
                    pygame.draw.rect(screen,ORANGE,((pozx-10,pozy-10,220,120)))
                screen.blit(zdj[id],(pozx,pozy))

        if gracz.sets:
            ostset=gracz.sets[-1]
            screen.blit(zdj[ostset[0]],(250, 450))
            screen.blit(zdj[ostset[1]],(500,450))
            screen.blit(zdj[ostset[2]], (750, 450))
        if ai.sets:
            ostset = ai.sets[-1]
            screen.blit(zdj[ostset[0]], (250, 600))
            screen.blit(zdj[ostset[1]], (500, 600))
            screen.blit(zdj[ostset[2]], (750, 600))
    else:
        winner = 'program' if len(ai.sets )>len(gracz.sets) else 'człowiek'
        roznica=abs(len(ai.sets)-len(gracz.sets))
        text = font.render("zwyciezca zostal " + winner , True, BLACK)
        screen.blit(text, ((size[0]/2 -100, size[1]/2-50)))
        text = font.render("Zwyciezyl on przewaga ilosc setow".replace('ilosc', str(roznica)), True, BLACK)
        screen.blit(text, ((size[0] / 2 - 100, size[1] / 2 - 20)))
    pygame.display.update()



while not done:
    f.sets = f.checkforsets()
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_state = event.button
            pygame.mouse.set_pos(mouse_x, mouse_y + 1)
        else:
            mouse_state = 0
    if gameState==0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            if not f.sets and not f.col5:

                f.ids.append([0,0,0])
                f.addcard(1,5)
                f.addcard(2,5)
                f.addcard(3,5)
                f.columns=5
                f.col5= True
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_state==3:
            gracz.clicked=[[0,0],[0,0],[0,0]]
        else:
            if (((mouse_x-90)%250>50 and not f.col5) or (mouse_x%250>50 and f.col5) ) and mouse_y%150>50 :
                if not f.col5:
                    xd=int((mouse_x-90)//250)
                else:
                    xd = int(mouse_x  // 250)
                yd=int(mouse_y//150)
                xd+=1
                yd+=1
            else:
                xd=0
                yd=0
        if mouse_state==1:
            if xd!=0:
                if gracz.clicked[1][0]>0 and gracz.clicked[1]!=[xd,yd] and gracz.clicked[0]!=[xd,yd]:
                    if not f.ids[xd-1][yd-1]==0:
                        gracz.clicked[2] = [xd, yd]
                        f.check()
                        gracz.clicked=[[0,0],[0,0],[0,0]]

                elif gracz.clicked[0][0]>0 and gracz.clicked[0]!=[xd,yd]:
                    if not f.ids[xd - 1][yd - 1] == 0:
                        gracz.clicked[1] = [xd, yd]

                else:
                    if not f.ids[xd-1][yd-1]==0:
                        gracz.clicked[0] = [xd,yd]
        if len(cardsleft)==0 and not f.sets:
            gameState=1

        a = odczyt()

        if a:
            if a['n']:
                f.sets = f.checkforsets()
                f.checkforsets()
                if not f.sets and not f.col5:
                    f.ids.append([0, 0, 0])
                    f.addcard(1, 5)
                    f.addcard(2, 5)
                    f.addcard(3, 5)
                    f.columns = 5
                    f.col5 = True
                # if f.sets and f.col5:
                #     done=True
            if a['clicked'] != ai.clicked:
                ai.clicked = a['clicked']
                f.checkai()
                print(len(ai.sets))
                print(len(gracz.sets))
                print(len(cardsleft))
                if len(cardsleft) ==0 and not f.sets:
                    gameState=1


        zapis()





pygame.quit()