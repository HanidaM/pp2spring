lst = []
n = int(input())

s = "@gmail.com"


for i in range(0, n):
    logs = input()

    lst.append(logs)


for i in lst:
    if i.find(s):
        print(i.removesuffix("@gmail.com"))
    else:
        lst.remove(i)

def contain(s):
    for i in lst:
        if i.find(s):
            return False
        else:
            return True

if contain(s):
    print(i.removesuffix(s))
else: