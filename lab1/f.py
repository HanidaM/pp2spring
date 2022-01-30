lst = []

n = int(input())

for i in range(0, n):
    nums = int(input())

    lst.append(nums)
for i in lst:
    if i <= 10:
        print("Go to work!")
    elif 10 <= i <= 25:
        print("You are weak")
    elif 25 <= i <= 45:
        print("Okay, fine")
    elif i > 45:
        print("Burn! Burn! Burn Young!")
