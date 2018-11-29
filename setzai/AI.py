import random,json,time
with open('cards','r')as f:
    cards=json.loads(f.read())
print('closing this window will stop the ai.')
latencymin=int(float(input('min. olatency: '))*10)
latencymax = int(float(input('max. latency: '))*10)
pok=input('Do you want to see the sets? (Y/N) ')
if pok.lower()=='y':
    pok=True



class player():
    def __init__(self):
        self.columns=4
        self.rows=3
        self.clicked=[[0,0],[0,0],[0,0]]
        self.ids=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self.n=False

    def checkset(self, pos):
        y1 = pos[0][1]
        x1 = pos[0][0]
        x2 = pos[1][0]
        y2 = pos[1][1]
        x3 = pos[2][0]
        y3 = pos[2][1]
        if not self.ids[x1][y1] == 0 and not self.ids[x2][y2] == 0 and not self.ids[x3][y3] == 0:
            blok1 = cards[str(self.ids[x1][y1])]
            blok2 = cards[str(self.ids[x2][y2])]
            blok3 = cards[str(self.ids[x3][y3])]
            if ((blok1['t'] == blok2['t'] and blok2['t'] == blok3['t']) or (
                    blok1['t'] != blok2['t'] and blok2['t'] != blok3['t'] and blok1['t'] != blok3['t'])) and \
                    ((blok1['k'] == blok2['k'] and blok2['k'] == blok3['k']) or (
                            blok1['k'] != blok2['k'] and blok2['k'] != blok3['k'] and blok1['k'] != blok3['k'])) \
                    and (((blok1['w'] == blok2['w'] and blok2['w'] == blok3['w']) or (
                    blok1['w'] != blok2['w'] and blok2['w'] != blok3['w'] and blok1['w'] != blok3['w']))) and \
                    ((blok1['n'] == blok2['n'] and blok2['n'] == blok3['n']) or
                     (blok1['n'] != blok2['n'] and blok2['n'] != blok3['n'] and blok1['n'] != blok3['n'])):
                if pok:
                    print(blok1)
                    print(blok2)
                    print(blok3)
                    print([[x1 + 1, y1 + 1], [x2 + 1, y2 + 1], [x3 + 1, y3 + 1]])
                self.clicked=[[x1 + 1, y1 + 1], [x2 + 1, y2 + 1], [x3 + 1, y3 + 1]]
                return True


    def findsets(self):
        for c in range(0, self.columns):
            for r in range(0, self.rows):
                for c2 in range(0, self.columns):
                    for r2 in range(0, self.rows):
                        if c != c2 and r != r2:
                            for c3 in range(0, self.columns):
                                for r3 in range(0, self.rows):
                                    if c != c2 and r != r2 and c != c3 and r != r3:
                                        if self.checkset([[c, r], [c2, r2], [c3, r3]]):
                                            return True
        return False

ai=player()


def read():
    try:
        with open('field.txt','r') as file:
            tablica = json.loads(file.read())
            return tablica
    except:
        pass
def zapis():
    pozycje={'n':ai.n,'clicked':ai.clicked}
    with open('aiclicked.txt','w') as file:
        file.write(json.dumps(pozycje))



done =False
while not done:
    a=read()
    tablica=a if a else tablica
    ai.columns=tablica['columns']
    latency=random.randint(latencymin,latencymax)/10
    # latency=0.2
    time.sleep(latency)
    ai.ids=tablica['ids']
    czysety = ai.findsets()
    if czysety:
        ai.n=False
    else:
        ai.n=True

    zapis()

    print(ai.n,ai.clicked, ai.columns)


    done=tablica['done']


