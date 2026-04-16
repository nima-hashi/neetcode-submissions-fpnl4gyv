class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # l = 0
        # r = len(arr) - 1

        # while l < r and r-l+1 > k:
        #     if abs(arr[l] - x) > abs(arr[r] - x):
        #         l += 1
        #     elif abs(arr[l] - x) < abs(arr[r] - x):
        #         r -= 1
        #     else:
        #         if abs(arr[l+1] - x) < abs(arr[r] - x):
        #             r -= 1
        #         else:
        #             l += 1
        # return arr[l:r+1]

        l = 0
        for r in range(k, len(arr)):
            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
        return arr[l:l+k]





        