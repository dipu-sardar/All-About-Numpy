prices = [100, 200, 300]

discount = 20 #10% doscount 

final_prices = []

for price in prices:
    final_price = price - (price * discount/100)
    final_prices.append(final_price)

print(final_prices)