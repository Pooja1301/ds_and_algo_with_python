import sys
def repeatedNumber(A):
    count1 = 0
    count2 = 0
    first = max(A)
    second = max(A)

    for i in range(0, len(A)):

        if (first == A[i]):
            count1 += 1

        elif (second == A[i]):
            count2 += 1

        elif (count1 == 0):
            count1 += 1
            first = A[i]

        elif (count2 == 0):
            count2 += 1
            second = A[i]

        else:
            count1 -= 1
            count2 -= 1

    count1 = 0
    count2 = 0

    for i in range(0, len(A)):
        if (A[i] == first):
            count1 += 1

        elif (A[i] == second):
            count2 += 1

    if (count1 > len(A) / 3):
        return first

    if (count2 > len(A) / 3):
        return second

    return -1

A=[1,2,3,1,1]
print(repeatedNumber(A))