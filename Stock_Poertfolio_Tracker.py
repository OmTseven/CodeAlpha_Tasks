import yfinance as yf

# Initialize the portfolio as an empty list
portfolio = []

def add_stock():
    """
    Add a stock to the portfolio or update an existing one.
    """
    symbol = input("Enter stock symbol: ").upper()
    try:
        ticker = yf.Ticker(symbol)
        # Check if the symbol is valid by accessing its current price
        price = ticker.info['currentPrice']
        shares = int(input("Enter number of shares: "))
        # Check if the symbol is already in the portfolio
        for item in portfolio:
            if item['symbol'] == symbol:
                item['shares'] += shares
                print(f"Updated {symbol} to {item['shares']} shares.")
                return
        # Add new stock to the portfolio
        portfolio.append({'symbol': symbol, 'shares': shares})
        print(f"Added {shares} shares of {symbol}.")
    except KeyError:
        print("Invalid stock symbol.")
    except ValueError:
        print("Invalid number of shares. Please enter an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_stock():
    """
    Remove a stock from the portfolio.
    """
    symbol = input("Enter stock symbol to remove: ").upper()
    for item in portfolio:
        if item['symbol'] == symbol:
            portfolio.remove(item)
            print(f"Removed {symbol} from portfolio.")
            return
    print(f"{symbol} not found in portfolio.")

def view_portfolio():
    """
    Display the current portfolio with stock values and total portfolio value.
    """
    if not portfolio:
        print("Portfolio is empty.")
        return
    symbols = ' '.join([item['symbol'] for item in portfolio])
    try:
        tickers = yf.Tickers(symbols)
        total_value = 0
        print("Portfolio:")
        for item in portfolio:
            symbol = item['symbol']
            shares = item['shares']
            price = tickers.tickers[symbol].info['currentPrice']
            value = shares * price
            total_value += value
            print(f"{symbol}: {shares} shares @ ${price:.2f} each, total ${value:.2f}")
        print(f"Total portfolio value: ${total_value:.2f}")
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")

# Main program loop
while True:
    print("\n1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_stock()
    elif choice == '2':
        remove_stock()
    elif choice == '3':
        view_portfolio()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")