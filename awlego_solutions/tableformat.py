import stock
import reader
from typing import List
from abc import ABC, abstractmethod


class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    
    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        header_str = ",".join(h for h in headers)
        print(header_str)
    
    def row(self, rowdata):
        row_str = ",".join(str(d) for d in rowdata)
        print(row_str)       

class HTMLTableFormatter(TableFormatter):
    def __init__(self):
        self.pre_str = "<tr> <th>"
        self.post_str = "</th> </tr>"

    def headings(self, headers):
        header_str = ""
        for h in headers:
            header_str += self.pre_str + h + self.post_str
        print(header_str)
    
    def row(self, rowdata):
        row_str = self.pre_str + "" + self.post_str.join(str(d) for d in rowdata)
        print(row_str)

def create_formatter(format_type):
    if format_type == "text":
        return TextTableFormatter()
    elif format_type == "csv":
        return CSVTableFormatter()
    elif format_type == "html":
        return HTMLTableFormatter()
    else:
        raise ValueError(f"Unknown format: {format_type}")

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

def print_table(records, fields, formatter):
    '''3.5 print_table'''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

def raises(exception_type, func, *args, **kwargs):
    """Test if a function call raises an exception"""
    try:
        func(*args, **kwargs)
        return False
    except exception_type:
        return True
    except Exception as e:
        return False
    
class NewFormatter(TableFormatter):
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

if __name__ == "__main__":
    # portfolio = stock.read_portfolio('../Data/portfolio.csv')  
    # print_table(portfolio, ['name','shares','price'])
    # print_table(portfolio, ['shares','name'])

    # # 3.5
    # portfolio = reader.read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    # formatter = TextTableFormatter()
    # print_table(portfolio, ['name','shares','price'], formatter)

    # formatter = CSVTableFormatter()
    # print_table(portfolio, ['name','shares','price'], formatter)

    # formatter = HTMLTableFormatter()
    # print_table(portfolio, ['name','shares','price'], formatter)

    # 3.7
    portfolio = reader.read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

    assert raises(TypeError, print_table, portfolio, ['name','shares','price'], MyFormatter())
    print_table(portfolio, ['name','shares','price'], create_formatter('text'))

    # f = NewFormatter()


