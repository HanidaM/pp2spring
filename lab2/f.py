n = int(input())
d = {}


for i in range(n):
    name, comp = input().split()
    comp = int(comp)
    d[name] = d.get(name, 0) + comp

mx = max(d.values())

for name, comp in sorted(d.items(), key=lambda x:(x[1])):
    if mx - d[name] == 0:
        print(f"{name} is lucky!")
    else:
        print(f"{name} has to receive {mx - d[name]}")