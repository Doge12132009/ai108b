def printMap(m) :
    for i in range(6):
        for j in range(8):
            print(m[i][j],end='')
        print() 

def steped(x1,y1) :
    m[x1][y1] = "."


def findPath(m, x, y) :
    print("=========================")
    print("x= {} y= {}".format(x,y))
    printMap(m)
    if x>=6 or y>=8 :
        return
    if m[x][y] == '*' :
        return
    if m[x][y] == ' ' :
        steped(x, y)
    if m[x][y] == '.' and (x == 5 or y==7) :  
        return
    if  y<7 and m[x][y+1]==' ' : 
        findPath(m, x,y+1)
    
    if  x<5 and m[x+1][y]==' ' : 
        findPath(m, x+1,y) 
            
    if y>0 and m[x][y-1]==' ' : 
        findPath(m, x,y-1)
            
    if x>0 and m[x-1][y]==' ' : 
        findPath(m, x-1,y)
            
    return x,y

m=[
    ["*","*","*","*","*","*","*","*"], 
    ["*","*"," ","*"," ","*","*","*"],
    [" "," "," "," "," ","*","*","*"],
    ["*"," ","*","*","*","*","*","*"],
    ["*"," "," "," "," "," ","*","*"],
    ["*","*","*","*","*"," ","*","*"]]

findPath(m, 2, 0)
print("=========================")
printMap(m)
