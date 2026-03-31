class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums, left, right):
            pivot = nums[right]
            i, j = left,right-1
            while i < j:
                while i < right and nums[i] < pivot:
                    i += 1
                while j > left and nums[j] >= pivot:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            if nums[i] > nums[right]:
                nums[i], nums[right] = nums[right], nums[i]
            
            return i

        def quickSort(nums, left, right):
            if left < right:
                partition_pos = partition(nums, left, right)
                quickSort(nums, left, partition_pos - 1)
                quickSort(nums, partition_pos + 1, right)
        
        quickSort(nums, 0, len(nums) - 1)

        