class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(A):
        mat=[[0 for j in range(i+1)] for i in range(A)]


        for i in range(A):
            for j in range(i+1):
                if j == 0 or j == i:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i-1][j] + mat[i-1][j-1]
        return mat

    print(solve(5))