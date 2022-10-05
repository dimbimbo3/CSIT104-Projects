userInt = int(input("Enter an integer (the input exits if the input is 0): "))
positive = 0
negative = 0

total = 0
count = 0
avg = 0

# Keep reading data until the input is 0
while (userInt != 0): 
    total += userInt
    count += 1
    
    if(userInt > 0):
        positive += 1
    else:
        negative += 1
        
    userInt = int(input("Enter an integer (the input exits if the input is 0): "))

if(count != 0):
    avg = total / count
    print("The number of positives is ", positive)
    print("The number of negatives is ", negative)
    print("The total is ", total)
    print("The average is ", avg)
else:
    print("No numbers are entered except 0")
