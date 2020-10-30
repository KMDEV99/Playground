"""
Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.
"""


def solution(array_a, array_b):
    res = 0
    for val1, val2 in zip(array_a, array_b):
        res += pow(val1 - val2, 2)
    return res / len(array_a)
