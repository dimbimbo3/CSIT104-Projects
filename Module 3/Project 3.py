month = int(input("Enter a month in the year (e.g, 1 for Jan):"))
year = int(input("Enter a year:"))

if(month == 1):
    days = 31
    mon = "January"
elif(month == 2):
    if(year % 4 == 0 and year % 100 != 0):
        days = 29
    else:
        days = 28
    mon = "February"
elif(month == 3):
    days = 31
    mon = "March"
elif(month == 4):
    days = 30
    mon = "April"
elif(month == 5):
    days = 31
    mon = "May"
elif(month == 6):
    days = 30
    mon = "June"
elif(month == 7):
    days == 31
    mon = "July"
elif(month == 8):
    days = 31
    mon = "August"
elif(month == 9):
    days = 30
    mon = "September"
elif(month == 10):
    days = 31
    mon = "October"
elif(month == 11):
    days = 30
    mon = "November"
elif(month == 12):
    days = 31
    mon = "December"

print(mon," ", year, " has ", days, " days")
