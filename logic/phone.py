from logic.utils import db_utils

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

