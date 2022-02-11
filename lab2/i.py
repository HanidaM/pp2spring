n = int(input())

arr_1 = [] 
arr_2 = [] 
arr_3 = [] 

for i in range(n): 
    diski = input() 
    if diski[0] == "1": 
        arr_1.append(diski[2:]) 
    elif diski[0] == "2": 
        arr_2.append(diski[:2]) 
 
 
x=arr_2.count("2") 
 
arr_3.append(arr_1[:x]) 
 
for j in arr_3: 
    print(*j)