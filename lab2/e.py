
n, x = map(int, input().split())
arr = [1000]
def xorOfArr(arr, n):
    xor_arr = 0

    for i in range(n):
        xor_arr = xor_arr ^ arr[i]
    
    return xor_arr

if __name__ == '__main__':
   
    for i in range(n):
        arr[i] = x + 2 * i
        arr.append(arr[i])

print(xorOfArr(arr, n))
    
