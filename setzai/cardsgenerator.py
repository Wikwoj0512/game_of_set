import json
id=0
t=["r",'f','e']
k=['f','c','z']
n=[1,2,3]
w=[1,2,3]
allcards={}
for ti in t:
    for ki in k:
        for wi in w:
            for ni in n:
                id+=1
                allcards[id]={'ide':id,'t':ti,'k':ki,'w':wi,'n':ni}
                print(allcards)

karty=open('cards','w')

karty.write(json.dumps(allcards))
# print(str(allcards))