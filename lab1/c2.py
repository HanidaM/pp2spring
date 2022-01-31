s = input()


def tolower(s):
    a = ""
    for i in s:
        if "A" <= i <= "Z":
            a += chr(ord(i) + 32)

        else:
            a += i

    print(a)


tolower(s)
