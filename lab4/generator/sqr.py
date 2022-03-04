

def gensquares(n):
    for i in range(n): 
        yield i**2

if __name__ == "__main__":
    n = int(input("Give me a range to sqr: "))
    for i in gensquares(n):
        print(i)
