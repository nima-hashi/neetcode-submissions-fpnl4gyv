class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # freqCount = {}
        # for num in nums:
        #     freqCount[num] = freqCount.get(num, 0) + 1

        # buckets = [[] for i in range(len(k+1))]
        # for num in freqCount:
        #     buckets[freqCount[num]].append(num)
        
        # res = []
        # for i in range(len(buckets)-1, -1, -1):
        #     for elm in

        freqCount = {}
        for num in nums:
            freqCount[num] = freqCount.get(num, 0) + 1

        arr = []
        for num, cnt in freqCount.items():
            arr.append([cnt, num])
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        


        