# readrides.py

import csv
from dataclasses import dataclass
from collections import namedtuple
import collections

class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []
        
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if type(index) is not int:
            if index.step == None:
                step = 1
            else:
                step = index.step
            result = []
            for i in range(index.start, index.stop, step):
                result.append(self.__getitem__(i))
            return result
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


# A class
class RowClass:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A named tuple
RowNamedTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# A class with __slots__
class RowClassWithSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dictionary(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(row)
    return records

def read_rides_as_dictionary_with_columns(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = RideData()      # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(row)
    return records

def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = RowNamedTuple(route, date, daytype, rides)
            records.append(row)
    return records

def read_rides_as_class(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = RowClass(route, date, daytype, rides)
            records.append(row)
    return records

def read_rides_as_class_with_slots(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = RowClassWithSlots(route, date, daytype, rides)
            records.append(row)
    return records

# A class made using @dataclass
@dataclass
class RowDataClass:
    route: int
    date: str
    daytype: chr
    rides: int

def read_rides_as_dataclass(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = RowDataClass(route, date, daytype, rides)
            records.append(row)
    return records

# A class made using @dataclass
@dataclass(slots=True)
class RowDataClassWithSlots:
    route: int
    date: str
    daytype: chr
    rides: int

def read_rides_as_dataclass_with_slots(filename):
    '''
    Read the bus ride data as dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row = RowDataClassWithSlots(route, date, daytype, rides)
            records.append(row)
    return records

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

def test_slicing():
    rows = read_rides_as_dictionary_with_columns('../Data/ctabus.csv')
    print(rows[0])
    print(rows[0:10])



if __name__ == '__main__':

    test_slicing()
    # exit()

    f = open('../Data/ctabus.csv')
    data = f.read()
    print("File size: ", len(data)/1000000, "MB")

    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Tuple Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_dictionary('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Dictionary Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_class('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Class Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_named_tuple('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Named tuple Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_class_with_slots('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Class with __slots__ Memory Use: Current {peak_MB}MB, {current_MB}MB')
    
    tracemalloc.reset_peak()
    rows = read_rides_as_dataclass('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Dataclass Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_dataclass_with_slots('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'Dataclass with slots Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_columns('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'reading as columns Memory Use: Current {peak_MB}MB, {current_MB}MB')

    tracemalloc.reset_peak()
    rows = read_rides_as_dictionary_with_columns('../Data/ctabus.csv')
    peak, current = tracemalloc.get_traced_memory()
    peak_MB = peak/1000000
    current_MB = current/1000000
    print(f'reading as dictionary with columns Memory Use: Current {peak_MB}MB, {current_MB}MB')

# results:
# python readrides.py
# File size:  12.361039 MB
# Tuple Memory Use: Current 123.688774MB, 123.719176MB
# Dictionary Memory Use: Current 0.164294MB, 339.818082MB
# Class Memory Use: Current 0.008201MB, 169.926634MB
# Named tuple Memory Use: Current 0.004437MB, 128.343262MB
# Class with __slots__ Memory Use: Current 0.005384MB, 119.103201MB
# Dataclass Memory Use: Current 0.011331MB, 169.929764MB
# Dataclass with slots Memory Use: Current 0.007422MB, 119.105239MB

