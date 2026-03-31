class Solution:
    def existsTarget(self, row, target):
        l = 0
        r = len(row)
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            midRow = (l+r) // 2
            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                return self.existsTarget(matrix[midRow], target)
            if target > matrix[midRow][-1]:
                l = midRow + 1
            else:
                r = midRow - 1
        return False
            
        