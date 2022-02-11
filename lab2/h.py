x, y = input().split()
array = []

def myf(x, y, a, b):
    dist = ((x-a)**(2) + (y-b)**2)**0.5
    return dist

for i in range(int(input())):
    s = input()
    a, b = s.split()
    arr1 = []
    arr1.append(myf(int(x), int(y), int(a), int(b)))
    arr1.append(int(a))
    arr1.append(int(b))
    array.append(arr1)

    
array.sort()


for i in range(len(array)):
    print(array[i][1], array[i][2])