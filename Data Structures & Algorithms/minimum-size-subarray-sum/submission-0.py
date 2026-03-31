class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        curMin = float("inf")
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            # shrink the window while it's valid
            while total >= target:
                curMin = min(curMin, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if curMin == float("inf") else curMin
