def rotate(A):
    transpose(A)
    reverseRows(A)
    return A

def transpose(A):
    for i in range(len(A[0])):
      for j in range(i, len(A)):
        A[i][j] , A[j][i] = A[j][i], A[i][j]

def reverseRows(A):
    for i in range(len(A)):
      j = 0
      k = len(A) - 1
      while(j<k):
        A[i][j], A[i][k] = A[i][k], A[i][j]
        j += 1
        k -= 1

A = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(A))