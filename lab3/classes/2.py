class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    

class square(shape):
    def __init__(self, length):
        shape.__init__(self)
        self.length = length
    def area(self):
        return self.length**2


qq = square(4)
print(qq.area())