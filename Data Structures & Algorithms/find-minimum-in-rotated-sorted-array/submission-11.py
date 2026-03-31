class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])  
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])  
                l = mid + 1
            else:
                r = mid - 1
        return res      