from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        bucket = [[] for _ in range(len(nums) + 1)]
        hm = Counter(nums) # {1:1, 2:2, 3:3}

        for key in hm:
            bucket[hm[key] - 1].append(key)

        for i in range(len(nums) - 1 , -1 , -1):
            for j in bucket[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res



        