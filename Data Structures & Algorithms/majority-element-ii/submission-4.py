class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = []
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for k, v in freq.items():
            if v > (len(nums) // 3):
                res.append(k)
        return res
        