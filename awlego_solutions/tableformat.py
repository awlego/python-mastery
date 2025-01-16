import stock
from typing import List

def print_table(objects: List, names: List):
    header_str = ""
    for name in names:
        header_str += '%10s ' % name
    print(header_str)
    print('%10s %10s %10s' % ("-"*10, "-"*10, "-"*10))
    for obj in objects:
        row_str = ""
        for name in names:
            row_str += '%10s ' % getattr(obj, name)
        print(row_str)
    return


if __name__ == "__main__":
    portfolio = stock.read_portfolio('../Data/portfolio.csv')  
    print_table(portfolio, ['name','shares','price'])
    print_table(portfolio, ['shares','name'])