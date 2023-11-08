price = 250

if price >= 300:
    price *= 0.7  # (1 - 0.3)
elif price >= 200:
    price *= 0.8  # (1 - 0.2)
elif price >= 100:
    price *= 0.9  # (1 - 0.1)
elif price < 100 and price >= 0:
    price *= 0.95  # (1 - 0.05)

print(price)

#2nd method of doing above problem
price = float(input("Enter the price: "))

if price < 0:
    discount = 0  # No discount for negative prices
elif price >= 300:
    discount = 0.3  # 30% discount for prices of 300 or above
elif price >= 200:
    discount = 0.2  # 20% discount for prices between 200 and 299
elif price >= 100:
    discount = 0.1  # 10% discount for prices between 100 and 199
else:
    discount = 0.05  # 5% discount for prices less than 100

discounted_price = price - (price * discount)
print(f"Discounted Price: {discounted_price:.2f}")
