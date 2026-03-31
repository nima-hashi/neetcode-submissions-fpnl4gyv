class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        curMin = float("inf")

        while l <= r:
            mid = (l + r) // 2
            curMin = min(nums[mid], curMin)
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                curMin = min(curMin, nums[l])
                l = mid + 1
        return curMin



        