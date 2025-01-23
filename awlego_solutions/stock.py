# stock.py
import csv

from typing import List, Type

import csv
from decimal import Decimal
from reader import read_csv_as_instances

class Stock:
    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value

    @property 
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value
    
    def sell(self, shares):
        self.shares -= shares

class DStock(Stock):
    _types = (str, int, Decimal)

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

def read_portfolio(csv_filepath: str, cls=Stock) -> List["Stock"]:
    '''exercise 3.3'''
    with open(csv_filepath, 'r') as file:
        portfolio = csv.reader(file)
        headers = next(portfolio)
        stocks = [Stock.from_row(row) for row in portfolio]
    return stocks

def print_portfolio(portfolio: List["Stock"]) -> None: 
    print('%10s %10s %10s' % ("Name", "Shares", "Price"))
    print('%10s %10s %10s' % ("--------", "--------", "--------"))

    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == "__main__":
    # # 3.1a
    # s = Stock('GOOG',100,490.10)
    # print(s.shares)
    # s.sell(25)
    # print(s.shares)

    # portfolio = read_csv_as_instances('../Data/portfolio.csv', Stock)
    # assert(s.shares == 75)

    # portfolio = read_portfolio("../Data/portfolio.csv")
    # for s in portfolio:
    #     print(s)

    # print_portfolio(portfolio)

    # ## 3.3
    # s = DStock.from_row(['GOOG', 100, 490.10])
    # print(s.name, type(s.name))
    # print(s.shares, type(s.shares))
    # print(s.price, type(s.price))

    # portfolio = read_portfolio("../Data/portfolio.csv")
    # for s in portfolio:
    #     print(s)

    # # 3.4
    # s = Stock('GOOG', 100, 490.10)
    # print(s.cost)
    # # s.spam = 10 # should error
    # s.price = 93.2
    # # s.price = Decimal('93.2') # should error


    # s = DStock('GOOG', 100, Decimal('490.10'))
    # s.price = Decimal('93.2')
    # print(s.price)
    # s.price = 93.2 # should type error
    pass

