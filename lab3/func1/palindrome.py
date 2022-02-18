def isPal(ss):
    left_pos = 0
    right_pos = len(ss) - 1
    
    while right_pos >= left_pos:
        if not ss[left_pos] == ss[right_pos]:
            print('false')
        left_pos += 1
        right_pos -= 1
    print('true')

if __name__ == '__main__':
    ss = input()
    isPal(ss)

