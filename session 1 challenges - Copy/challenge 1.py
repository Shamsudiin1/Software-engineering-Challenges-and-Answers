orangesPrice = float(input("What is the price of the oranges?"))

percentageDiscount = float(input("What is the percentage discount?"))

discountedPrice = orangesPrice - orangesPrice * percentageDiscount / 100

print("The discounted price of the oranges is "+ str(discountedPrice))
