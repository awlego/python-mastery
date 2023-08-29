# readport.py

import csv
from pprint import pprint
import readrides
from collections import defaultdict
from collections import Counter

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio

def exploration():
    # comprehensions exploration
    print("comprehensions: ")
    portfolio = read_portfolio('../Data/portfolio.csv')
    pprint(portfolio)
    print([s for s in portfolio if s['shares'] > 100])
    print(sum([s['shares']*s['price'] for s in portfolio]))
    print({ s['name'] for s in portfolio })
    totals = { s['name']: 0 for s in portfolio }
    for s in portfolio:
        totals[s['name']] += s['shares']
    print(totals)

    print("\nCollections: ")
    # collections explorations
    totals = Counter()
    for s in portfolio:
        totals[s['name']] += s['shares']
    print(totals)
    print(totals.most_common(2))
    more = Counter()
    more['IBM'] = 75
    more['AA'] = 200
    more['ACME'] = 30
    print(more)
    print(totals)
    print(totals + more)

    byname = defaultdict(list)
    for s in portfolio:
        byname[s['name']].append(s)
    print(byname['IBM'])


def how_many_rode_the_bus(records, query_date):
    daily_riders = defaultdict(int)
    for record in records:
        daily_riders[record.date] += record.rides
    return daily_riders[query_date]

def rides_by_route(records):
    rides_by_route = defaultdict(int)
    for record in records:
        rides_by_route[record.route] += record.rides
    return rides_by_route
    
def find_biggest_growth(records, num_routes=5, year1=2001, year2=2011):
    year_1_rides = defaultdict(int)
    year_2_rides = defaultdict(int)
    for record in records:
        record_year = int(record.date.split("/")[2])
        if record_year == year1:
            year_1_rides[record.route] += record.rides
        if record_year == year2:
            year_2_rides[record.route] += record.rides

    growth = Counter(year_2_rides) - Counter(year_1_rides)
    # most common sorts it
    # print(growth.most_common()[-1*num_routes:]) #smallest growth just for fun -- looks like there was no negative growth here
    return(growth.most_common()[0:num_routes])

if __name__ == "__main__":
    # exploration()
    records = readrides.read_rides_as_class_with_slots("../Data/ctabus.csv")

    unique_routes = set({record.route for record in records})
    num_unique_routes = len(unique_routes)
    print("Number unique routes in Chicago: ", num_unique_routes)

    print(how_many_rode_the_bus(records, "02/02/2001"), "people road the bus on February 2, 2011")
    print(how_many_rode_the_bus(records, "03/02/2001"), "people road the bus on March 2, 2011")
    print(how_many_rode_the_bus(records, "04/02/2001"), "people road the bus on April 2, 2011")

    print("Rides taken by route:")
    pprint(rides_by_route(records))

    print("Biggest growth:")
    print(find_biggest_growth(records))