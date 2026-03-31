class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        m = float('inf')

        while l <= r:
            if nums[l] <= nums[r]:
                return min(nums[l],m)

            mid = (l+r)//2
            m = min(nums[mid], m)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1


        