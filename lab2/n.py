a = list() 

while True: 
     n = int(input()) 
     if n == 0: 
         break 
     else: 
         a.append(n)

for i in range((len(a) // 2) + 1): 
    if i == len(a) - i: 
        print(a[i]) 
    else: 
        print(a[i] + a[-1 - i]) 
