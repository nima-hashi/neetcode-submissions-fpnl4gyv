class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        if hm.values():
            return max(hm.values()) >= 2
        return False
        