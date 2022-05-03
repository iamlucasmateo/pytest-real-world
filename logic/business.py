class Phonebook:
    def __init__(self):
        self.entries = {}
    
    def add(self, name, number):
        self.entries[name] = number
    
    def lookup(self, name):
        return self.entries[name]
    
    @property
    def names(self):
        return self.entries.keys()


class Company:
    def __init__(self, name: str, stock_symbol: str = "GENERIC"):
        self.name = name
        self.stock_symbol = stock_symbol
    
    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"