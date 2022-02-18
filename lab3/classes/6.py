def prime_num(num):   
    prime = True
    is_prime = lambda a, b: a % b == 0
    for i in range (2, num):
        if(is_prime(num, i)):
            prime = False
            break
    return prime



if __name__ == "__main__":
    user_input = int(input())
    lst = []
    for i in range(user_input):
        s = int(input())
        lst.append(int(i))
        lst2 = list(filter(prime_num, lst))

print(lst2)