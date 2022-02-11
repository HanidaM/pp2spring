n = int(input())  
a = list(map(int,input().strip().split()))[:n] 

a.sort(reverse=True)

print(a[0]*a[1])

