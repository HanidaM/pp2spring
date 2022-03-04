def evenrange(n):
    for i in range(n): 
        if(i % 2 == 0):
            yield i

if __name__ == "__main__":
    n = int(input("Give me a range: "))
    for i in evenrange(n):
        print(i, end=", ")