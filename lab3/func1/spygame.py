

def spy_game(lst):
    for x in lst:
        if x == 0 and x+1 == 0 and x+2 == 7:
            print('true')
        else: 
            print('false')   


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    spy_game(lst)

