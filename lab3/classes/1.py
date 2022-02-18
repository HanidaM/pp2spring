class Upper:
    def __init__(self, string):
        self.string = string
        

    def getString(self):
        pass    
    
    def printString(self):
        print(self.string.upper())

ss = Upper(input())
ss.printString()
