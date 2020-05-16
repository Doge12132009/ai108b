import json
import random,os,re

inputfile=open("data.json",encoding="UTF-8")
bs=json.load(inputfile)

famous=bs["famous"]
after=bs["after"]
before=bs["before"]
bullshit=bs["bullshit"]

xxx=input("主題:")
limit=input("字數限制:")
limit=int(limit)

dup=2

def hash(List):
    global dup
    pool = list(List) * dup
    while True:
        random.shuffle(pool)
        for elem in pool:
            yield elem

nextFam=hash(famous)
nextShit=hash(bullshit)

def newWords():
    global nextFam
    xxx = next(nextFam)
    xxx = xxx.replace(  "a",random.choice(before)) 
    xxx = xxx.replace(  "b",random.choice(after) )
    return xxx

def newPar():
    xxx = ". "
    xxx += "\r\n"
    xxx += "    "
    return xxx

if __name__ == "__main__":
    for x in xxx:
        tmp = str()
        while ( len(tmp) < limit ) :
            node = random.randint(0,100)
            if node < 5:
                tmp += newPar()
            elif node < 20 :
                tmp += newWords()
            else:
                tmp += next(nextShit)
        tmp = tmp.replace("x",xxx)
        print(tmp)
