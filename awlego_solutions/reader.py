# reader.py
import csv
from collections import namedtuple
import collections
import collections.abc

def type_a_row(row, types):
    return list(zip(types, row))

def read_csv_as_dicts(filename, coltypes):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        for row in rows:
            row_record = { name:func(val) for name, func, val in zip(headers, coltypes, row) }
            records.append(row_record)
        return records

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

class DataCollection(collections.abc.Sequence):

    def __init__(self):
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


def read_csv_as_columns(filename, coltypes):
    records = DataCollection()
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        for row in rows:
            row_record = { name:func(val) for name, func, val in zip(headers, coltypes, row) }
            records.append(row_record)
        return records

if __name__ == "__main__":
    import tracemalloc
    from sys import intern

    ## 2_6 part 1
    # portfolio = read_csv_as_dicts('../Data/portfolio.csv', [str,int,float])
    # for s in portfolio:
    #     print(s)

    # ctabus_data = read_csv_as_dicts('../Data/ctabus.csv', [str,str,str,int])
    # print(len(ctabus_data))
    # routes = { row['route'] for row in ctabus_data }
    # print(len(routes))
    # routeids = { id(row['route']) for row in ctabus_data }
    # print(len(routeids))

    ## 2_6 part 2
    # tracemalloc.start()
    # rows = read_csv_as_dicts('../Data/ctabus.csv', [str, str, str, int])
    # routeids = { id(row['route']) for row in rows }
    # print(len(routeids))
    # print(tracemalloc.get_traced_memory())

    # tracemalloc.reset_peak()
    # rows = read_csv_as_dicts('../Data/ctabus.csv', [intern, str, str, int])
    # routeids = { id(row['route']) for row in rows }
    # print(len(routeids))
    # print(tracemalloc.get_traced_memory())
    
    # tracemalloc.reset_peak()
    # rows = read_csv_as_dicts('../Data/ctabus.csv', [intern, intern, str, int])
    # routeids = { id(row['route']) for row in rows }
    # print(len(routeids))
    # print(tracemalloc.get_traced_memory())

    ## 2_6 part 3
    data = read_csv_as_columns('../Data/ctabus.csv', coltypes=[str, str, str, int])
    print(type(data))
    print(len(data))
    print(data[0])
    print(data[1])
    print(data[2])