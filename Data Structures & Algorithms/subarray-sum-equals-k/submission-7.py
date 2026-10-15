class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum = {0:1}
        subArr = 0
        curSum = 0

        for num in nums:
            curSum += num
            if (curSum - k) in prefixSum:
                subArr += prefixSum[curSum - k]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return subArr



        