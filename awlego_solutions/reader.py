# reader.py
import csv
from collections import namedtuple
import collections
import collections.abc
from abc import ABC, abstractmethod
import csv
import stock
from typing import Iterable
import gzip

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) 
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records


def csv_as_dicts(lines: Iterable, types, headers: list[str] | None = None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records

def csv_as_instances(lines: Iterable, cls: type, headers: list[str] | None = None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


    
if __name__ == "__main__":
    # port = read_csv_as_dicts('../Data/portfolio.csv', [str, int, float])
    # print(port)
    # port = read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    # print(port)
    # file = open('../Data/portfolio.csv')
    # port = csv_as_dicts(file, [str, int, float])
    # print(port)
    file = gzip.open('../Data/portfolio.csv.gz', 'rt')
    port = csv_as_instances(file, stock.Stock)