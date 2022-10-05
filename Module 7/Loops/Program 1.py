firstNum = int(input("Enter a number:"))
ascend = True

for i in range(1, 6):
    secondNum = int(input("Enter a number:"))
    if firstNum > secondNum:
        ascend = False
        break
    firstNum = secondNum
    
print(ascend)
