"""
Given an array of integers, find out the maximum sum of subarray of non negative numbers
from given array
e.g.: Input : [1,2,5,-7,2,3]
output : [1,2,5]
"""

def max_sum_subarray(A):
    _max = []
    _temp = []
    i = 0

    while i < len(A):
        if A[i] >= 0:
            _temp.append(A[i])

            if sum(_max) == sum(_temp):
                if len(_max) < len(_temp):
                    _max = _temp
            elif sum(_max) < sum(_temp):
                _max = _temp
        else:
            _temp = []
        i += 1
    return _max
print(max_sum_subarray([1,2,5,-7,2,3]))
