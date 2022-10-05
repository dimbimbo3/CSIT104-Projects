year = int(input("Enter year (e.g. 2008):"))
month = int(input("Enter month (1-12):"))
mDay = int(input("Enter the day of the month (1-31):"))

if (month == 1):
    month = 13
    year -= 1
elif (month == 2):
    month = 14
    year -= 1

q = mDay
m = month
j = year // 100
k = year % 100
h = (q + 26*(m+1)//10 + k + k//4 + j//4 +5*j) % 7

if (h == 0):
    wDay = "Saturday"
elif (h == 1):
    wDay = "Sunday"
elif (h == 2):
    wDay = "Monday"
elif (h == 3):
    wDay = "Tuesday"
elif (h == 4):
    wDay = "Wednesday"
elif (h == 5):
    wDay = "Thursday"
elif (h == 6):
    wDay = "Friday"

print("Day of the week is", wDay)
