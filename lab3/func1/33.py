



def has_33(lst):
    for i in lst:
        if lst[i] and lst[i+1] == 3:
            return True
        else: return False

lst = list(map(int, input().split()))
print(has_33(lst))
