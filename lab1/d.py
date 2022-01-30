n = int(input())
z = input()
c = input()
digits = 0 + int(c)

if z == 'k':
    m = float((n / 1024))
    print(round(m, 10))
elif z == 'b':
    print(n * 1024)
