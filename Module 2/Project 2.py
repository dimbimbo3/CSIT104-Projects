minutes = int(input("Enter the number of minutes:"))
years = int(minutes / 525600)
remainder = minutes % 525600
days = int(remainder / 1440)
print(minutes," minutes is approximately ", years, " years and ", days, " days")
