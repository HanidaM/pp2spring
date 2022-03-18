import numpy

#loop wersion
def prod(lst1):
    result = 1
    for x in lst1:
         result = result * x
    return result

if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5]

#numpy versions
print(numpy.prod(lst1))

print(prod(lst1))



