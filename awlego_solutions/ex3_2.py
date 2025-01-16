import stock
import tableformat
portfolio = stock.read_portfolio('../Data/portfolio.csv')
tableformat.print_table(portfolio, ['name','shares','price'])
tableformat.print_table(portfolio, ['name','shares'])

s = stock.Stock('GOOG', 100, 490.10)
print(s.cost)
print(s.cost())
f = s.sell
f.__func__(f.__self__, 25)
print(s.shares)
