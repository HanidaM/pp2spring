words = input() 
s = '' 
res = set() 

for i in range(len(words)): 
    if words[i].isalpha(): 
        s += words[i] 
    elif words[i] == ' ' or i == len(words) - 1: 
        res.add(s) 
        s = '' 
print(len(res)) 
print(*sorted(res),sep='\n')
