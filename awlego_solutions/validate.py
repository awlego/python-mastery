# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
    
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
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
        PositiveFloat.check(value)
        self._price = value

    @property 
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        PositiveInteger.check(value)
        self._shares = value
    
    def sell(self, shares):
        self.shares -= shares
    
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, other.price))


if __name__ == "__main__":
    goog = Stock("GOOG", 100, 490.10)
    print(goog.shares)
    goog.shares = 100
    print(goog.shares)
    goog.shares = -100 # should fail
    print(goog.shares)
