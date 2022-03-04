from cmath import acos, asin, tan
from math import pi, radians


n = int(input("Number of sides: "))
m = int(input("Length of a side: "))

area = (n * (pow(m, 2)) / (4 * tan(pi / n)))

print("Area of polygon: ", )