def histogram(list):
        for i in range(0,len(list)):
                print('*' * list[i])
        return

        
if __name__ == '__main__':
    li = list(map(int, input().split()))

    histogram(li)