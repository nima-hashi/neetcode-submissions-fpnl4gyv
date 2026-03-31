class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cur = nums[0]
        c = 0

        for n in nums:
            if n == cur:
                c += 1
            else:
                if c-1 <= 0 :
                    cur = n
                c -= 1
        return cur


        