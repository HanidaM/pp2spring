n = int(input())
lst = []


def delmail(n):
    for i in range(n):
        lst.append(input())

    for i in range(len(lst)):
        q = lst[i].endswith("@gmail.com")
        if q == 1:
            print(lst[i][:-10])


delmail(n)