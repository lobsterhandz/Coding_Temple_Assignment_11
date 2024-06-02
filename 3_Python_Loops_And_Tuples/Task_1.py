# Sample Data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-03", 135.0),
    ("MSFT", "2021-01-02", 225.0),
    ("AAPL", "2021-01-04", 137.0),
]

def calculate_average_closing_price(stock_data, stock_symbol):
    
    total_price = 0
    count = 0
    
    # Iterate through each data point in the stock data
    for data in stock_data:
        symbol, date, closing_price = data
        
        # Check if the stock symbol matches the specified symbol
        if symbol == stock_symbol:
            total_price += closing_price
            count += 1
            
    # Calculate the average closing price
    if count == 0:
        return None  # If no data points were found, return None
    average_price = total_price / count
    return average_price

# Example usage
stock_symbol = "AAPL"
average_price = calculate_average_closing_price(stock_data, stock_symbol)
if average_price is not None:
    print(f"The average closing price of {stock_symbol} is: {average_price:.2f}")
else:
    print(f"No data found for stock symbol {stock_symbol}")
