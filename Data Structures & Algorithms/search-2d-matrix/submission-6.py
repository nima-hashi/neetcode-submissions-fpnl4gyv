class Solution:
    def binarySearch(self, L, target):
        l = 0
        r = len(L) - 1 

        while l <= r:
            m = (l + r) // 2
            if L[m] == target:
                return True
            elif L[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1

        while l <= r:
            midList = (l + r) // 2
            
            if matrix[midList][0] <= target <= matrix[midList][-1]:
                return self.binarySearch(matrix[midList], target)

            elif target < matrix[midList][0]:
                r = midList - 1
            
            else:
                l = midList + 1

        return False

        
        