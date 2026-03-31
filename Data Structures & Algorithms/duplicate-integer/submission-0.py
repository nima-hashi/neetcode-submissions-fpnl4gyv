class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                return True
        return False
        