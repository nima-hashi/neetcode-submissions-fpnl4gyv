class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numCount = {}

        for num in nums:
            if num not in numCount:
                numCount[num] = 1
            else:
                numCount[num] += 1
        # {1:1,2:2,3:3}
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in numCount.items():
            freq[c].append(n)

        mostFreq = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                mostFreq.append(n)
                if len(mostFreq) == k:
                    return mostFreq 

        