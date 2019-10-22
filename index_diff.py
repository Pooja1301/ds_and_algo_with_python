def maxIndexDiff(A):
    n = len(A)
    LMin = [0] * n
    RMax = [0] * n

    LMin[0] = A[0]
    for i in range(1, n):
        LMin[i] = min(A[i],LMin[i-1])

    RMax[0] = A[n-1]
    for i in range(n-2, -1, -1):
        RMax[i] = max(A[i], RMax[i + 1])

    i = j = 0
    maxDiff = -1
    while(j < n and i < n):
        if LMin[i] < RMax[j]:
            maxDiff = max(maxDiff, j-i)
            j += 1
        else:
            i += 1
    return maxDiff

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
print(maxIndexDiff(arr))
