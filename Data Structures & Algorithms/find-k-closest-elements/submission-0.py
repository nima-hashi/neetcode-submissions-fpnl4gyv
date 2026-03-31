class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
         # Binary search to find the insert position of x
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        # Initialize two pointers around the insert position
        left, right = l - 1, l

        # Expand window to include k closest elements
        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1

        # Return sorted slice of k elements
        return arr[left + 1:right]