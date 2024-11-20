# stock.py
import csv

from typing import List, Type

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(csv_filepath: str) -> List["Stock"]: 
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    with open(csv_filepath, 'r') as file:
        portfolio = csv.reader(file)
        headers = next(portfolio)

        rows = (dict(zip(headers,row)) for row in portfolio)
        stocks = [Stock(str(row["name"]), float(row["shares"]), float(row["price"])) for row in rows]
        
    return stocks

def print_portfolio(portfolio: List["Stock"]) -> None: 
    print('%10s %10s %10s' % ("Name", "Shares", "Price"))
    print('%10s %10s %10s' % ("--------", "--------", "--------"))

    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == "__main__":
    # 3.1a
    s = Stock('GOOG',100,490.10)
    print(s.shares)
    s.sell(25)
    print(s.shares)
    assert(s.shares == 75)

    portfolio = read_portfolio("../Data/portfolio.csv")
    for s in portfolio:
        print(s)

    print_portfolio(portfolio)