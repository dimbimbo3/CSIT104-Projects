userScores = input("Enter scores:")
scores = userScores.split()
grades = []
best = int(scores[0])

#Get best score
for i in range(len(scores)):
    if(int(scores[i]) > best):
        best = int(scores[i])

#Get grades
for x in range(len(scores)):
    if(int(scores[x]) >= (best - 10)):
        grades.append("A")
    elif(int(scores[x]) >= (best - 20)):
        grades.append("B")
    elif(int(scores[x]) >= (best - 30)):
        grades.append("C")
    elif(int(scores[x]) >= (best - 40)):
        grades.append("D")
    else:
        grades.append("F")
        
    print("Student",x,"score is",scores[x],"and grade is",grades[x])
