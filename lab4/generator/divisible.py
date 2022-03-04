def divisible(n):
    for i in range(n):
        if(i%3==0 and i%4==0):
            yield i

if __name__ == "__main__":
    n = int(input("Give me a range: "))
    for i in divisible(n):
        print(i)