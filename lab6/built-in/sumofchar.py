string = input("Enter a stroing: ")
upper = 0
lower = 0

for i in string:
    if(i.isupper()):
        upper = upper + 1
    elif(i.islower()):
        lower = lower + 1

print("Count of upper: ", upper)
print("count of lower: ", lower) 