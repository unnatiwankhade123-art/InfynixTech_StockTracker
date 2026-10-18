# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

portfolio = {}

print("Welcome to Stock Portfolio Tracker")

while True:
    stock = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity purchased: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Display portfolio summary
total_value = 0

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    print(
        f"{stock}: {quantity} shares = ${value}"
    )

print("-----------------------------")
print(f"Total investment value: ${total_value}")

# Save results to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares = ${value}\n"
        )

    file.write(f"Total investment value: ${total_value}\n")

print("Portfolio saved to portfolio.txt")