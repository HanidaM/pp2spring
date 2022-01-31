a = input()
b = input()

def occurance(a, b):
    for i in a:
        c = a.find(b)
        d = a.rfind(b)
        if c == d:
            print(c)
            return 0
        elif c != d:
            print(c, d)
            return 0
occurance(a, b)

