class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        total = 0
        count = {0:1}

        cur = 0
        for num in nums:
            cur += num
            # if (cur - k) in count:
            #     total += count[cur - k]
            total += count.get(cur - k, 0) 
            count[cur] = count.get(cur, 0) + 1
        return total

            

        