class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLen = float("inf")

        l = r = 0
        curSum = 0

        while r < len(nums):
            curSum += nums[r]
            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
            r += 1
        return 0 if minLen == float("inf") else minLen