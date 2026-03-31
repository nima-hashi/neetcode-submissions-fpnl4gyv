import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            i = left - 1
            for j in range(left, right):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[right] = nums[right], nums[i+1]
            return i + 1

        def quickSort(nums, left, right):
            while left < right:
                p = partition(nums, left, right)
                if p - left < right - p:  # recurse into smaller side first
                    quickSort(nums, left, p - 1)
                    left = p + 1
                else:
                    quickSort(nums, p + 1, right)
                    right = p - 1

        quickSort(nums, 0, len(nums) - 1)
        return nums
