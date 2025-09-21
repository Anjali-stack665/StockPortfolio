# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOGL": 140,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks with prices:", stock_prices)

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print(" Stock not available in the list.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Store in portfolio
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} - Quantity: {qty}, Value: ${value}")

print(f"\n Total Investment Value: ${total_investment}")

# Option to save result
save_option = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()

if save_option == "yes":
    file_choice = input("Save as 'txt' or 'csv'? ").lower()
    
    if file_choice == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock} - Quantity: {qty}, Value: ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment: ${total_investment}")
        print("Portfolio saved to portfolio.txt")

    elif file_choice == "csv":
        import csv
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock] * qty])
            writer.writerow(["Total", "", total_investment])
        print(" Portfolio saved to portfolio.csv")
    else:
        print(" Invalid choice. File not saved.")
