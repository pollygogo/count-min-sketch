from math import exp
from math import log2
import random
import numpy as np

class CountMinSketch:
    def __init__(self, p, error_rate, failure_probability):
        self.p = p
        self.error_rate = error_rate
        self.failure_probability = failure_probability
        self.w = int(exp(1)/self.error_rate)
        self.d = int(log2(1/self.failure_probability))
        self.table = np.zeros((self.d, self.w), dtype=int)
        self.a = random.sample(range(1,self.p), self.d)
        self.b = random.sample(range(1,self.p), self.d)
    
    '''
    The number of hash functions needed for CMS is equal to the number of rows (d) in the table.
    This function generates d hash functions based on the formula: (a*h + b) % p % w, where p is
    a prime number greater than the largest value of the integer representation of the item, w is
    the width of the table, and a and b are random numbers between 1 and p. The function returns
    the hash values of the item.
    '''
    def hash_function(self, h): 
        hashed_values = []
        for i in range(self.d):
            v = ((self.a[i]*h + self.b[i]) % self.p) % self.w
            hashed_values.append(v)
        return hashed_values
    
    # to increment the count of the item
    def update(self, h):
        hashed_values = self.hash_function(h)
        for row, col in enumerate(hashed_values):
            self.table[row, col] += 1
    
    # to query the count of the item
    def query(self, h):
        hashed_values = self.hash_function(h)
        return min(self.table[row][col] for row, col in enumerate(hashed_values))
    
    
    



