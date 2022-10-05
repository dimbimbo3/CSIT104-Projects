import math

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

discrim = b**2 - (4*a*c)

if(discrim > 0):
    r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    print("The roots are ", r1, " and ", r2)
elif(discrim == 0):
    r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    print("The root is ", r1)
else:
    print("The equation has no real roots")
    
