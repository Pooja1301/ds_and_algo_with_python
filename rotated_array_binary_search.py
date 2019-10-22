"""
Given a sorted array which is rotated at some unknown pivot
Search given value in the given array
e.g.: Input: [4,5,6,7,0,1,2] and value= 5
Output: 1
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = self.findPivot(A, 0, len(A) - 1)
        if (pivot == -1):
            return self.binarySearch(A, 0, len(A) - 1, B)
        elif (A[pivot] == B):
            return pivot
        elif (A[0] <= B):
            return self.binarySearch(A, 0, pivot - 1, B)
        return self.binarySearch(A, pivot + 1, len(A) - 1, B)

    def findPivot( self,A, low, high):
        if (high < low):
            return -1
        elif (high == low):
            return low
        mid = low + (high - low) // 2

        if (mid < high and A[mid] > A[mid + 1]):
            return mid
        elif (mid > low and A[mid] < A[mid - 1]):
            return mid - 1
        elif (A[mid] <= A[low]):
            return self.findPivot(A, low, mid - 1)
        return self.findPivot(A, mid + 1, high)

    def binarySearch(self, A, low, high, B):
        if (high < low):
            return -1
        mid = low + (high - low) // 2
        if (B == A[mid]):
            return mid
        elif (B > A[mid]):
            return self.binarySearch(A, mid + 1, high, B)
        return self.binarySearch(A, low, mid - 1, B)

print(Solution().search([4,5,6,7,0,1,2], 0))