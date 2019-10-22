"""
Given a non-negative number in an array
add 1 to the number
Most significant digit is at the starting position of array
e.g. : [1,2,3]
output: [1,2,4]
"""

def plusOne(A):
    A[-1] += 1
    carry = A[-1] / 10
    A[-1] = A[-1] % 10

    n = len(A)
    for i in range(n - 2, -1, -1):
        if (carry == 1):
            A[i] += 1
            carry = A[i] / 10
            A[i] = A[i] % 10

    if carry == 1:
        A.insert(0, 1)

    i = 0
    while (A[i] == 0):
        A.pop(0)
    return A

print(plusOne([9,9,9]))