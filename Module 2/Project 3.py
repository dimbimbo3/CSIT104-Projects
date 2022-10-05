userInt = int(input("Enter an integer"))
while(userInt > 0):
    last = userInt % 10
    userInt //= 10
    print(last)
    
