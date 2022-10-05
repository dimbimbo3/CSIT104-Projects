investmentAmount = float(input("Enter investment amount:"))
annualInterestRate = float(input("Enter annual interest rate:"))
monthlyInterestRate = (annualInterestRate/100) / 12
print("Monthly Interest Rate:", monthlyInterestRate)
numberOfYears = int(input("Enter the number of years:"))
numberOfMonths = numberOfYears * 12
print("Number of Months", numberOfMonths)
futureInvestmentAmount = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)
print("Accumulated value is ", futureInvestmentAmount)
