

def countr(ss):
    cnt = 0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            cnt = cnt + 1
    return cnt

s = input()
ss = s.lower()
print(int(countr(ss)))









