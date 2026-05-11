stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 140}

total_investment = 0

for stock, price in stocks.items():
    quantity = int(input(f"Enter quantity for {stock}: "))
    total_investment += quantity * price

print("\nTotal Investment Value:", total_investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: {total_investment}")