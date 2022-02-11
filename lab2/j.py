cnt = int(input())
l = []

for x in range(cnt):
    up = 0
    low = 0
    num = 0
    s = input()
    for y in s:
        if y.isupper():
            up += 1
        elif y.islower():
            low += 1
        elif y.isdigit():
            num += 1
    if up != 0 and low != 0 and num != 0 and s not in l:
        l.append(s)
print(len(l))
l.sort()

for x in l:
    print(x)