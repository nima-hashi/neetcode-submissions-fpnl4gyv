from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quickSort(nums, l, r):
            if r <= l:
                return 
                
            pivot = nums[r]
            i = l-1
            #j = l
            #while j < r:
            for j in range(l,r):
                #if nums[j] > pivot:
                    #j += 1
                #else:
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]

            quickSort(nums,l,i-1)
            quickSort(nums,i+1,r)

        quickSort(nums, 0, len(nums)-1)
        