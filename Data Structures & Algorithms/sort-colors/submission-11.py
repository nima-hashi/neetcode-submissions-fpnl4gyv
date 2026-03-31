class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1
        i = 0 

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1

        # def partition(nums, left, right):
        #     pivot = nums[right]
        #     i, j = left,right-1
        #     while i < j:
        #         while i < right and nums[i] < pivot:
        #             i += 1
        #         while j > left and nums[j] >= pivot:
        #             j -= 1
        #         if i < j:
        #             nums[i], nums[j] = nums[j], nums[i]

        #     if nums[i] > nums[right]:
        #         nums[i], nums[right] = nums[right], nums[i]
            
        #     return i

        # def quickSort(nums, left, right):
        #     if left < right:
        #         partition_pos = partition(nums, left, right)
        #         quickSort(nums, left, partition_pos - 1)
        #         quickSort(nums, partition_pos + 1, right)

        # quickSort(nums, 0, len(nums) - 1)

        # def mergeSort(nums):
        #     if len(nums) > 1:
        #         left = nums[:len(nums)//2]
        #         right = nums[len(nums)//2:]

        #         mergeSort(left)
        #         mergeSort(right)

        #         i, j, k = 0,0,0

        #         while i < len(left) and j < len(right):
        #             if left[i] < right[j]:
        #                 nums[k] = left[i]
        #                 i += 1
        #             else:
        #                 nums[k] = right[j]
        #                 j += 1
        #             k += 1

        #         while i < len(left):
        #                 nums[k] = left[i]
        #                 i += 1
        #                 k += 1
        #         while j < len(right):
        #                 nums[k] = right[j]
        #                 j += 1
        #                 k += 1
        # mergeSort(nums)