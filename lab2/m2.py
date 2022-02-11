t=False
a=[]
while True:
    n=input()
    if  len(n)==1 and n[0]=="0":
        t=True
        break
    a.append(n.split())
for i in a:
     i.reverse()
a.sort()
for i in a:
    i.reverse()
    print(*i)