class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        bucket = [[] for i in range(len(nums))]

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for key, v in counter.items():
            bucket[v-1].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res


        

        