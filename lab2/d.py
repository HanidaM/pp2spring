n = int(input())

if n % 2 == 0:
    for i in range(0, n):
        for j in range(0, n):
            if i >=j:
                print("#", end="")
            else:
                 print(".", end="")
        print("")
                 
else:
    for i in range(0, n):
        for j in range(0, n):
            if i+j >= n - 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")