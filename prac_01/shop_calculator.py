"""
Program to calculate the price of n items
If the total is over $100 a 10% discount is applied
"""

price = 0

while True:
    numItems = int(input("Number of items: "))
    if numItems < 0:
        print("Invalid number of items!")
    else:
        break

for i in range(numItems):
    price = price + float(input("Price of item %i: " % (i+1)))

if price > 100:
    price = price * 0.9

print("The total price for %i items is $%.2f" % (numItems, price))
