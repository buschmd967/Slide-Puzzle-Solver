from board import board

b = board(5, 5)
inputsUsed = []

def up():
    b.up()
    inputsUsed.append("D")
def down():
    b.down()
    inputsUsed.append("U")
def left():
    b.left()
    inputsUsed.append("R")
def right():
    b.right()
    inputsUsed.append("L")

def gotoTarget(target):
    while(target // 5 > b.x // 5):
        up()
        b.print()
    while(target // 5 < b.x // 5):
        down()
        b.print()
    while(target % 5 < b.x % 5):
        right()
        b.print()
    while(target % 5 > b.x % 5):
        left()
        b.print()

def getBelow(target):
    if(target // 5 >= 4):
        if(b.x // 5 == target // 5):
            down()
            b.print()
        gotoTarget(target - 5)
        up()
    else:
        gotoTarget(target + 5)

def shiftUp():
    if(b.x % 5 < 4):
        left()
        down()
        down()
        right()
        up()
    else:
        right()
        down()
        down()
        left()
        up()

def shiftLeft():
    right()
    down()
    left()
    up()
    right()

def shiftRight():
    left()
    down()
    right()
    up()
    left()

def cornerInsert():
    down()
    down()
    left()
    up()
    right()
    down()
    left()
    up()
    up()
    right()
    down()
    left()
    up()
    right()
    down()
    down()
    left()
    up()

#Bottom Triangle:
# X 2
# 1
# Want to get
# . X
# 1 2

def bottomTriangle(): #['U', 'L', 'D', 'L', 'U', 'R', 'R', 'D', 'L', 'U', 'L', 'D', 'R']
    up()
    left()
    down()
    left()
    up()
    right()
    right()
    down()
    left()
    up()
    left()
    down()
    right()

def solveFirstRow():
    for i in range(1, 5):
        print("=====" + str(i) + "=====")
        target = b.find(str(i))
        getBelow(target)
        while(b.b[b.x - 5] != str(i)):
            target = b.find(str(i))
            getBelow(target) #get a position where X is right of target number
       
        while(b.x % 5 > i - 1): #get to correct col
            shiftLeft()
            print("left")
            b.print()
        while(b.x % 5 < (i - 1) % 5):
            shiftRight()
            print("right")
            b.print()
        while(b.x // 5 > 1): #get to correct row
            shiftUp()
            print("up")
            b.print()
    #now do 5
    print("=====5======")
    target = b.find("5")
    if(target != 4):
        getBelow(target)
        #want to get under 4, which is index 8 (row 2, col 4)
        while(b.x // 5 > 2):
            shiftUp()
            b.print()
        while(b.x % 5 > 3):
            shiftLeft()
            b.print()
        while(b.x % 5 < 3):
            shiftRight()
            b.print()
        cornerInsert()

def solveSecondRow():
    for i in range(6, 10):
        print("=====" + str(i) + "=====")
        target = b.find(str(i))
        getBelow(target)
        while(b.b[b.x - 5] != str(i)):
            target = b.find(str(i))
            getBelow(target) #get a position where X is right of target number
        
        while(b.x % 5 > (i - 1) % 5): #get to correct col
            shiftLeft()
            print("left")
            b.print()
        while(b.x % 5 < (i - 1) % 5):
            shiftRight()
            print("right")
            b.print()
        while(b.x // 5 > 2): #get to correct row
            shiftUp()
            print("up")
            b.print()
    #now do 5
    print("=====10======")
    target = b.find("10")
    if(target != 9):
        getBelow(target)
        b.print()
        while(b.b[b.x - 5] != "10"):
            target = b.find("10")
            getBelow(target)
            b.print()
        #want to get under 4, which is index 8 (row 2, col 4)
        while(b.x // 5 > 3):
            shiftUp()
            b.print()
        while(b.x % 5 > 3):
            shiftLeft()
            b.print()
        while(b.x % 5 < 3):
            shiftRight()
            b.print()
        cornerInsert()

def solveThirdRow():
    for i in range(11, 15):
        print("=====" + str(i) + "=====")
        target = b.find(str(i))
        getBelow(target)
        while(b.b[b.x - 5] != str(i)):
            target = b.find(str(i))
            getBelow(target) #get a position where X is right of target number
        
        while(b.x % 5 > (i - 1) % 5): #get to correct col
            shiftLeft()
            print("left")
            b.print()
        while(b.x % 5 < (i - 1) % 5):
            shiftRight()
            print("right")
            b.print()
        while(b.x // 5 > 3): #get to correct row
            shiftUp()
            print("up")
            b.print()
    #now do 5
    print("=====15======")
    target = b.find("15")
    getBelow(target)
    if(target != 14):
        #want to get under 4, which is index 8 (row 2, col 4)
        while(b.x // 5 > 4):
            shiftUp()
            b.print()
        while(b.x % 5 > 3):
            shiftLeft()
            b.print()
        while(b.x % 5 < 3):
            shiftRight()
            b.print()
        cornerInsert()


def prepare16(): 
    #Get 16 to bottom left
    print("=====16=====")
    b.print()
    target = b.find("16")
    if(target != 21): # if not in bottom left
        if(target // 5 == 3): #if in 4th row
            #Get below
            up()
            while(target % 5 < b.x % 5):
                right()
            #move to left edge
            while(b.x % 5 > 0):
                shiftLeft()
            #move above to shift it th bottom left
            down()
        else: #in last row already
            while(target % 5 < b.x % 5):
                right()
            #now above
            up()
            print("Should be below 16")
            b.print()
            while(b.x % 5 > 0):
                shiftLeft()
            #now below and at bottom left
            down()
    else:
        while(b.x % 5 > 0):
            right()

def solveLeftTwo(): #X expected to be in 4th row, right edge
    prepare16()
    print("16 prepared")
    target = b.find("21")
    if(target == 20): #Shouldn't happen, idk
        getBelow(16)
        return
    if(target == 16):
        bottomTriangle()
    elif(target != 21): #if not right of bottom left
        #assume 21 is in bottom right 6
        if(target // 5 == 3): #if in 4th row
            left()
            up()
        getBelow(target)
        print("going to 2nd col")
        while(b.x % 5 > 1): #until x in 2nd col
            shiftLeft()
        down()
        #Currently next to 16, x above 21
    if(target != 21):
        right()
    up()
    left()

def prepare17():
    target = b.find("17")
    if(target // 5 == 4): #if in last row
        down()
    getBelow(target)
    while(b.x % 5 > 1): #move to 2nd col
        shiftLeft()
    down()



def solveSecondLeftTwo(): # X expected to be in 
    prepare17()
    print("17 prepared")
    b.print()
    #X should now be above 17 in the 2nd col
    target = b.find("22")
    if(target == 17):
        print("doing triangle")
        bottomTriangle()
        right()
    elif(target != 22):
        if(target // 5 == 3):
            left()
            up()
        getBelow(target)
        while(b.x % 5 > 2):
            shiftLeft()
        down()
        right()
    #X above 22, 17 left of 22
    up()
    left()

def prepare18():
    target = b.find("18")
    if(target // 5 == 4): #if in last row
        down()
    getBelow(target)
    while(b.x % 5 > 2): #move to 2nd col
        shiftLeft()
    down()

def solveMiddleTwo():
    prepare18()
    print("18 prepared")
    b.print()
    #X should now be above 17 in the 2nd col
    target = b.find("23")
    if(target == 18):
        print("doing triangle")
        bottomTriangle()
        right()
    elif(target != 23):
        if(target // 5 == 3):
            left()
            up()
        getBelow(target)
        while(b.x % 5 > 3):
            shiftLeft()
        down()
        right()
    #X above 22, 17 left of 22
    up()
    left()
            
def finishByCase():
    while(b.x // 5 < 4):
        up()
    while(b.x % 5 < 4):
        left()
    b.print()
    
    #case made up of 19, 20, 24, whith x in bottom right
    case = [b.b[18], b.b[19], b.b[23]]
    print(case)
    if case == ["19", "20", "24"]:
        return
    elif case == ["19", "24", "20"]:
        pass #not possible?
    elif case == ["20", "19", "24"]:
        pass #not possible?
    elif case == ["20", "24", "19"]:
        down()
        right()
        up()
        left()
    elif(case == ["24", "19", "20"]):
        right()
        down()
        left()
        up()
        right()
    elif(case == ["24", "20", "19"]):
        pass #not possible()

def solveLastTwo():
    solveLeftTwo()
    solveSecondLeftTwo()
    solveMiddleTwo()
    finishByCase()


def getBoard():
    with open("input.txt", "r") as f:
        s = f.read()
        s = s.replace("|", "")
        s = s.replace("\n", "")
        a = []
        for c in s.split(" "):
            if(c.replace(" ", "") != ""):
                a.append(c)
        return a

def main():
    a = getBoard()
    #a = [
    #"22", "4", "3", "2", "5",
    #"24", "6", "7", "8", "9",
    #"10", "11", "12", "13", "14",
    #"15", "16", "17", "18", "19",
    #"20", "21", "1", "23", "x"]
    b.set(5, 5, a)
    solveFirstRow()
    solveSecondRow()
    solveThirdRow()
    solveLastTwo()
    
    b.print()
    
    for i in inputsUsed:
        print(i + ",", end="")

if __name__ == "__main__":
    main()