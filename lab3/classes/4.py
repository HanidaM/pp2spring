import math


class point:
    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy

    def show(self):
        print (self.xx, self.yy)

    def move(self):
        self.xx = int(input())
        self.yy = int(input())
    
    def dist(self, p2):
        return math.sqrt((self.xx + p2.xx)**2 + (self.yy + p2.yy)**2)



p1 = point(int(input()), int(input()))
p2 = point(int(input()), int(input()))


print(p1.dist(p2))