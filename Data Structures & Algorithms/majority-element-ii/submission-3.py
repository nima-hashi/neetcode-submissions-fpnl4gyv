class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        top2 = {}

        for n in nums:
            top2[n] = top2.get(n, 0) + 1
            if len(top2) <= 2:
                continue
            newTop2 = {}
            for k, v in top2.items():
                if v-1>0:
                    newTop2[k] = v-1
            top2 = newTop2

        res = []
        for k in top2:
            if nums.count(k) > len(nums)//3:
                res.append(k)
        return res


        