# pcost.py

filename = "../data/portfolio.dat"
bad_data = "../data/portfolio3.dat"
portfolio2 = "../data/portfolio2.dat"

def portfolio_cost(filename):
    total_price = 0
    with open(filename) as openfile:
        for line in openfile:
            try:
                stock_name = line.split()[0]
                num_shares = float(line.split()[1])
                purchase_price = float(line.split()[2])
            except ValueError as error:
                print("WARNING couldn't parse: ", line.strip())
                print("Reason: ", error)
                continue
            total_price += num_shares * purchase_price
        
    return total_price

if __name__ == "__main__":
    print(portfolio_cost(filename))
    print(portfolio_cost(bad_data))
    print(portfolio_cost(portfolio2))



