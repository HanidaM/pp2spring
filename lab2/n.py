a = []
arr = []


a.append((int(input())))
while(a[len(a) - 1] != 0):
    a.append(int(input()))

for i in range(int((len(a) - 1) / 2)):
    arr.append(a[i] + a[len(a) - 2 - i])
if(len(a) % 2 == 0):
    arr.append(a[int((len(a)) / 2 ) - 1])
print(*arr)