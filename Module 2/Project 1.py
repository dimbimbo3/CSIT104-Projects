subTotal = float(input("Enter the subtotal:"))
gratuityRate = float(input("Enter the gratuity:"))
gratuity = (subTotal * gratuityRate) / 100
total = subTotal + gratuity
print("The gratuity is ", gratuity, " and the total is ", total)
