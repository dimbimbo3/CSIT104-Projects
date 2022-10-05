x = float(input("Enter the x-coordinate of the point:"))
y = float(input("Enter the y-coordinate of the point:"))
xDistance = (x*x)/2
yDistance = (y*y)/2

if(xDistance <= (10/2) and yDistance <= (5/2)):
    print("Point (",x,", ",y,") is in the rectangle")
else:
    print("Point (",x,", ",y,") is not in the rectangle")
