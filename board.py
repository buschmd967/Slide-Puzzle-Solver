import os

class board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.b = [str(i+1) for i in range(width * height - 1)]
        self.b.append("x")
        self.x = width * height - 1
    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.b[j + i * self.width].ljust(3, " "), end="")
            print("")
        print("")
    def find(self, val):
        for i in range(len(self.b)):
            if(self.b[i] == val):
                return i
        return -1
    def down(self):
        if(self.x >= self.height):
            target = self.x - self.height
            self.b[self.x] = self.b[target]
            self.b[target] = "x"
            self.x = target
        else:
            print("Tried to move down when not possible.")
            os.exit()
    def up(self):
        if(self.x <= self.height * self.width - self.height):
            target = self.x + self.height
            self.b[self.x] = self.b[target]
            self.b[target] = "x"
            self.x = target
        else:
            print("Tried to move up when not possible.")
            os.exit()
    def left(self):
        if(self.x % self.height < self.width - 1):
            target = self.x + 1
            self.b[self.x] = self.b[target]
            self.b[target] = "x"
            self.x = target
        else:
            print("Tried to move left when not possible.")
            os.exit()
    def right(self):
        if(self.x % self.height > 0):
            target = self.x - 1
            self.b[self.x] = self.b[target]
            self.b[target] = "x"
            self.x = target
        else:
            print("Tried to move right when not possible.")
            self.print()
            os.exit()

    def set(self, height, width, a):
        self.height = height
        self.width = width
        self.b = a.copy()
        self.x = self.find("x")
        if(self.x == -1):
            self.x = self.find("X")
        if(self.x == -1):
            print("COULD NOT FIND X")


def test():
    b = board(5, 5)
    a = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15",
    "16", "17", "18", "24", "19",
    "21", "22", "23", "20", "x"]
    b.set(5, 5, a)
    x = "go"
    b.print()
    inputs = []
    while x != "X":
        x = input()
        if(x == "w"):
            b.down()
            inputs.append("D")
        elif(x == "s"):
            b.up()
            inputs.append("U")
        elif(x == "a"):
            b.right()
            inputs.append("R")
        elif(x == "d"):
            b.left()
            inputs.append("L")
        b.print()
    print(inputs)



if __name__ == "__main__":
    test()
