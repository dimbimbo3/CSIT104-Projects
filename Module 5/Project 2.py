letter = input("Enter a letter grade:")
valid = True

if(letter.upper() == "A"):
    grade = 4
elif(letter.upper() == "B"):
    grade = 3
elif(letter.upper() == "C"):
    grade = 2
elif(letter.upper() == "D"):
    grade = 1
elif(letter.upper() == "F"):
    grade = 0
else:
    valid = False

if(valid):
    print("The numeric value for grade ", letter, " is ", grade)
else:
    print(letter, " is an invalid grade")
