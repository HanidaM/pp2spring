class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class rectangle():
    def __init__(self,length, width):
        self.length = length
        self.width = width
        super().__init__()
    
    def area(self):
        return self.length * self.width


user = rectangle(int(input()), int(input()))
print(user.area())