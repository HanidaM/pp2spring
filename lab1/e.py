a, b = map(int, input().split())


def isprime(a):
    for i in range(2, a):
        if (a % i) == 0:
            return False
    else:
        return True


if isprime(a) and a < 500 and b % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")
