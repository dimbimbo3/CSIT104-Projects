import math

sNum = int(input("Enter the number of sides:"))
sLen = float(input("Enter the side:"))

area = (sNum * sLen**2) / (4 * (math.sin(math.pi / sNum) / math.cos(math.pi / sNum)))

print("The area of the polygon is", area)
