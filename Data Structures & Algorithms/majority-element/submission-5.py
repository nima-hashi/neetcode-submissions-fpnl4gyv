class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = nums[0] # rand variable
        c = 0

        for n in nums:
            if c == 0:
                res = n
                c += 1
            else:
                if n == res:
                    c += 1
                else:
                    c -=1
        return res


        