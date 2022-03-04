def gensquares(n, m):
    for i in range(n, m): 
        yield i**2

if __name__ == "__main__":
    n = int(input("Give me a range A to sqr: "))
    m = int(input("Give me a range B to sqr: "))
    
    for i in gensquares(n, m):
        print(i, end=", ")