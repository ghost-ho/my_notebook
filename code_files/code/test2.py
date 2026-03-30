import numpy as np

def condition_generator(n):
    def condition(t):
        return t + n
    return condition
result = 0
