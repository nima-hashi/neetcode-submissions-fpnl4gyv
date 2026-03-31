from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
            if len(hm) > 2:
                for n in list(hm.keys()):
                    hm[n] -= 1
                    if hm[n] == 0:
                        del hm[n]
        res = []
        for n in hm:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res


        