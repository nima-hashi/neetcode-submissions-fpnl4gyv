class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sums = {0: 1}    
        curSum = 0
        res = 0
        
        for n in nums:
            curSum += n

            # If there exists a prefix_sum such that curSum - prefix_sum == k
            if curSum - k in sums:
                res += sums[curSum - k]

            # Store current prefix sum
            sums[curSum] = sums.get(curSum, 0) + 1

        return res