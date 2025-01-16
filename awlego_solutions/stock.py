# stock.py
import csv

from typing import List, Type

import csv
from decimal import Decimal
from reader import read_csv_as_instances

class Stock:
    types = (str, int, Decimal)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price
    
    def sell(self, shares):
        self.shares -= shares

def read_portfolio(filename):
    portfolio = []
    with open(filename) as csv_file:
        rows = csv.reader(csv_file)
        headers = next(rows)
        for (name, shares, price) in rows:
            portfolio.append(Stock.from_row([name, shares, price]))
    return portfolio

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

    # portfolio = read_portfolio("../Data/portfolio.csv")
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    assert(s.shares == 75)

    portfolio = read_portfolio("../Data/portfolio.csv")
    for s in portfolio:
        print(s)

    print_portfolio(portfolio)