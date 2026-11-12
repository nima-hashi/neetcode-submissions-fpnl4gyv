class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        res = None

        for num in nums:
            if count == 0:
                count = 1
                res = num
            elif res == num:
                count += 1
            else:
                count -= 1
        return res
        