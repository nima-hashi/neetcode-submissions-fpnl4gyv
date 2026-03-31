class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result, count = [], {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                #print(n)
                result.append(n)
                if len(result) == k:
                    return result
