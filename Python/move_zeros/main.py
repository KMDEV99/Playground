"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""


def move_zeros(arr):
    length = len(arr)
    res_arr = [0] * length
    index = 0

    for item in arr:
        if item is not 0 and not isinstance(item, float):
            res_arr[index] = item
            index += 1
    return res_arr
