class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(x,y):
            nums[x], nums[y] = nums[y], nums[x]

        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                # nums[i], nums[l] = nums[l], nums[i]
                swap(i,l)
                l += 1
            if nums[i] == 2:
                # nums[i], nums[r] = nums[r], nums[i]
                swap(i,r)
                r -=1
                i -= 1
            i += 1
            
        