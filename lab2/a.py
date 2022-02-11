n = input().split()
a = []
max_jump=0

for i in range (len(n)):
    a.append(int(n[i]))

for i in range (len(n)):
    if max_jump >= i:
        if a[i] + i >= len(n) - 1:
            print(1)
            exit()
        elif a[i] + i > max_jump:
            max_jump = a[i] + i
    else:
        break
if max_jump < len(n) - 1:
    print(0)